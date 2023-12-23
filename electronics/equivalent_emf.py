def equi_emf(cells, connection_type):
    total_emf = 0
    tot_int_res = 0

    for emf, int_res in cells:
        total_emf += emf

        if connection_type == "series":
            tot_int_res += int_res
        elif connection_type == "parallel":
            tot_int_res += 1 / int_res

    if connection_type == "parallel":
        tot_int_res = 1 / tot_int_res

    return total_emf, tot_int_res


def main():
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
