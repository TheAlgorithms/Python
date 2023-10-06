# The following code will take input from user the number of cells in a circuit and their emfs along with internal resistance then it will ask whether the cells are in series or parallel and the output will be the equivalent emf and internal resistance



def equivalent_emf_internal_resistance(cells, connection_type):
    total_emf = 0
    total_internal_resistance = 0

    for emf, internal_resistance in cells:
        total_emf += emf

        if connection_type == "series":
            total_internal_resistance += internal_resistance
        elif connection_type == "parallel":
            # In parallel, the total internal resistance is the reciprocal of the sum of reciprocals
            total_internal_resistance += 1 / internal_resistance

    if connection_type == "parallel":
        total_internal_resistance = 1 / total_internal_resistance

    return total_emf, total_internal_resistance

def main():
    # Input: Number of cells
    n = int(input("Enter the number of cells: "))
    cells = []

    # Input: EMF and internal resistance for each cell
    for i in range(n):
        emf = float(input(f"Enter the EMF of cell {i+1}: "))
        internal_resistance = float(input(f"Enter the internal resistance of cell {i+1}: "))
        cells.append((emf, internal_resistance))

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
    equivalent_emf, equivalent_internal_resistance = equivalent_emf_internal_resistance(cells, connection_type)

    # Output equivalent cell parameters
    print("\nEquivalent Cell Parameters:")
    print(f"Equivalent EMF: {equivalent_emf} volts")
    print(f"Equivalent Internal Resistance: {equivalent_internal_resistance} ohms")

if __name__ == "__main__":
    main()
