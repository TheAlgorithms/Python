"""
In the Tower of Hanoi problem, we are given three rods and a number of disks of different sizes, which can slide onto any rod. The puzzle starts with the disks in a neat stack in ascending order of size on one rod, the smallest at the top, thus making a conical shape.
The objective of the puzzle is to move the entire stack to another rod, obeying the following simple rules:

    1. Only one disk can be moved at a time.
    2. Each move consists of taking the upper disk from one of the stacks and placing it on top of another stack or on an empty rod.
    3. No disk may be placed on top of a smaller disk.

The goal is to move all the disks from the source rod to the destination rod, using the auxiliary rod if needed.

Time complexity: O(2^n)  // where n is the number of disks

Constraints:
1 <= number of disks <= 20
"""


def move_disk(n, source_rod, destination_rod):
    """
    Helper function to print a single move.

    >>> move_disk(1, 'A', 'B')
    Move disk 1 from A to B
    """
    print(f"Move disk {n} from {source_rod} to {destination_rod}")


def tower_of_hanoi(n, source_rod, destination_rod, auxiliary_rod):
    """
    Solve the Tower of Hanoi problem.

    Parameters:
    - n: Number of disks
    - source_rod: The rod from which to move the disks
    - destination_rod: The rod to which to move the disks
    - auxiliary_rod: The auxiliary rod for intermediate moves

    >>> tower_of_hanoi(1, 'A', 'C', 'B')
    Move disk 1 from A to C

    >>> tower_of_hanoi(2, 'A', 'C', 'B')
    Move disk 1 from A to B
    Move disk 2 from A to C
    Move disk 1 from B to C

    >>> tower_of_hanoi(3, 'A', 'C', 'B')
    Move disk 1 from A to C
    Move disk 2 from A to B
    Move disk 1 from C to B
    Move disk 3 from A to C
    Move disk 1 from B to A
    Move disk 2 from B to C
    Move disk 1 from A to C
    """
    if n == 1:
        move_disk(1, source_rod, destination_rod)
        return
    tower_of_hanoi(n - 1, source_rod, auxiliary_rod, destination_rod)
    move_disk(n, source_rod, destination_rod)
    tower_of_hanoi(n - 1, auxiliary_rod, destination_rod, source_rod)


def main():
    tower_of_hanoi(3, "A", "C", "B")


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    main()
