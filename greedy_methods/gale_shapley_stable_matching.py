"""
Gale-Shapley Stable Matching (Hospital-Proposing Version)

wikipedia: https://en.wikipedia.org/wiki/Gale%E2%80%93Shapley_algorithm

This function implements the Gale-Shapley algorithm to produce a stable
matching between two groups: hospitals and students. Each hospital ranks
students in order of preference, and each student ranks hospitals.

A matching is considered stable if there is no hospital-student pair who
would both prefer to be matched with each other over their current assignment

Algorithm overview:
1. Start with all hospitals and students unmatched.
2. While there exists an unmatched hospital that still has students left
   to propose to:
   a. The hospital proposes to the highest-ranked student on its preference
      list that it has not yet proposed to.
   b. If the student is unmatched, they tentatively accept the proposal.
   c. If the student is already matched, they compare their current match
      with the new hospital and keep the one they prefer more, rejecting
      the other.
3. Rejected hospitals continue proposing down their lists.
4. The process ends when all hospitals are matched or have exhausted their
   preference lists.

Properties:
- The algorithm always terminates with a stable matching.
- The result is optimal for the proposing side (hospitals): each hospital
  receives the best student it could obtain in any stable matching.
- If students propose instead, the result becomes student-optimal.
"""


class GaleShapley:
    """Implementation of the Gale-Shapley algorithem

    takes it 2 preference list as a 2D array of ints. First one is the
    proposing side.
    """

    def find_matches(
        self,
        proposers_preferences: dict[int, list[int]],
        receivers_preferences: dict[int, list[int]],
    ) -> dict[int, int]:
        """
        >>> gs = GaleShapley()
        >>> gs.find_matches(
        ... {1: [1, 2, 3], 2: [2, 1, 3], 3: [2, 3, 1]},
        ... {1: [1, 2, 3], 2: [2, 1, 3], 3: [2, 3, 1]})
        {1: 1, 2: 2, 3: 3}
        >>> gs.find_matches({}, {})
        {}
        >>> gs.find_matches(
        ... {1: [1,]},
        ... {1: [1,]})
        {1: 1}
        >>> gs.find_matches(
        ... {1: [1, 2, 3, 4], 2: [1, 2, 3, 4], 3: [1, 2, 3, 4], 4: [1, 2, 3, 4]},
        ... {1: [4, 3, 2, 1], 2: [1, 2, 3, 4], 3: [2, 3, 4, 1], 4: [3, 4, 1, 2]})
        {1: 2, 2: 3, 3: 4, 4: 1}
        >>> gs.find_matches(
        ... {1: [2, 3, 4, 5, 6, 1], 2: [2, 4, 5, 6, 1, 3], 3: [4, 5, 6, 1, 2, 3],
        ...     4: [5, 6, 1, 2, 3, 4], 5: [2, 1, 6, 3, 4, 5], 6: [1, 2, 3, 4, 5, 6]},
        ... {1: [6, 1, 2, 3, 4, 5], 2: [1, 2, 3, 4, 5, 6], 3: [2, 3, 4, 5, 6, 1],
        ...     4: [3, 4, 5, 6, 1, 2], 5: [4, 5, 6, 1, 2, 3], 6: [5, 6, 1, 2, 3, 4]})
        {1: 2, 2: 3, 3: 4, 4: 5, 5: 6, 6: 1}
        """

        matches = dict.fromkeys(proposers_preferences.keys(), -1)
        tested_matches = dict.fromkeys(proposers_preferences.keys(), 0)
        free_proposers = list(proposers_preferences.keys())

        while free_proposers:
            proposer = free_proposers[0]

            # continue if all options for proposer have been exhausted
            if tested_matches[proposer] == len(proposers_preferences[proposer]):
                free_proposers.remove(proposer)
                continue

            receiver = proposers_preferences[proposer][tested_matches[proposer]]
            tested_matches[proposer] += 1

            # set receiver as match if not previously matched
            if receiver not in matches.values():
                matches[proposer] = receiver
                free_proposers.remove(proposer)
                continue
            cur_proposer = next(
                prop for prop, rec in matches.items() if rec == receiver
            )

            # give receiver new proposer match only if it preferes new over old
            if receivers_preferences[receiver].index(proposer) < receivers_preferences[
                receiver
            ].index(cur_proposer):
                free_proposers.remove(proposer)
                free_proposers.append(cur_proposer)
                matches[cur_proposer] = -1
                matches[proposer] = receiver

        return matches


if __name__ == "__main__":
    import doctest

    doctest.testmod()
