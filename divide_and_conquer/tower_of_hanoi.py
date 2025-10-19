"""
Towers of Hanoi is a mathematical puzzle that is solved using a recursive
divide-and-conquer strategy.

It moves a stack of disks from a source pole to a destination pole,
using an auxiliary pole, subject to these rules:
1. Only one disk can be moved at a time.
2. Each move consists of taking the upper disk from one stack and
   placing it on top of another stack or an empty pole.
3. No disk may be placed on top of a smaller disk.

More information:
https://en.wikipedia.org/wiki/Tower_of_Hanoi
"""


def tower_of_hanoi(
    n: int, source: str = "A", auxiliary: str = "B", destination: str = "C"
) -> list[tuple[str, str]]:
    """
    Pure python implementation of the Towers of Hanoi puzzle (recursive version),
    returning the sequence of moves required to solve the puzzle.

    >>> tower_of_hanoi(1)
    [('A', 'C')]
    >>> tower_of_hanoi(2)
    [('A', 'B'), ('A', 'C'), ('B', 'C')]
    >>> tower_of_hanoi(3)
    [('A', 'C'), ('A', 'B'), ('C', 'B'), ('A', 'C'), ('B', 'A'), ('B', 'C'), ('A', 'C')]
    >>> tower_of_hanoi(0)
    []
    """
    moves = []

    def solve_hanoi(n: int, source: str, auxiliary: str, destination: str):
        """Recursive helper function to generate the moves."""
        if n == 0:
            return

        # 1. Move n-1 disks from Source to Auxiliary, using Destination as auxiliary.
        # This is the "Divide" step.
        solve_hanoi(n - 1, source, destination, auxiliary)

        # 2. Move the largest disk (n) from Source to Destination.
        # This is the "Conquer" step (base step of the recursion).
        moves.append((source, destination))

        # 3. Move n-1 disks from Auxiliary to Destination, using Source as auxiliary.
        # This is the "Combine" step.
        solve_hanoi(n - 1, auxiliary, source, destination)

    solve_hanoi(n, source, auxiliary, destination)
    return moves


if __name__ == "__main__":
    try:
        n_disks = int(
            input("Enter the number of disks for the Tower of Hanoi: ").strip()
        )
        if n_disks < 0:
            print("Please enter a non-negative number of disks.")
        else:
            all_moves = tower_of_hanoi(n_disks)
            print(f"\nTotal moves required: {len(all_moves)}")
            print("Sequence of Moves (Source -> Destination):")
            for move in all_moves:
                print(f"Move disk from {move[0]} to {move[1]}")
    except ValueError:
        print("Invalid input. Please enter an integer.")
