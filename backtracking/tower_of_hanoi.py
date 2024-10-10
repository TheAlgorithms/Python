# https://en.wikipedia.org/wiki/Tower_of_Hanoi
def tower_of_hanoi(n, source, destination, auxiliary):
    """
    Solves the Tower of Hanoi problem using backtracking.

    Args:
        n: The number of disks to be moved.
        source: The index of the source peg.
        destination: The index of the destination peg.
        auxiliary: The index of the auxiliary peg.

    Returns:
        None
    """

    if n == 1:
        print(f"Move disk 1 from peg {source} to peg {destination}")
        return

    tower_of_hanoi(n - 1, source, auxiliary, destination)
    print(f"Move disk {n} from peg {source} to peg {destination}")
    tower_of_hanoi(n - 1, auxiliary, destination, source)


# Example usage:
n = 3  # Number of disks
tower_of_hanoi(n, 1, 3, 2)

# Explanation:

# tower_of_hanoi function:

# Takes four arguments:
# n: The number of disks to be moved.
# source: The index of the source peg.
# destination: The index of the destination peg.
# auxiliary: The index of the auxiliary peg.
# If n is 1, it means there's only one disk to move, so it directly prints the move.
# Otherwise, it recursively calls itself:
# Moves n-1 disks from the source to the auxiliary peg using the destination as the temporary peg.
# Moves the largest disk (n) from the source to the destination.
# Moves the n-1 disks from the auxiliary to the destination using the source as the temporary peg.
# Example usage:

# Sets n to 3 (the number of disks).
# Calls the tower_of_hanoi function with the initial pegs: source (1), destination (3), and auxiliary (2).
# Output:

# Move disk 1 from peg 1 to peg 3
# Move disk 2 from peg 1 to peg 2
# Move disk 1 from peg 3 to peg 2
# Move disk 3 from peg 1 to peg 3
# Move disk 1 from peg 2 to peg 1
# Move disk 2 from peg 2 to peg 3
# Move disk 1 from peg 1 to peg
#  3
# This output demonstrates the correct sequence of moves to solve the Tower of Hanoi problem with 3 disks.
