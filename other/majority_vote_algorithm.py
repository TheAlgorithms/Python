"""
This is Booyer-Moore Majority Vote Algorithm. The problem statement goes like this:
Given an integer array of size n, find all elements that appear more than ⌊ n/k ⌋ times.
We have to solve in O(n) time and O(1) Space.
URL : https://en.wikipedia.org/wiki/Boyer%E2%80%93Moore_majority_vote_algorithm
"""
from collections import Counter


def majority_vote(votes: list[int], votes_needed_to_win: int) -> list[int]:
    """
    >>> majority_vote([1, 2, 2, 3, 1, 3, 2], 3)
    [2]
    >>> majority_vote([1, 2, 2, 3, 1, 3, 2], 2)
    []
    >>> majority_vote([1, 2, 2, 3, 1, 3, 2], 4)
    [1, 2, 3]
    """
    majority_candidate_counter: Counter[int] = Counter()
    for vote in votes:
        majority_candidate_counter[vote] += 1
        if len(majority_candidate_counter) == votes_needed_to_win:
            majority_candidate_counter -= Counter(set(majority_candidate_counter))
    majority_candidate_counter = Counter(
        vote for vote in votes if vote in majority_candidate_counter
    )
    return [
        vote
        for vote in majority_candidate_counter
        if majority_candidate_counter[vote] > len(votes) / votes_needed_to_win
    ]


if __name__ == "__main__":
    import doctest

    doctest.testmod()
