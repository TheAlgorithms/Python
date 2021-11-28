from typing import TYPE_CHECKING, Dict, Iterable, Iterator, Mapping, Sequence, Union

from pip._vendor.resolvelib.providers import AbstractProvider

from .base import Candidate, Constraint, Requirement
from .factory import Factory

if TYPE_CHECKING:
    from pip._vendor.resolvelib.providers import Preference
    from pip._vendor.resolvelib.resolvers import RequirementInformation

    PreferenceInformation = RequirementInformation[Requirement, Candidate]

    _ProviderBase = AbstractProvider[Requirement, Candidate, str]
else:
    _ProviderBase = AbstractProvider

# Notes on the relationship between the provider, the factory, and the
# candidate and requirement classes.
#
# The provider is a direct implementation of the resolvelib class. Its role
# is to deliver the API that resolvelib expects.
#
# Rather than work with completely abstract "requirement" and "candidate"
# concepts as resolvelib does, pip has concrete classes implementing these two
# ideas. The API of Requirement and Candidate objects are defined in the base
# classes, but essentially map fairly directly to the equivalent provider
# methods. In particular, `find_matches` and `is_satisfied_by` are
# requirement methods, and `get_dependencies` is a candidate method.
#
# The factory is the interface to pip's internal mechanisms. It is stateless,
# and is created by the resolver and held as a property of the provider. It is
# responsible for creating Requirement and Candidate objects, and provides
# services to those objects (access to pip's finder and preparer).


class PipProvider(_ProviderBase):
    """Pip's provider implementation for resolvelib.

    :params constraints: A mapping of constraints specified by the user. Keys
        are canonicalized project names.
    :params ignore_dependencies: Whether the user specified ``--no-deps``.
    :params upgrade_strategy: The user-specified upgrade strategy.
    :params user_requested: A set of canonicalized package names that the user
        supplied for pip to install/upgrade.
    """

    def __init__(
        self,
        factory,  # type: Factory
        constraints,  # type: Dict[str, Constraint]
        ignore_dependencies,  # type: bool
        upgrade_strategy,  # type: str
        user_requested,  # type: Dict[str, int]
    ):
        # type: (...) -> None
        self._factory = factory
        self._constraints = constraints
        self._ignore_dependencies = ignore_dependencies
        self._upgrade_strategy = upgrade_strategy
        self._user_requested = user_requested

    def identify(self, requirement_or_candidate):
        # type: (Union[Requirement, Candidate]) -> str
        return requirement_or_candidate.name

    def get_preference(
        self,
        identifier: str,
        resolutions: Mapping[str, Candidate],
        candidates: Mapping[str, Iterator[Candidate]],
        information: Mapping[str, Iterator["PreferenceInformation"]],
    ) -> "Preference":
        """Produce a sort key for given requirement based on preference.

        The lower the return value is, the more preferred this group of
        arguments is.

        Currently pip considers the followings in order:

        * Prefer if any of the known requirements points to an explicit URL.
        * If equal, prefer if any requirements contain ``===`` and ``==``.
        * If equal, prefer if requirements include version constraints, e.g.
          ``>=`` and ``<``.
        * If equal, prefer user-specified (non-transitive) requirements, and
          order user-specified requirements by the order they are specified.
        * If equal, order alphabetically for consistency (helps debuggability).
        """

        def _get_restrictive_rating(requirements):
            # type: (Iterable[Requirement]) -> int
            """Rate how restrictive a set of requirements are.

            ``Requirement.get_candidate_lookup()`` returns a 2-tuple for
            lookup. The first element is ``Optional[Candidate]`` and the
            second ``Optional[InstallRequirement]``.

            * If the requirement is an explicit one, the explicitly-required
              candidate is returned as the first element.
            * If the requirement is based on a PEP 508 specifier, the backing
              ``InstallRequirement`` is returned as the second element.

            We use the first element to check whether there is an explicit
            requirement, and the second for equality operator.
            """
            lookups = (r.get_candidate_lookup() for r in requirements)
            cands, ireqs = zip(*lookups)
            if any(cand is not None for cand in cands):
                return 0
            spec_sets = (ireq.specifier for ireq in ireqs if ireq)
            operators = [
                specifier.operator for spec_set in spec_sets for specifier in spec_set
            ]
            if any(op in ("==", "===") for op in operators):
                return 1
            if operators:
                return 2
            # A "bare" requirement without any version requirements.
            return 3

        rating = _get_restrictive_rating(r for r, _ in information[identifier])
        order = self._user_requested.get(identifier, float("inf"))

        # HACK: Setuptools have a very long and solid backward compatibility
        # track record, and extremely few projects would request a narrow,
        # non-recent version range of it since that would break a lot things.
        # (Most projects specify it only to request for an installer feature,
        # which does not work, but that's another topic.) Intentionally
        # delaying Setuptools helps reduce branches the resolver has to check.
        # This serves as a temporary fix for issues like "apache-airlfow[all]"
        # while we work on "proper" branch pruning techniques.
        delay_this = identifier == "setuptools"

        return (delay_this, rating, order, identifier)

    def find_matches(
        self,
        identifier: str,
        requirements: Mapping[str, Iterator[Requirement]],
        incompatibilities: Mapping[str, Iterator[Candidate]],
    ) -> Iterable[Candidate]:
        def _eligible_for_upgrade(name):
            # type: (str) -> bool
            """Are upgrades allowed for this project?

            This checks the upgrade strategy, and whether the project was one
            that the user specified in the command line, in order to decide
            whether we should upgrade if there's a newer version available.

            (Note that we don't need access to the `--upgrade` flag, because
            an upgrade strategy of "to-satisfy-only" means that `--upgrade`
            was not specified).
            """
            if self._upgrade_strategy == "eager":
                return True
            elif self._upgrade_strategy == "only-if-needed":
                return name in self._user_requested
            return False

        return self._factory.find_candidates(
            identifier=identifier,
            requirements=requirements,
            constraint=self._constraints.get(identifier, Constraint.empty()),
            prefers_installed=(not _eligible_for_upgrade(identifier)),
            incompatibilities=incompatibilities,
        )

    def is_satisfied_by(self, requirement, candidate):
        # type: (Requirement, Candidate) -> bool
        return requirement.is_satisfied_by(candidate)

    def get_dependencies(self, candidate):
        # type: (Candidate) -> Sequence[Requirement]
        with_requires = not self._ignore_dependencies
        return [r for r in candidate.iter_dependencies(with_requires) if r is not None]
