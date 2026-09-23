"""
Elementary Cellular Automaton - Rule 30
---------------------------------------

A one-dimensional cellular automaton introduced by Stephen Wolfram.
Each cell's next state depends on its current state and its two immediate neighbors.

Reference:
    https://en.wikipedia.org/wiki/Rule_30
"""


def rule_30_step(current: list[int]) -> list[int]:
    """
    Compute the next generation of a one-dimensional cellular automaton
    following Wolfram's Rule 30.

    Each cell's next state is determined by its left, center, and right neighbors.

    Args:
        current (list[int]): The current generation as a list of 0s (dead)
            and 1s (alive).

    Returns:
        list[int]: The next generation as a list of 0s and 1s.

    Example:
        >>> rule_30_step([0, 0, 1, 0, 0])
        [0, 1, 1, 1, 0]
    """
    next_gen = []
    for i in range(len(current)):
        left = current[i - 1] if i > 0 else 0
        center = current[i]
        right = current[i + 1] if i < len(current) - 1 else 0

        # Combine neighbors into a 3-bit pattern
        pattern = (left << 2) | (center << 1) | right

        # Rule 30 binary: 00011110 (bitwise representation of 30)
        next_gen.append((30 >> pattern) & 1)

    return next_gen


def generate_rule_30(size: int = 31, generations: int = 15) -> list[list[int]]:
    """
    Generate multiple generations of Rule 30 automaton.

    Args:
        size (int): Number of cells in one generation. Default is 31.
        generations (int): Number of generations to evolve. Default is 15.

    Returns:
        list[list[int]]: A list of generations (each a list of 0s and 1s).

    Example:
        >>> len(generate_rule_30(15, 5))
        5
    """
    grid = [[0] * size for _ in range(generations)]
    grid[0][size // 2] = 1  # Start with a single live cell in the middle

    for i in range(1, generations):
        grid[i] = rule_30_step(grid[i - 1])

    return grid


if __name__ == "__main__":
    # Run an example simulation
    generations = generate_rule_30(31, 15)
    for row in generations:
        print("".join("█" if cell else " " for cell in row))
