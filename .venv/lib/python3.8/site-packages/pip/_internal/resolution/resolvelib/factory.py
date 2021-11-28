import contextlib
import functools
import logging
from typing import (
    TYPE_CHECKING,
    Dict,
    FrozenSet,
    Iterable,
    Iterator,
    List,
    Mapping,
    Optional,
    Sequence,
    Set,
    Tuple,
    TypeVar,
    cast,
)

from pip._vendor.packaging.requirements import InvalidRequirement
from pip._vendor.packaging.requirements import Requirement as PackagingRequirement
from pip._vendor.packaging.specifiers import SpecifierSet
from pip._vendor.packaging.utils import NormalizedName, canonicalize_name
from pip._vendor.pkg_resources import Distribution
from pip._vendor.resolvelib import ResolutionImpossible

from pip._internal.cache import CacheEntry, WheelCache
from pip._internal.exceptions import (
    DistributionNotFound,
    InstallationError,
    InstallationSubprocessError,
    MetadataInconsistent,
    UnsupportedPythonVersion,
    UnsupportedWheel,
)
from pip._internal.index.package_finder import PackageFinder
from pip._internal.models.link import Link
from pip._internal.models.wheel import Wheel
from pip._internal.operations.prepare import RequirementPreparer
from pip._internal.req.constructors import install_req_from_link_and_ireq
from pip._internal.req.req_install import InstallRequirement
from pip._internal.resolution.base import InstallRequirementProvider
from pip._internal.utils.compatibility_tags import get_supported
from pip._internal.utils.hashes import Hashes
from pip._internal.utils.misc import (
    dist_in_site_packages,
    dist_in_usersite,
    get_installed_distributions,
)
from pip._internal.utils.virtualenv import running_under_virtualenv

from .base import Candidate, CandidateVersion, Constraint, Requirement
from .candidates import (
    AlreadyInstalledCandidate,
    BaseCandidate,
    EditableCandidate,
    ExtrasCandidate,
    LinkCandidate,
    RequiresPythonCandidate,
    as_base_candidate,
)
from .found_candidates import FoundCandidates, IndexCandidateInfo
from .requirements import (
    ExplicitRequirement,
    RequiresPythonRequirement,
    SpecifierRequirement,
    UnsatisfiableRequirement,
)

if TYPE_CHECKING:
    from typing import Protocol

    class ConflictCause(Protocol):
        requirement: RequiresPythonRequirement
        parent: Candidate


logger = logging.getLogger(__name__)

C = TypeVar("C")
Cache = Dict[Link, C]


class Factory:
    def __init__(
        self,
        finder,  # type: PackageFinder
        preparer,  # type: RequirementPreparer
        make_install_req,  # type: InstallRequirementProvider
        wheel_cache,  # type: Optional[WheelCache]
        use_user_site,  # type: bool
        force_reinstall,  # type: bool
        ignore_installed,  # type: bool
        ignore_requires_python,  # type: bool
        py_version_info=None,  # type: Optional[Tuple[int, ...]]
    ):
        # type: (...) -> None
        self._finder = finder
        self.preparer = preparer
        self._wheel_cache = wheel_cache
        self._python_candidate = RequiresPythonCandidate(py_version_info)
        self._make_install_req_from_spec = make_install_req
        self._use_user_site = use_user_site
        self._force_reinstall = force_reinstall
        self._ignore_requires_python = ignore_requires_python

        self._build_failures = {}  # type: Cache[InstallationError]
        self._link_candidate_cache = {}  # type: Cache[LinkCandidate]
        self._editable_candidate_cache = {}  # type: Cache[EditableCandidate]
        self._installed_candidate_cache = (
            {}
        )  # type: Dict[str, AlreadyInstalledCandidate]
        self._extras_candidate_cache = (
            {}
        )  # type: Dict[Tuple[int, FrozenSet[str]], ExtrasCandidate]

        if not ignore_installed:
            self._installed_dists = {
                canonicalize_name(dist.project_name): dist
                for dist in get_installed_distributions(local_only=False)
            }
        else:
            self._installed_dists = {}

    @property
    def force_reinstall(self):
        # type: () -> bool
        return self._force_reinstall

    def _fail_if_link_is_unsupported_wheel(self, link: Link) -> None:
        if not link.is_wheel:
            return
        wheel = Wheel(link.filename)
        if wheel.supported(self._finder.target_python.get_tags()):
            return
        msg = f"{link.filename} is not a supported wheel on this platform."
        raise UnsupportedWheel(msg)

    def _make_extras_candidate(self, base, extras):
        # type: (BaseCandidate, FrozenSet[str]) -> ExtrasCandidate
        cache_key = (id(base), extras)
        try:
            candidate = self._extras_candidate_cache[cache_key]
        except KeyError:
            candidate = ExtrasCandidate(base, extras)
            self._extras_candidate_cache[cache_key] = candidate
        return candidate

    def _make_candidate_from_dist(
        self,
        dist,  # type: Distribution
        extras,  # type: FrozenSet[str]
        template,  # type: InstallRequirement
    ):
        # type: (...) -> Candidate
        try:
            base = self._installed_candidate_cache[dist.key]
        except KeyError:
            base = AlreadyInstalledCandidate(dist, template, factory=self)
            self._installed_candidate_cache[dist.key] = base
        if not extras:
            return base
        return self._make_extras_candidate(base, extras)

    def _make_candidate_from_link(
        self,
        link,  # type: Link
        extras,  # type: FrozenSet[str]
        template,  # type: InstallRequirement
        name,  # type: Optional[NormalizedName]
        version,  # type: Optional[CandidateVersion]
    ):
        # type: (...) -> Optional[Candidate]
        # TODO: Check already installed candidate, and use it if the link and
        # editable flag match.

        if link in self._build_failures:
            # We already tried this candidate before, and it does not build.
            # Don't bother trying again.
            return None

        if template.editable:
            if link not in self._editable_candidate_cache:
                try:
                    self._editable_candidate_cache[link] = EditableCandidate(
                        link,
                        template,
                        factory=self,
                        name=name,
                        version=version,
                    )
                except (InstallationSubprocessError, MetadataInconsistent) as e:
                    logger.warning("Discarding %s. %s", link, e)
                    self._build_failures[link] = e
                    return None
            base = self._editable_candidate_cache[link]  # type: BaseCandidate
        else:
            if link not in self._link_candidate_cache:
                try:
                    self._link_candidate_cache[link] = LinkCandidate(
                        link,
                        template,
                        factory=self,
                        name=name,
                        version=version,
                    )
                except (InstallationSubprocessError, MetadataInconsistent) as e:
                    logger.warning("Discarding %s. %s", link, e)
                    self._build_failures[link] = e
                    return None
            base = self._link_candidate_cache[link]

        if not extras:
            return base
        return self._make_extras_candidate(base, extras)

    def _iter_found_candidates(
        self,
        ireqs: Sequence[InstallRequirement],
        specifier: SpecifierSet,
        hashes: Hashes,
        prefers_installed: bool,
        incompatible_ids: Set[int],
    ) -> Iterable[Candidate]:
        if not ireqs:
            return ()

        # The InstallRequirement implementation requires us to give it a
        # "template". Here we just choose the first requirement to represent
        # all of them.
        # Hopefully the Project model can correct this mismatch in the future.
        template = ireqs[0]
        assert template.req, "Candidates found on index must be PEP 508"
        name = canonicalize_name(template.req.name)

        extras = frozenset()  # type: FrozenSet[str]
        for ireq in ireqs:
            assert ireq.req, "Candidates found on index must be PEP 508"
            specifier &= ireq.req.specifier
            hashes &= ireq.hashes(trust_internet=False)
            extras |= frozenset(ireq.extras)

        # Get the installed version, if it matches, unless the user
        # specified `--force-reinstall`, when we want the version from
        # the index instead.
        installed_candidate = None
        if not self._force_reinstall and name in self._installed_dists:
            installed_dist = self._installed_dists[name]
            if specifier.contains(installed_dist.version, prereleases=True):
                installed_candidate = self._make_candidate_from_dist(
                    dist=installed_dist,
                    extras=extras,
                    template=template,
                )

        def iter_index_candidate_infos():
            # type: () -> Iterator[IndexCandidateInfo]
            result = self._finder.find_best_candidate(
                project_name=name,
                specifier=specifier,
                hashes=hashes,
            )
            icans = list(result.iter_applicable())

            # PEP 592: Yanked releases must be ignored unless only yanked
            # releases can satisfy the version range. So if this is false,
            # all yanked icans need to be skipped.
            all_yanked = all(ican.link.is_yanked for ican in icans)

            # PackageFinder returns earlier versions first, so we reverse.
            for ican in reversed(icans):
                if not all_yanked and ican.link.is_yanked:
                    continue
                func = functools.partial(
                    self._make_candidate_from_link,
                    link=ican.link,
                    extras=extras,
                    template=template,
                    name=name,
                    version=ican.version,
                )
                yield ican.version, func

        return FoundCandidates(
            iter_index_candidate_infos,
            installed_candidate,
            prefers_installed,
            incompatible_ids,
        )

    def _iter_explicit_candidates_from_base(
        self,
        base_requirements: Iterable[Requirement],
        extras: FrozenSet[str],
    ) -> Iterator[Candidate]:
        """Produce explicit candidates from the base given an extra-ed package.

        :param base_requirements: Requirements known to the resolver. The
            requirements are guaranteed to not have extras.
        :param extras: The extras to inject into the explicit requirements'
            candidates.
        """
        for req in base_requirements:
            lookup_cand, _ = req.get_candidate_lookup()
            if lookup_cand is None:  # Not explicit.
                continue
            # We've stripped extras from the identifier, and should always
            # get a BaseCandidate here, unless there's a bug elsewhere.
            base_cand = as_base_candidate(lookup_cand)
            assert base_cand is not None, "no extras here"
            yield self._make_extras_candidate(base_cand, extras)

    def _iter_candidates_from_constraints(
        self,
        identifier: str,
        constraint: Constraint,
        template: InstallRequirement,
    ) -> Iterator[Candidate]:
        """Produce explicit candidates from constraints.

        This creates "fake" InstallRequirement objects that are basically clones
        of what "should" be the template, but with original_link set to link.
        """
        for link in constraint.links:
            self._fail_if_link_is_unsupported_wheel(link)
            candidate = self._make_candidate_from_link(
                link,
                extras=frozenset(),
                template=install_req_from_link_and_ireq(link, template),
                name=canonicalize_name(identifier),
                version=None,
            )
            if candidate:
                yield candidate

    def find_candidates(
        self,
        identifier: str,
        requirements: Mapping[str, Iterator[Requirement]],
        incompatibilities: Mapping[str, Iterator[Candidate]],
        constraint: Constraint,
        prefers_installed: bool,
    ) -> Iterable[Candidate]:
        # Collect basic lookup information from the requirements.
        explicit_candidates = set()  # type: Set[Candidate]
        ireqs = []  # type: List[InstallRequirement]
        for req in requirements[identifier]:
            cand, ireq = req.get_candidate_lookup()
            if cand is not None:
                explicit_candidates.add(cand)
            if ireq is not None:
                ireqs.append(ireq)

        # If the current identifier contains extras, add explicit candidates
        # from entries from extra-less identifier.
        with contextlib.suppress(InvalidRequirement):
            parsed_requirement = PackagingRequirement(identifier)
            explicit_candidates.update(
                self._iter_explicit_candidates_from_base(
                    requirements.get(parsed_requirement.name, ()),
                    frozenset(parsed_requirement.extras),
                ),
            )

        # Add explicit candidates from constraints. We only do this if there are
        # kown ireqs, which represent requirements not already explicit. If
        # there are no ireqs, we're constraining already-explicit requirements,
        # which is handled later when we return the explicit candidates.
        if ireqs:
            try:
                explicit_candidates.update(
                    self._iter_candidates_from_constraints(
                        identifier,
                        constraint,
                        template=ireqs[0],
                    ),
                )
            except UnsupportedWheel:
                # If we're constrained to install a wheel incompatible with the
                # target architecture, no candidates will ever be valid.
                return ()

        # Since we cache all the candidates, incompatibility identification
        # can be made quicker by comparing only the id() values.
        incompat_ids = {id(c) for c in incompatibilities.get(identifier, ())}

        # If none of the requirements want an explicit candidate, we can ask
        # the finder for candidates.
        if not explicit_candidates:
            return self._iter_found_candidates(
                ireqs,
                constraint.specifier,
                constraint.hashes,
                prefers_installed,
                incompat_ids,
            )

        return (
            c
            for c in explicit_candidates
            if id(c) not in incompat_ids
            and constraint.is_satisfied_by(c)
            and all(req.is_satisfied_by(c) for req in requirements[identifier])
        )

    def make_requirement_from_install_req(self, ireq, requested_extras):
        # type: (InstallRequirement, Iterable[str]) -> Optional[Requirement]
        if not ireq.match_markers(requested_extras):
            logger.info(
                "Ignoring %s: markers '%s' don't match your environment",
                ireq.name,
                ireq.markers,
            )
            return None
        if not ireq.link:
            return SpecifierRequirement(ireq)
        self._fail_if_link_is_unsupported_wheel(ireq.link)
        cand = self._make_candidate_from_link(
            ireq.link,
            extras=frozenset(ireq.extras),
            template=ireq,
            name=canonicalize_name(ireq.name) if ireq.name else None,
            version=None,
        )
        if cand is None:
            # There's no way we can satisfy a URL requirement if the underlying
            # candidate fails to build. An unnamed URL must be user-supplied, so
            # we fail eagerly. If the URL is named, an unsatisfiable requirement
            # can make the resolver do the right thing, either backtrack (and
            # maybe find some other requirement that's buildable) or raise a
            # ResolutionImpossible eventually.
            if not ireq.name:
                raise self._build_failures[ireq.link]
            return UnsatisfiableRequirement(canonicalize_name(ireq.name))
        return self.make_requirement_from_candidate(cand)

    def make_requirement_from_candidate(self, candidate):
        # type: (Candidate) -> ExplicitRequirement
        return ExplicitRequirement(candidate)

    def make_requirement_from_spec(
        self,
        specifier,  # type: str
        comes_from,  # type: InstallRequirement
        requested_extras=(),  # type: Iterable[str]
    ):
        # type: (...) -> Optional[Requirement]
        ireq = self._make_install_req_from_spec(specifier, comes_from)
        return self.make_requirement_from_install_req(ireq, requested_extras)

    def make_requires_python_requirement(self, specifier):
        # type: (Optional[SpecifierSet]) -> Optional[Requirement]
        if self._ignore_requires_python or specifier is None:
            return None
        return RequiresPythonRequirement(specifier, self._python_candidate)

    def get_wheel_cache_entry(self, link, name):
        # type: (Link, Optional[str]) -> Optional[CacheEntry]
        """Look up the link in the wheel cache.

        If ``preparer.require_hashes`` is True, don't use the wheel cache,
        because cached wheels, always built locally, have different hashes
        than the files downloaded from the index server and thus throw false
        hash mismatches. Furthermore, cached wheels at present have
        nondeterministic contents due to file modification times.
        """
        if self._wheel_cache is None or self.preparer.require_hashes:
            return None
        return self._wheel_cache.get_cache_entry(
            link=link,
            package_name=name,
            supported_tags=get_supported(),
        )

    def get_dist_to_uninstall(self, candidate):
        # type: (Candidate) -> Optional[Distribution]
        # TODO: Are there more cases this needs to return True? Editable?
        dist = self._installed_dists.get(candidate.project_name)
        if dist is None:  # Not installed, no uninstallation required.
            return None

        # We're installing into global site. The current installation must
        # be uninstalled, no matter it's in global or user site, because the
        # user site installation has precedence over global.
        if not self._use_user_site:
            return dist

        # We're installing into user site. Remove the user site installation.
        if dist_in_usersite(dist):
            return dist

        # We're installing into user site, but the installed incompatible
        # package is in global site. We can't uninstall that, and would let
        # the new user installation to "shadow" it. But shadowing won't work
        # in virtual environments, so we error out.
        if running_under_virtualenv() and dist_in_site_packages(dist):
            raise InstallationError(
                "Will not install to the user site because it will "
                "lack sys.path precedence to {} in {}".format(
                    dist.project_name,
                    dist.location,
                )
            )
        return None

    def _report_requires_python_error(self, causes):
        # type: (Sequence[ConflictCause]) -> UnsupportedPythonVersion
        assert causes, "Requires-Python error reported with no cause"

        version = self._python_candidate.version

        if len(causes) == 1:
            specifier = str(causes[0].requirement.specifier)
            message = (
                f"Package {causes[0].parent.name!r} requires a different "
                f"Python: {version} not in {specifier!r}"
            )
            return UnsupportedPythonVersion(message)

        message = f"Packages require a different Python. {version} not in:"
        for cause in causes:
            package = cause.parent.format_for_error()
            specifier = str(cause.requirement.specifier)
            message += f"\n{specifier!r} (required by {package})"
        return UnsupportedPythonVersion(message)

    def _report_single_requirement_conflict(self, req, parent):
        # type: (Requirement, Optional[Candidate]) -> DistributionNotFound
        if parent is None:
            req_disp = str(req)
        else:
            req_disp = f"{req} (from {parent.name})"

        cands = self._finder.find_all_candidates(req.project_name)
        versions = [str(v) for v in sorted({c.version for c in cands})]

        logger.critical(
            "Could not find a version that satisfies the requirement %s "
            "(from versions: %s)",
            req_disp,
            ", ".join(versions) or "none",
        )

        return DistributionNotFound(f"No matching distribution found for {req}")

    def get_installation_error(
        self,
        e,  # type: ResolutionImpossible[Requirement, Candidate]
        constraints,  # type: Dict[str, Constraint]
    ):
        # type: (...) -> InstallationError

        assert e.causes, "Installation error reported with no cause"

        # If one of the things we can't solve is "we need Python X.Y",
        # that is what we report.
        requires_python_causes = [
            cause
            for cause in e.causes
            if isinstance(cause.requirement, RequiresPythonRequirement)
            and not cause.requirement.is_satisfied_by(self._python_candidate)
        ]
        if requires_python_causes:
            # The comprehension above makes sure all Requirement instances are
            # RequiresPythonRequirement, so let's cast for convinience.
            return self._report_requires_python_error(
                cast("Sequence[ConflictCause]", requires_python_causes),
            )

        # Otherwise, we have a set of causes which can't all be satisfied
        # at once.

        # The simplest case is when we have *one* cause that can't be
        # satisfied. We just report that case.
        if len(e.causes) == 1:
            req, parent = e.causes[0]
            if req.name not in constraints:
                return self._report_single_requirement_conflict(req, parent)

        # OK, we now have a list of requirements that can't all be
        # satisfied at once.

        # A couple of formatting helpers
        def text_join(parts):
            # type: (List[str]) -> str
            if len(parts) == 1:
                return parts[0]

            return ", ".join(parts[:-1]) + " and " + parts[-1]

        def describe_trigger(parent):
            # type: (Candidate) -> str
            ireq = parent.get_install_requirement()
            if not ireq or not ireq.comes_from:
                return f"{parent.name}=={parent.version}"
            if isinstance(ireq.comes_from, InstallRequirement):
                return str(ireq.comes_from.name)
            return str(ireq.comes_from)

        triggers = set()
        for req, parent in e.causes:
            if parent is None:
                # This is a root requirement, so we can report it directly
                trigger = req.format_for_error()
            else:
                trigger = describe_trigger(parent)
            triggers.add(trigger)

        if triggers:
            info = text_join(sorted(triggers))
        else:
            info = "the requested packages"

        msg = (
            "Cannot install {} because these package versions "
            "have conflicting dependencies.".format(info)
        )
        logger.critical(msg)
        msg = "\nThe conflict is caused by:"

        relevant_constraints = set()
        for req, parent in e.causes:
            if req.name in constraints:
                relevant_constraints.add(req.name)
            msg = msg + "\n    "
            if parent:
                msg = msg + f"{parent.name} {parent.version} depends on "
            else:
                msg = msg + "The user requested "
            msg = msg + req.format_for_error()
        for key in relevant_constraints:
            spec = constraints[key].specifier
            msg += f"\n    The user requested (constraint) {key}{spec}"

        msg = (
            msg
            + "\n\n"
            + "To fix this you could try to:\n"
            + "1. loosen the range of package versions you've specified\n"
            + "2. remove package versions to allow pip attempt to solve "
            + "the dependency conflict\n"
        )

        logger.info(msg)

        return DistributionNotFound(
            "ResolutionImpossible: for help visit "
            "https://pip.pypa.io/en/latest/user_guide/"
            "#fixing-conflicting-dependencies"
        )
