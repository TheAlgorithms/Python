import logging
import sys
from typing import TYPE_CHECKING, Any, FrozenSet, Iterable, Optional, Tuple, Union, cast

from pip._vendor.packaging.specifiers import InvalidSpecifier, SpecifierSet
from pip._vendor.packaging.utils import NormalizedName, canonicalize_name
from pip._vendor.packaging.version import Version
from pip._vendor.packaging.version import parse as parse_version
from pip._vendor.pkg_resources import Distribution

from pip._internal.exceptions import HashError, MetadataInconsistent
from pip._internal.models.link import Link, links_equivalent
from pip._internal.models.wheel import Wheel
from pip._internal.req.constructors import (
    install_req_from_editable,
    install_req_from_line,
)
from pip._internal.req.req_install import InstallRequirement
from pip._internal.utils.misc import dist_is_editable, normalize_version_info
from pip._internal.utils.packaging import get_requires_python

from .base import Candidate, CandidateVersion, Requirement, format_name

if TYPE_CHECKING:
    from .factory import Factory

logger = logging.getLogger(__name__)

BaseCandidate = Union[
    "AlreadyInstalledCandidate",
    "EditableCandidate",
    "LinkCandidate",
]


def as_base_candidate(candidate: Candidate) -> Optional[BaseCandidate]:
    """The runtime version of BaseCandidate."""
    base_candidate_classes = (
        AlreadyInstalledCandidate,
        EditableCandidate,
        LinkCandidate,
    )
    if isinstance(candidate, base_candidate_classes):
        return candidate
    return None


def make_install_req_from_link(link, template):
    # type: (Link, InstallRequirement) -> InstallRequirement
    assert not template.editable, "template is editable"
    if template.req:
        line = str(template.req)
    else:
        line = link.url
    ireq = install_req_from_line(
        line,
        user_supplied=template.user_supplied,
        comes_from=template.comes_from,
        use_pep517=template.use_pep517,
        isolated=template.isolated,
        constraint=template.constraint,
        options=dict(
            install_options=template.install_options,
            global_options=template.global_options,
            hashes=template.hash_options,
        ),
    )
    ireq.original_link = template.original_link
    ireq.link = link
    return ireq


def make_install_req_from_editable(link, template):
    # type: (Link, InstallRequirement) -> InstallRequirement
    assert template.editable, "template not editable"
    return install_req_from_editable(
        link.url,
        user_supplied=template.user_supplied,
        comes_from=template.comes_from,
        use_pep517=template.use_pep517,
        isolated=template.isolated,
        constraint=template.constraint,
        options=dict(
            install_options=template.install_options,
            global_options=template.global_options,
            hashes=template.hash_options,
        ),
    )


def make_install_req_from_dist(dist, template):
    # type: (Distribution, InstallRequirement) -> InstallRequirement
    project_name = canonicalize_name(dist.project_name)
    if template.req:
        line = str(template.req)
    elif template.link:
        line = f"{project_name} @ {template.link.url}"
    else:
        line = f"{project_name}=={dist.parsed_version}"
    ireq = install_req_from_line(
        line,
        user_supplied=template.user_supplied,
        comes_from=template.comes_from,
        use_pep517=template.use_pep517,
        isolated=template.isolated,
        constraint=template.constraint,
        options=dict(
            install_options=template.install_options,
            global_options=template.global_options,
            hashes=template.hash_options,
        ),
    )
    ireq.satisfied_by = dist
    return ireq


class _InstallRequirementBackedCandidate(Candidate):
    """A candidate backed by an ``InstallRequirement``.

    This represents a package request with the target not being already
    in the environment, and needs to be fetched and installed. The backing
    ``InstallRequirement`` is responsible for most of the leg work; this
    class exposes appropriate information to the resolver.

    :param link: The link passed to the ``InstallRequirement``. The backing
        ``InstallRequirement`` will use this link to fetch the distribution.
    :param source_link: The link this candidate "originates" from. This is
        different from ``link`` when the link is found in the wheel cache.
        ``link`` would point to the wheel cache, while this points to the
        found remote link (e.g. from pypi.org).
    """

    is_installed = False

    def __init__(
        self,
        link,  # type: Link
        source_link,  # type: Link
        ireq,  # type: InstallRequirement
        factory,  # type: Factory
        name=None,  # type: Optional[NormalizedName]
        version=None,  # type: Optional[CandidateVersion]
    ):
        # type: (...) -> None
        self._link = link
        self._source_link = source_link
        self._factory = factory
        self._ireq = ireq
        self._name = name
        self._version = version
        self.dist = self._prepare()

    def __str__(self):
        # type: () -> str
        return f"{self.name} {self.version}"

    def __repr__(self):
        # type: () -> str
        return "{class_name}({link!r})".format(
            class_name=self.__class__.__name__,
            link=str(self._link),
        )

    def __hash__(self):
        # type: () -> int
        return hash((self.__class__, self._link))

    def __eq__(self, other):
        # type: (Any) -> bool
        if isinstance(other, self.__class__):
            return links_equivalent(self._link, other._link)
        return False

    @property
    def source_link(self):
        # type: () -> Optional[Link]
        return self._source_link

    @property
    def project_name(self):
        # type: () -> NormalizedName
        """The normalised name of the project the candidate refers to"""
        if self._name is None:
            self._name = canonicalize_name(self.dist.project_name)
        return self._name

    @property
    def name(self):
        # type: () -> str
        return self.project_name

    @property
    def version(self):
        # type: () -> CandidateVersion
        if self._version is None:
            self._version = parse_version(self.dist.version)
        return self._version

    def format_for_error(self):
        # type: () -> str
        return "{} {} (from {})".format(
            self.name,
            self.version,
            self._link.file_path if self._link.is_file else self._link,
        )

    def _prepare_distribution(self):
        # type: () -> Distribution
        raise NotImplementedError("Override in subclass")

    def _check_metadata_consistency(self, dist):
        # type: (Distribution) -> None
        """Check for consistency of project name and version of dist."""
        canonical_name = canonicalize_name(dist.project_name)
        if self._name is not None and self._name != canonical_name:
            raise MetadataInconsistent(
                self._ireq,
                "name",
                self._name,
                dist.project_name,
            )
        parsed_version = parse_version(dist.version)
        if self._version is not None and self._version != parsed_version:
            raise MetadataInconsistent(
                self._ireq,
                "version",
                str(self._version),
                dist.version,
            )

    def _prepare(self):
        # type: () -> Distribution
        try:
            dist = self._prepare_distribution()
        except HashError as e:
            # Provide HashError the underlying ireq that caused it. This
            # provides context for the resulting error message to show the
            # offending line to the user.
            e.req = self._ireq
            raise
        self._check_metadata_consistency(dist)
        return dist

    def _get_requires_python_dependency(self):
        # type: () -> Optional[Requirement]
        requires_python = get_requires_python(self.dist)
        if requires_python is None:
            return None
        try:
            spec = SpecifierSet(requires_python)
        except InvalidSpecifier as e:
            message = "Package %r has an invalid Requires-Python: %s"
            logger.warning(message, self.name, e)
            return None
        return self._factory.make_requires_python_requirement(spec)

    def iter_dependencies(self, with_requires):
        # type: (bool) -> Iterable[Optional[Requirement]]
        requires = self.dist.requires() if with_requires else ()
        for r in requires:
            yield self._factory.make_requirement_from_spec(str(r), self._ireq)
        yield self._get_requires_python_dependency()

    def get_install_requirement(self):
        # type: () -> Optional[InstallRequirement]
        return self._ireq


class LinkCandidate(_InstallRequirementBackedCandidate):
    is_editable = False

    def __init__(
        self,
        link,  # type: Link
        template,  # type: InstallRequirement
        factory,  # type: Factory
        name=None,  # type: Optional[NormalizedName]
        version=None,  # type: Optional[CandidateVersion]
    ):
        # type: (...) -> None
        source_link = link
        cache_entry = factory.get_wheel_cache_entry(link, name)
        if cache_entry is not None:
            logger.debug("Using cached wheel link: %s", cache_entry.link)
            link = cache_entry.link
        ireq = make_install_req_from_link(link, template)
        assert ireq.link == link
        if ireq.link.is_wheel and not ireq.link.is_file:
            wheel = Wheel(ireq.link.filename)
            wheel_name = canonicalize_name(wheel.name)
            assert name == wheel_name, f"{name!r} != {wheel_name!r} for wheel"
            # Version may not be present for PEP 508 direct URLs
            if version is not None:
                wheel_version = Version(wheel.version)
                assert version == wheel_version, "{!r} != {!r} for wheel {}".format(
                    version, wheel_version, name
                )

        if (
            cache_entry is not None
            and cache_entry.persistent
            and template.link is template.original_link
        ):
            ireq.original_link_is_in_wheel_cache = True

        super().__init__(
            link=link,
            source_link=source_link,
            ireq=ireq,
            factory=factory,
            name=name,
            version=version,
        )

    def _prepare_distribution(self):
        # type: () -> Distribution
        return self._factory.preparer.prepare_linked_requirement(
            self._ireq, parallel_builds=True
        )


class EditableCandidate(_InstallRequirementBackedCandidate):
    is_editable = True

    def __init__(
        self,
        link,  # type: Link
        template,  # type: InstallRequirement
        factory,  # type: Factory
        name=None,  # type: Optional[NormalizedName]
        version=None,  # type: Optional[CandidateVersion]
    ):
        # type: (...) -> None
        super().__init__(
            link=link,
            source_link=link,
            ireq=make_install_req_from_editable(link, template),
            factory=factory,
            name=name,
            version=version,
        )

    def _prepare_distribution(self):
        # type: () -> Distribution
        return self._factory.preparer.prepare_editable_requirement(self._ireq)


class AlreadyInstalledCandidate(Candidate):
    is_installed = True
    source_link = None

    def __init__(
        self,
        dist,  # type: Distribution
        template,  # type: InstallRequirement
        factory,  # type: Factory
    ):
        # type: (...) -> None
        self.dist = dist
        self._ireq = make_install_req_from_dist(dist, template)
        self._factory = factory

        # This is just logging some messages, so we can do it eagerly.
        # The returned dist would be exactly the same as self.dist because we
        # set satisfied_by in make_install_req_from_dist.
        # TODO: Supply reason based on force_reinstall and upgrade_strategy.
        skip_reason = "already satisfied"
        factory.preparer.prepare_installed_requirement(self._ireq, skip_reason)

    def __str__(self):
        # type: () -> str
        return str(self.dist)

    def __repr__(self):
        # type: () -> str
        return "{class_name}({distribution!r})".format(
            class_name=self.__class__.__name__,
            distribution=self.dist,
        )

    def __hash__(self):
        # type: () -> int
        return hash((self.__class__, self.name, self.version))

    def __eq__(self, other):
        # type: (Any) -> bool
        if isinstance(other, self.__class__):
            return self.name == other.name and self.version == other.version
        return False

    @property
    def project_name(self):
        # type: () -> NormalizedName
        return canonicalize_name(self.dist.project_name)

    @property
    def name(self):
        # type: () -> str
        return self.project_name

    @property
    def version(self):
        # type: () -> CandidateVersion
        return parse_version(self.dist.version)

    @property
    def is_editable(self):
        # type: () -> bool
        return dist_is_editable(self.dist)

    def format_for_error(self):
        # type: () -> str
        return f"{self.name} {self.version} (Installed)"

    def iter_dependencies(self, with_requires):
        # type: (bool) -> Iterable[Optional[Requirement]]
        if not with_requires:
            return
        for r in self.dist.requires():
            yield self._factory.make_requirement_from_spec(str(r), self._ireq)

    def get_install_requirement(self):
        # type: () -> Optional[InstallRequirement]
        return None


class ExtrasCandidate(Candidate):
    """A candidate that has 'extras', indicating additional dependencies.

    Requirements can be for a project with dependencies, something like
    foo[extra].  The extras don't affect the project/version being installed
    directly, but indicate that we need additional dependencies. We model that
    by having an artificial ExtrasCandidate that wraps the "base" candidate.

    The ExtrasCandidate differs from the base in the following ways:

    1. It has a unique name, of the form foo[extra]. This causes the resolver
       to treat it as a separate node in the dependency graph.
    2. When we're getting the candidate's dependencies,
       a) We specify that we want the extra dependencies as well.
       b) We add a dependency on the base candidate.
          See below for why this is needed.
    3. We return None for the underlying InstallRequirement, as the base
       candidate will provide it, and we don't want to end up with duplicates.

    The dependency on the base candidate is needed so that the resolver can't
    decide that it should recommend foo[extra1] version 1.0 and foo[extra2]
    version 2.0. Having those candidates depend on foo=1.0 and foo=2.0
    respectively forces the resolver to recognise that this is a conflict.
    """

    def __init__(
        self,
        base,  # type: BaseCandidate
        extras,  # type: FrozenSet[str]
    ):
        # type: (...) -> None
        self.base = base
        self.extras = extras

    def __str__(self):
        # type: () -> str
        name, rest = str(self.base).split(" ", 1)
        return "{}[{}] {}".format(name, ",".join(self.extras), rest)

    def __repr__(self):
        # type: () -> str
        return "{class_name}(base={base!r}, extras={extras!r})".format(
            class_name=self.__class__.__name__,
            base=self.base,
            extras=self.extras,
        )

    def __hash__(self):
        # type: () -> int
        return hash((self.base, self.extras))

    def __eq__(self, other):
        # type: (Any) -> bool
        if isinstance(other, self.__class__):
            return self.base == other.base and self.extras == other.extras
        return False

    @property
    def project_name(self):
        # type: () -> NormalizedName
        return self.base.project_name

    @property
    def name(self):
        # type: () -> str
        """The normalised name of the project the candidate refers to"""
        return format_name(self.base.project_name, self.extras)

    @property
    def version(self):
        # type: () -> CandidateVersion
        return self.base.version

    def format_for_error(self):
        # type: () -> str
        return "{} [{}]".format(
            self.base.format_for_error(), ", ".join(sorted(self.extras))
        )

    @property
    def is_installed(self):
        # type: () -> bool
        return self.base.is_installed

    @property
    def is_editable(self):
        # type: () -> bool
        return self.base.is_editable

    @property
    def source_link(self):
        # type: () -> Optional[Link]
        return self.base.source_link

    def iter_dependencies(self, with_requires):
        # type: (bool) -> Iterable[Optional[Requirement]]
        factory = self.base._factory

        # Add a dependency on the exact base
        # (See note 2b in the class docstring)
        yield factory.make_requirement_from_candidate(self.base)
        if not with_requires:
            return

        # The user may have specified extras that the candidate doesn't
        # support. We ignore any unsupported extras here.
        valid_extras = self.extras.intersection(self.base.dist.extras)
        invalid_extras = self.extras.difference(self.base.dist.extras)
        for extra in sorted(invalid_extras):
            logger.warning(
                "%s %s does not provide the extra '%s'",
                self.base.name,
                self.version,
                extra,
            )

        for r in self.base.dist.requires(valid_extras):
            requirement = factory.make_requirement_from_spec(
                str(r), self.base._ireq, valid_extras
            )
            if requirement:
                yield requirement

    def get_install_requirement(self):
        # type: () -> Optional[InstallRequirement]
        # We don't return anything here, because we always
        # depend on the base candidate, and we'll get the
        # install requirement from that.
        return None


class RequiresPythonCandidate(Candidate):
    is_installed = False
    source_link = None

    def __init__(self, py_version_info):
        # type: (Optional[Tuple[int, ...]]) -> None
        if py_version_info is not None:
            version_info = normalize_version_info(py_version_info)
        else:
            version_info = sys.version_info[:3]
        self._version = Version(".".join(str(c) for c in version_info))

    # We don't need to implement __eq__() and __ne__() since there is always
    # only one RequiresPythonCandidate in a resolution, i.e. the host Python.
    # The built-in object.__eq__() and object.__ne__() do exactly what we want.

    def __str__(self):
        # type: () -> str
        return f"Python {self._version}"

    @property
    def project_name(self):
        # type: () -> NormalizedName
        # Avoid conflicting with the PyPI package "Python".
        return cast(NormalizedName, "<Python from Requires-Python>")

    @property
    def name(self):
        # type: () -> str
        return self.project_name

    @property
    def version(self):
        # type: () -> CandidateVersion
        return self._version

    def format_for_error(self):
        # type: () -> str
        return f"Python {self.version}"

    def iter_dependencies(self, with_requires):
        # type: (bool) -> Iterable[Optional[Requirement]]
        return ()

    def get_install_requirement(self):
        # type: () -> Optional[InstallRequirement]
        return None
