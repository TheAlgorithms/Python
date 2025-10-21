<<<<<<< HEAD
def a_very_big_sum(arr: list[int]) -> int:
=======
from typing import List


def a_very_big_sum(arr: List[int]) -> int:
>>>>>>> 2e5b8980304014f131c23d43a7a08e624c23de8b
    """
    Return the sum of all integers in the input array.

    >>> a_very_big_sum([2, 4, 6])
    12
    >>> a_very_big_sum([])
    0
    """
    total = 0
    for i in arr:
        total += i
    return total

if __name__ == "__main__":
    # Example usage
    arr = [2, 4, 6, 2, 4, 6, 3]
    result = a_very_big_sum(arr)
    print(f"Sum of {arr} is {result}")
