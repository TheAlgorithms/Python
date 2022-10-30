"""
Implementation of an algorithm to solve the Tower of Hanoi Problem.

The problem involves three poles, with a number of disks on one
https://en.wikipedia.org/wiki/Tower_of_Hanoi
"""


def move_tower(height, from_pole, to_pole, with_pole):
    """
    Recursive algorithm to move a tower with `height` number of
    disks from `from_pole` to `to_pole`, using `with_pole` for
    intermediate steps.

    :param height: The number of disks in the tower.

    :param from_pole: The starting pole with all the disks.

    :param to_pole: The pole for the final position of all disks.

    :param with_pole: A spare pole to use for intermediate steps.

    >>> move_tower(3, 'A', 'B', 'C')
    moving disk from A to B
    moving disk from A to C
    moving disk from B to C
    moving disk from A to B
    moving disk from C to A
    moving disk from C to B
    moving disk from A to B
    """
    if height >= 1:
        move_tower(height - 1, from_pole, with_pole, to_pole)
        move_disk(from_pole, to_pole)
        move_tower(height - 1, with_pole, to_pole, from_pole)


def move_disk(fp, tp):
    """
    Prints that a disk has been moved from fp to tp

    :param fp: from-pole - The starting position of the disk.

    :param tp: to-pole - The ending position of the disk.
    """
    print("moving disk from", fp, "to", tp)


def main():
    height = int(input("Height of hanoi: ").strip())
    move_tower(height, "A", "B", "C")


if __name__ == "__main__":
    main()
