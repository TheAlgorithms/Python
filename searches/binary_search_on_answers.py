from typing import Callable


def binary_search_on_answer(
    low: int, high: int, condition: Callable[[int], bool]
) -> int:
    """
    Generic Binary Search on Answer template.

    Finds the minimum value in the range [low, high] that satisfies the condition.

    The condition function must be monotonic:
    - False False False True True True

    :param low: lower bound of search space
    :param high: upper bound of search space
    :param condition: function that returns True if mid is a valid answer

    :return: smallest value that satisfies the condition

    Examples:
    >>> def condition(x): return x * x >= 16
    >>> binary_search_on_answer(0, 10, condition)
    4

    >>> def condition(x): return x >= 7
    >>> binary_search_on_answer(0, 10, condition)
    7
    """
    answer = high

    while low <= high:
        mid = low + (high - low) // 2

        if condition(mid):
            answer = mid
            high = mid - 1
        else:
            low = mid + 1

    return answer


# Example1: minimum capacity to ship

def min_capacity_to_ship(weights: list[int], days: int) -> int:
    """
    Find minimum capacity to ship packages within given days.

    >>> min_capacity_to_ship([1,2,3,4,5,6,7,8,9,10], 5)
    15
    """

    def can_ship(capacity: int) -> bool:
        days_used = 1
        current = 0

        for weight in weights:
            if current + weight > capacity:
                days_used += 1
                current = 0
            current += weight

        return days_used <= days

    return binary_search_on_answer(max(weights), sum(weights), can_ship)