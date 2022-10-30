#!/usr/bin/env python3


def climb_stairs(number_of_steps: int) -> int:
    """
    LeetCdoe No.70: Climbing Stairs
    Distinct ways to climb a number_of_steps staircase where each time you can either
    climb 1 or 2 steps.

    Args:
        number_of_steps: number of steps on the staircase

    Returns:
        Distinct ways to climb a number_of_steps staircase

    Raises:
        AssertionError: number_of_steps not positive integer

    >>> climb_stairs(3)
    3
    >>> climb_stairs(1)
    1
    >>> climb_stairs(-7)  # doctest: +ELLIPSIS
    Traceback (most recent call last):
        ...
    AssertionError: number_of_steps needs to be positive integer, your input -7
    """
    assert (
        isinstance(number_of_steps, int) and number_of_steps > 0
    ), f"number_of_steps needs to be positive integer, your input {number_of_steps}"
    if number_of_steps == 1:
        return 1
    previous, current = 1, 1
    for _ in range(number_of_steps - 1):
        current, previous = current + previous, current
    return current


if __name__ == "__main__":
    import doctest

    doctest.testmod()
