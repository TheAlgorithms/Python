from pip._vendor.packaging.specifiers import SpecifierSet
from pip._vendor.packaging.utils import NormalizedName, canonicalize_name

from pip._internal.req.req_install import InstallRequirement

from .base import Candidate, CandidateLookup, Requirement, format_name


class ExplicitRequirement(Requirement):
    def __init__(self, candidate):
        # type: (Candidate) -> None
        self.candidate = candidate

    def __str__(self):
        # type: () -> str
        return str(self.candidate)

    def __repr__(self):
        # type: () -> str
        return "{class_name}({candidate!r})".format(
            class_name=self.__class__.__name__,
            candidate=self.candidate,
        )

    @property
    def project_name(self):
        # type: () -> NormalizedName
        # No need to canonicalise - the candidate did this
        return self.candidate.project_name

    @property
    def name(self):
        # type: () -> str
        # No need to canonicalise - the candidate did this
        return self.candidate.name

    def format_for_error(self):
        # type: () -> str
        return self.candidate.format_for_error()

    def get_candidate_lookup(self):
        # type: () -> CandidateLookup
        return self.candidate, None

    def is_satisfied_by(self, candidate):
        # type: (Candidate) -> bool
        return candidate == self.candidate


class SpecifierRequirement(Requirement):
    def __init__(self, ireq):
        # type: (InstallRequirement) -> None
        assert ireq.link is None, "This is a link, not a specifier"
        self._ireq = ireq
        self._extras = frozenset(ireq.extras)

    def __str__(self):
        # type: () -> str
        return str(self._ireq.req)

    def __repr__(self):
        # type: () -> str
        return "{class_name}({requirement!r})".format(
            class_name=self.__class__.__name__,
            requirement=str(self._ireq.req),
        )

    @property
    def project_name(self):
        # type: () -> NormalizedName
        assert self._ireq.req, "Specifier-backed ireq is always PEP 508"
        return canonicalize_name(self._ireq.req.name)

    @property
    def name(self):
        # type: () -> str
        return format_name(self.project_name, self._extras)

    def format_for_error(self):
        # type: () -> str

        # Convert comma-separated specifiers into "A, B, ..., F and G"
        # This makes the specifier a bit more "human readable", without
        # risking a change in meaning. (Hopefully! Not all edge cases have
        # been checked)
        parts = [s.strip() for s in str(self).split(",")]
        if len(parts) == 0:
            return ""
        elif len(parts) == 1:
            return parts[0]

        return ", ".join(parts[:-1]) + " and " + parts[-1]

    def get_candidate_lookup(self):
        # type: () -> CandidateLookup
        return None, self._ireq

    def is_satisfied_by(self, candidate):
        # type: (Candidate) -> bool
        assert candidate.name == self.name, (
            f"Internal issue: Candidate is not for this requirement "
            f"{candidate.name} vs {self.name}"
        )
        # We can safely always allow prereleases here since PackageFinder
        # already implements the prerelease logic, and would have filtered out
        # prerelease candidates if the user does not expect them.
        assert self._ireq.req, "Specifier-backed ireq is always PEP 508"
        spec = self._ireq.req.specifier
        return spec.contains(candidate.version, prereleases=True)


class RequiresPythonRequirement(Requirement):
    """A requirement representing Requires-Python metadata."""

    def __init__(self, specifier, match):
        # type: (SpecifierSet, Candidate) -> None
        self.specifier = specifier
        self._candidate = match

    def __str__(self):
        # type: () -> str
        return f"Python {self.specifier}"

    def __repr__(self):
        # type: () -> str
        return "{class_name}({specifier!r})".format(
            class_name=self.__class__.__name__,
            specifier=str(self.specifier),
        )

    @property
    def project_name(self):
        # type: () -> NormalizedName
        return self._candidate.project_name

    @property
    def name(self):
        # type: () -> str
        return self._candidate.name

    def format_for_error(self):
        # type: () -> str
        return str(self)

    def get_candidate_lookup(self):
        # type: () -> CandidateLookup
        if self.specifier.contains(self._candidate.version, prereleases=True):
            return self._candidate, None
        return None, None

    def is_satisfied_by(self, candidate):
        # type: (Candidate) -> bool
        assert candidate.name == self._candidate.name, "Not Python candidate"
        # We can safely always allow prereleases here since PackageFinder
        # already implements the prerelease logic, and would have filtered out
        # prerelease candidates if the user does not expect them.
        return self.specifier.contains(candidate.version, prereleases=True)


class UnsatisfiableRequirement(Requirement):
    """A requirement that cannot be satisfied."""

    def __init__(self, name):
        # type: (NormalizedName) -> None
        self._name = name

    def __str__(self):
        # type: () -> str
        return f"{self._name} (unavailable)"

    def __repr__(self):
        # type: () -> str
        return "{class_name}({name!r})".format(
            class_name=self.__class__.__name__,
            name=str(self._name),
        )

    @property
    def project_name(self):
        # type: () -> NormalizedName
        return self._name

    @property
    def name(self):
        # type: () -> str
        return self._name

    def format_for_error(self):
        # type: () -> str
        return str(self)

    def get_candidate_lookup(self):
        # type: () -> CandidateLookup
        return None, None

    def is_satisfied_by(self, candidate):
        # type: (Candidate) -> bool
        return False
