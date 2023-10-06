def tower_of_hanoi(
    n: int, source_peg: str, auxiliary_peg: str, target_peg: str
) -> None:
    """
    Solve the Tower of Hanoi problem for 'n' disks.

    Args:
        n (int): The number of disks to move.
        source_peg (str): The name of the source peg.
        auxiliary_peg (str): The name of the auxiliary peg.
        target_peg (str): The name of the target peg.

    Returns:
        None

    Examples:
        >>> tower_of_hanoi(1, 'A', 'B', 'C')
        Move disk 1 from A to C

        >>> tower_of_hanoi(3, 'A', 'B', 'C')
        Move disk 1 from A to C
        Move disk 2 from A to B
        Move disk 1 from C to B
        Move disk 3 from A to C
        Move disk 1 from B to A
        Move disk 2 from B to C
        Move disk 1 from A to C
    """
    if n == 1:
        print(f"Move disk 1 from {source_peg} to {target_peg}")
        return
    tower_of_hanoi(n - 1, source_peg, target_peg, auxiliary_peg)
    print(f"Move disk {n} from {source_peg} to {target_peg}")
    tower_of_hanoi(n - 1, auxiliary_peg, source_peg, target_peg)


# Input from the user
if __name__ == "__main__":
    n = int(input("Enter the number of disks: "))
    source_peg = input("Enter the name of the source peg (e.g., 'A'): ").strip().upper()
    auxiliary_peg = (
        input("Enter the name of the auxiliary peg (e.g., 'B'): ").strip().upper()
    )
    target_peg = input("Enter the name of the target peg (e.g., 'C'): ").strip().upper()

    # Ensure peg names are distinct
    while (
        source_peg == auxiliary_peg
        or source_peg == target_peg
        or auxiliary_peg == target_peg
    ):
        print("Peg names must be distinct. Please enter again.")
        source_peg = input("Enter the name of the source peg: ").strip().upper()
        auxiliary_peg = input("Enter the name of the auxiliary peg: ").strip().upper()
        target_peg = input("Enter the name of the target peg: ").strip().upper()

    # Call the tower_of_hanoi function with user input
    tower_of_hanoi(n, source_peg, auxiliary_peg, target_peg)
