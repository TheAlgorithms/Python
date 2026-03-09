"""
The Josephus problem is a famous theoretical problem related to a certain
counting-out game. This module provides functions to solve the Josephus problem
for num_people and a step_size.

The Josephus problem is defined as follows:
- num_people are standing in a circle.
- Starting with a specified person, you count around the circle,
  skipping a fixed number of people (step_size).
- The person at which you stop counting is eliminated from the circle.
- The counting continues until only one person remains.

For more information about the Josephus problem, refer to:
https://en.wikipedia.org/wiki/Josephus_problem
"""


def josephus_recursive(num_people: int, step_size: int) -> int:
    """
    Solve the Josephus problem for num_people and a step_size recursively.

    Args:
        num_people: A positive integer representing the number of people.
        step_size: A positive integer representing the step size for elimination.

    Returns:
        The position of the last person remaining.

    Raises:
        ValueError: If num_people or step_size is not a positive integer.

    Examples:
        >>> josephus_recursive(7, 3)
        3
        >>> josephus_recursive(10, 2)
        4
        >>> josephus_recursive(0, 2)
        Traceback (most recent call last):
            ...
        ValueError: num_people or step_size is not a positive integer.
        >>> josephus_recursive(1.9, 2)
        Traceback (most recent call last):
            ...
        ValueError: num_people or step_size is not a positive integer.
        >>> josephus_recursive(-2, 2)
        Traceback (most recent call last):
            ...
        ValueError: num_people or step_size is not a positive integer.
        >>> josephus_recursive(7, 0)
        Traceback (most recent call last):
            ...
        ValueError: num_people or step_size is not a positive integer.
        >>> josephus_recursive(7, -2)
        Traceback (most recent call last):
            ...
        ValueError: num_people or step_size is not a positive integer.
        >>> josephus_recursive(1_000, 0.01)
        Traceback (most recent call last):
            ...
        ValueError: num_people or step_size is not a positive integer.
        >>> josephus_recursive("cat", "dog")
        Traceback (most recent call last):
            ...
        ValueError: num_people or step_size is not a positive integer.
    """
    if (
        not isinstance(num_people, int)
        or not isinstance(step_size, int)
        or num_people <= 0
        or step_size <= 0
    ):
        raise ValueError("num_people or step_size is not a positive integer.")

    if num_people == 1:
        return 0

    return (josephus_recursive(num_people - 1, step_size) + step_size) % num_people


def find_winner(num_people: int, step_size: int) -> int:
    """
    Find the winner of the Josephus problem for num_people and a step_size.

    Args:
        num_people (int): Number of people.
        step_size (int): Step size for elimination.

    Returns:
        int: The position of the last person remaining (1-based index).

    Examples:
        >>> find_winner(7, 3)
        4
        >>> find_winner(10, 2)
        5
    """
    return josephus_recursive(num_people, step_size) + 1


def josephus_iterative(num_people: int, step_size: int) -> int:
    """
    Solve the Josephus problem for num_people and a step_size iteratively.

    Args:
        num_people (int): The number of people in the circle.
        step_size (int): The number of steps to take before eliminating someone.

    Returns:
        int: The position of the last person standing.

    Examples:
        >>> josephus_iterative(5, 2)
        3
        >>> josephus_iterative(7, 3)
        4
    """
    circle = list(range(1, num_people + 1))
    current = 0

    while len(circle) > 1:
        current = (current + step_size - 1) % len(circle)
        circle.pop(current)

    return circle[0]


if __name__ == "__main__":
    import doctest

    doctest.testmod()
