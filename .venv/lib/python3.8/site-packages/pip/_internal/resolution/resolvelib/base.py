from typing import FrozenSet, Iterable, Optional, Tuple, Union

from pip._vendor.packaging.specifiers import SpecifierSet
from pip._vendor.packaging.utils import NormalizedName, canonicalize_name
from pip._vendor.packaging.version import LegacyVersion, Version

from pip._internal.models.link import Link, links_equivalent
from pip._internal.req.req_install import InstallRequirement
from pip._internal.utils.hashes import Hashes

CandidateLookup = Tuple[Optional["Candidate"], Optional[InstallRequirement]]
CandidateVersion = Union[LegacyVersion, Version]


def format_name(project, extras):
    # type: (str, FrozenSet[str]) -> str
    if not extras:
        return project
    canonical_extras = sorted(canonicalize_name(e) for e in extras)
    return "{}[{}]".format(project, ",".join(canonical_extras))


class Constraint:
    def __init__(self, specifier, hashes, links):
        # type: (SpecifierSet, Hashes, FrozenSet[Link]) -> None
        self.specifier = specifier
        self.hashes = hashes
        self.links = links

    @classmethod
    def empty(cls):
        # type: () -> Constraint
        return Constraint(SpecifierSet(), Hashes(), frozenset())

    @classmethod
    def from_ireq(cls, ireq):
        # type: (InstallRequirement) -> Constraint
        links = frozenset([ireq.link]) if ireq.link else frozenset()
        return Constraint(ireq.specifier, ireq.hashes(trust_internet=False), links)

    def __nonzero__(self):
        # type: () -> bool
        return bool(self.specifier) or bool(self.hashes) or bool(self.links)

    def __bool__(self):
        # type: () -> bool
        return self.__nonzero__()

    def __and__(self, other):
        # type: (InstallRequirement) -> Constraint
        if not isinstance(other, InstallRequirement):
            return NotImplemented
        specifier = self.specifier & other.specifier
        hashes = self.hashes & other.hashes(trust_internet=False)
        links = self.links
        if other.link:
            links = links.union([other.link])
        return Constraint(specifier, hashes, links)

    def is_satisfied_by(self, candidate):
        # type: (Candidate) -> bool
        # Reject if there are any mismatched URL constraints on this package.
        if self.links and not all(_match_link(link, candidate) for link in self.links):
            return False
        # We can safely always allow prereleases here since PackageFinder
        # already implements the prerelease logic, and would have filtered out
        # prerelease candidates if the user does not expect them.
        return self.specifier.contains(candidate.version, prereleases=True)


class Requirement:
    @property
    def project_name(self):
        # type: () -> NormalizedName
        """The "project name" of a requirement.

        This is different from ``name`` if this requirement contains extras,
        in which case ``name`` would contain the ``[...]`` part, while this
        refers to the name of the project.
        """
        raise NotImplementedError("Subclass should override")

    @property
    def name(self):
        # type: () -> str
        """The name identifying this requirement in the resolver.

        This is different from ``project_name`` if this requirement contains
        extras, where ``project_name`` would not contain the ``[...]`` part.
        """
        raise NotImplementedError("Subclass should override")

    def is_satisfied_by(self, candidate):
        # type: (Candidate) -> bool
        return False

    def get_candidate_lookup(self):
        # type: () -> CandidateLookup
        raise NotImplementedError("Subclass should override")

    def format_for_error(self):
        # type: () -> str
        raise NotImplementedError("Subclass should override")


def _match_link(link, candidate):
    # type: (Link, Candidate) -> bool
    if candidate.source_link:
        return links_equivalent(link, candidate.source_link)
    return False


class Candidate:
    @property
    def project_name(self):
        # type: () -> NormalizedName
        """The "project name" of the candidate.

        This is different from ``name`` if this candidate contains extras,
        in which case ``name`` would contain the ``[...]`` part, while this
        refers to the name of the project.
        """
        raise NotImplementedError("Override in subclass")

    @property
    def name(self):
        # type: () -> str
        """The name identifying this candidate in the resolver.

        This is different from ``project_name`` if this candidate contains
        extras, where ``project_name`` would not contain the ``[...]`` part.
        """
        raise NotImplementedError("Override in subclass")

    @property
    def version(self):
        # type: () -> CandidateVersion
        raise NotImplementedError("Override in subclass")

    @property
    def is_installed(self):
        # type: () -> bool
        raise NotImplementedError("Override in subclass")

    @property
    def is_editable(self):
        # type: () -> bool
        raise NotImplementedError("Override in subclass")

    @property
    def source_link(self):
        # type: () -> Optional[Link]
        raise NotImplementedError("Override in subclass")

    def iter_dependencies(self, with_requires):
        # type: (bool) -> Iterable[Optional[Requirement]]
        raise NotImplementedError("Override in subclass")

    def get_install_requirement(self):
        # type: () -> Optional[InstallRequirement]
        raise NotImplementedError("Override in subclass")

    def format_for_error(self):
        # type: () -> str
        raise NotImplementedError("Subclass should override")
