"""
Starting in the top left corner of a 2×2 grid, and only being able to move to
the right and down, there are exactly 6 routes to the bottom right corner.
How many such routes are there through a 20×20 grid?
"""
from math import factorial


def lattice_paths(n):
    """
        Returns the number of paths possible in a n x n grid starting at top left
        corner going to bottom right corner and being able to move right and down
        only.

    bruno@bruno-laptop:~/git/Python/project_euler/problem_15$ python3 sol1.py 50
    1.008913445455642e+29
    bruno@bruno-laptop:~/git/Python/project_euler/problem_15$ python3 sol1.py 25
    126410606437752.0
    bruno@bruno-laptop:~/git/Python/project_euler/problem_15$ python3 sol1.py 23
    8233430727600.0
    bruno@bruno-laptop:~/git/Python/project_euler/problem_15$ python3 sol1.py 15
    155117520.0
    bruno@bruno-laptop:~/git/Python/project_euler/problem_15$ python3 sol1.py 1
    2.0

        >>> lattice_paths(25)
        126410606437752
        >>> lattice_paths(23)
        8233430727600
        >>> lattice_paths(20)
        137846528820
        >>> lattice_paths(15)
        155117520
        >>> lattice_paths(1)
        2

    """
    n = 2 * n  # middle entry of odd rows starting at row 3 is the solution for n = 1,
    # 2, 3,...
    k = n / 2

    return int(factorial(n) / (factorial(k) * factorial(n - k)))


if __name__ == "__main__":
    import sys

    if len(sys.argv) == 1:
        print(lattice_paths(20))
    else:
        try:
            n = int(sys.argv[1])
            print(lattice_paths(n))
        except ValueError:
            print("Invalid entry - please enter a number.")
