from typing import List, Tuple


def equi_emf(
    cells: List[Tuple[float, float]], connection_type: str
) -> Tuple[float, float]:
    """
    Calculate the equivalent EMF and internal resistance of a set of cells.

    Args:
        cells (List[Tuple[float, float]]): List of tuples, each containing the
            EMF and internal resistance of a cell.
        connection_type (str): Either "series" or "parallel" to specify the
            connection type.

    Returns:
        Tuple[float, float]: Equivalent EMF (volts) and equivalent internal
        resistance (ohms).
    """
    total_emf = 0.0
    total_internal_resistance = 0.0

    for emf, int_res in cells:
        total_emf += emf

        if connection_type == "series":
            total_internal_resistance += int_res
        elif connection_type == "parallel":
            total_internal_resistance += 1.0 / int_res

    if connection_type == "parallel":
        total_internal_resistance = 1.0 / total_internal_resistance

    return total_emf, total_internal_resistance


def main() -> None:
    """
    Main function to calculate equivalent EMF and internal resistance of cells.

    Example:
    >>> import io
    >>> import sys
    >>> sys.stdin = io.StringIO('3\\n1.5\\n0.2\\n2.0\\n0.3\\n1.0\\n0.1\\n2\\n')
    >>> main()
    Enter the number of cells:
    Enter the EMF of cell 1:
    Enter the internal resistance of cell 1:
    Enter the EMF of cell 2:
    Enter the internal resistance of cell 2:
    Enter the EMF of cell 3:
    Enter the internal resistance of cell 3:
    Select the connection type (1/2):
    Invalid choice. Please select 1 or 2.
    Equivalent Cell Parameters:
    Equivalent EMF: 4.5 volts
    Equivalent Internal Resistance: 0.21176470588235294 ohms
    """
    # Input: Number of cells
    n = int(input("Enter the number of cells: "))
    cells = []

    # Input: EMF and internal resistance for each cell
    for i in range(n):
        emf = float(input(f"Enter the EMF of cell {i+1}: "))
        int_res = float(input(f"Enter the internal resistance of cell {i+1}: "))
        cells.append((emf, int_res))

    # User selects the connection type
    print("\nConnection Types:")
    print("1. Series")
    print("2. Parallel")
    connection_type = input("Select the connection type (1/2): ")

    if connection_type == "1":
        connection_type = "series"
    elif connection_type == "2":
        connection_type = "parallel"
    else:
        print("Invalid choice. Please select 1 or 2.")
        return

    # Calculate equivalent EMF and internal resistance
    eq_emf, eq_int_res = equi_emf(cells, connection_type)

    # Output equivalent cell parameters
    print("\nEquivalent Cell Parameters:")
    print(f"Equivalent EMF: {eq_emf} volts")
    print(f"Equivalent Internal Resistance: {eq_int_res} ohms")


if __name__ == "__main__":
    main()
