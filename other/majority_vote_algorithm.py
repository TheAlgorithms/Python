import collections

"""
This is Booyer-Moore Majority Vote Algorithm. The problem statement goes like:
Given an integer array of size n, find all elements that appear more than ⌊ n/k ⌋ times.
We have to solve in O(n) time and O(1) Space.
URL : https://en.wikipedia.org/wiki/Boyer%E2%80%93Moore_majority_vote_algorithm
"""

def majority_element(total_votes: list[int], max_candidates: int) -> list[int]:
    """
    >>> majority_element([1, 2, 2, 3, 1, 3, 2],3)
    [2]
    """
    majority_candidate_counter = collections.Counter()
    for vote in total_votes:
        majority_candidate_counter[vote] += 1
        if len(majority_candidate_counter) == max_candidates:
            majority_candidate_counter -= collections.Counter(
                set(majority_candidate_counter)
            )
    majority_candidate_counter = collections.Counter(
        vote for vote in total_votes if vote in majority_candidate_counter
    )
    return [
        vote
        for vote in majority_candidate_counter
        if majority_candidate_counter[vote] > len(total_votes) / max_candidates
    ]


if __name__ == "__main__":
    import doctest

    doctest.testmod()
