#!/usr/bin/env python3


def climb_stairs(number_of_steps: int) -> int:
    """
    Calculate the number of distinct ways to climb a staircase with a given number of steps.

    This problem is from LeetCode No. 70: Climbing Stairs.

    Args:
        number_of_steps (int): The number of steps on the staircase.

    Returns:
        int: The number of distinct ways to climb the staircase.

    Raises:
        AssertionError: If number_of_steps is not a positive integer.

    Example:
        >>> climb_stairs(3)
        3
        >>> climb_stairs(1)
        1
        >>> climb_stairs(-7)  # doctest: +ELLIPSIS
        Traceback (most recent call last):
            ...
        AssertionError: number_of_steps needs to be a positive integer, your input: -7
    """
    assert (
        isinstance(number_of_steps, int) and number_of_steps > 0
    ), f"number_of_steps needs to be a positive integer, your input: {number_of_steps}"

    if number_of_steps == 1:
        return 1

    previous, current = 1, 1
    for _ in range(number_of_steps - 1):
        current, previous = current + previous, current

    return current


if __name__ == "__main__":
    import doctest

    doctest.testmod()
