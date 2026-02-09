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
        >>> gs.find_matches({1: [1, 2, 3], 2: [2, 1, 3], 3: [2, 3, 1]}, {1: [1, 2, 3], 2: [2, 1, 3], 3: [2, 3, 1]})
        {1: 1, 2: 2, 3: 3}
        >>> gs.find_matches({}, {})
        {}
        >>> gs.find_matches({1: [1,]}, {1: [1,]})
        {1: 1}
        """

        matches = {key: -1 for key in proposers_preferences.keys()}

        # [NOTE] I would've used sets, but want replicability for easy debugging.
        free_proposers = list(proposers_preferences.keys())
        tested_matches = {key: 0 for key in proposers_preferences.keys()}

        while free_proposers:
            proposer = free_proposers[0]

            if tested_matches[proposer] == len(proposers_preferences[proposer]):
                free_proposers.remove(proposer)
                continue

            receiver = proposers_preferences[proposer][tested_matches[proposer]]
            tested_matches[proposer] += 1

            if receiver not in matches.values():
                matches[proposer] = receiver
                free_proposers.remove(proposer)
                continue
            cur_proposer = next(
                prop for prop, rec in matches.items() if rec == receiver
            )
            if receivers_preferences[receiver].index(proposer) < receivers_preferences[
                receiver
            ].index(cur_proposer):
                matches[cur_proposer] = -1
                matches[proposer] = receiver
                free_proposers.remove(proposer)
                free_proposers.append(cur_proposer)

        return matches


if __name__ == "__main__":
    import doctest

    doctest.testmod()
