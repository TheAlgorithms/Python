from typing import List, Tuple, Dict


def get_best_match(
        group1: Dict[object, List],
        group2: Dict[object, List]) -> List[Tuple]:
    """
    Match elements from group1 and group2 based on their preferences, such that there are
    no rogue couples (Two elements such that they have a higher preference for each other
    than the element they have been matched with)

    This algorithm comes from the MITOCW lecture from the course 6.042 by Prof. Tom Leighton
    The algorithm discussed with an example:
    https://youtu.be/5RSMLgy06Ew?list=PL6MpDZWD2gTF3mz26HSufmsIO-COKKb5j&t=1623


    :param group1: Preferences of elements of group1 as a dict of the form
    {<group1_elemt>: [...<List of group2_elemts in descending order of preference>]}
    :param group2: Preferences of elements of group2 as a dict of the form
    {<group2_elemt>: [...<List of group1_elemts in descending order of preference>]}
    """
    group1_checklist = dict(zip(group1.keys(), list(group1.values()).copy()))
    group2_possible_matches = dict(zip(group2.keys(), [[]] * 5))

    def best_match_found():
        """
        Best match corresponds to the case where each element in group2
        has exactly ONE possible match
        """
        return all([
            len(possible_matches) == 1
            for possible_matches in group2_possible_matches.values()])

    def perform_matching():
        """
        Performs one round of matching elements in group 1 to group 2
        1. All group 1 elements try to match with their remaining best top preference in group 2
        2. group 2 elements then keep only their top preference out of the possible matches from
        group 1 (from step 1) and reject the remaining elements from group 1
        3. The rejected elements cross out the group 2 element that rejected them, from their
        checklist.
        4. We go back to step 1 and continue till each element in group 2 has exactly ONE matching
        element in group 1

        Then we return the match as a list of tuples in the form [(group2_elemt, group1_elemt), ...]
        """
        # Each group1 element tries to match with their avaialable top match in group2
        for group1_element, checklist in group1_checklist.items():
            group2_possible_matches[checklist[0]] = list(
                set(group2_possible_matches[checklist[0]] + [group1_element]))

        if best_match_found():
            # Format the group2_possible_matches according to the requirement in doc comment
            return list(zip(
                group2_possible_matches.keys(),
                list(map(
                    lambda possible_matches: possible_matches[0],
                    group2_possible_matches.values()))
            ))
            # return group2_possible_matches
        else:
            for group2_element in group2_possible_matches:
                # Sort possible matches for each element in group2
                # according to their preference
                group2_possible_matches[group2_element].sort(
                    key=lambda possible_match: group2[group2_element].index(possible_match))
                # Only top match retained, rest all rejected
                rejected_group1 = group2_possible_matches[group2_element][1:]
                group2_possible_matches[group2_element] = group2_possible_matches[group2_element][:1]
                # Rejected group1 elements cross out the group2 element from their list
                for group1_element in rejected_group1:
                    # Index 0 is popped as the element tried to match with its top available choice
                    group1_checklist[group1_element].pop(0)
            return perform_matching()

    return perform_matching()


def main():
    '''
    group1 = boys and group2 = girls
    The preference order of every boy and girl is taken
    from the video lecture referred to in the doc comment
    of get_best_match()
    '''
    boys = {
        1: ['C', 'B', 'E', 'A', 'D'],
        2: ['A', 'B', 'E', 'C', 'D'],
        3: ['D', 'C', 'B', 'A', 'E'],
        4: ['A', 'C', 'D', 'B', 'E'],
        5: ['A', 'B', 'D', 'E', 'C']
    }

    girls = {
        'A': [3, 5, 2, 1, 4],
        'B': [5, 2, 1, 4, 3],
        'C': [4, 3, 5, 1, 2],
        'D': [1, 2, 3, 4, 5],
        'E': [2, 3, 4, 1, 5]
    }
    print(get_best_match(boys, girls))


if __name__ == '__main__':
    main()
