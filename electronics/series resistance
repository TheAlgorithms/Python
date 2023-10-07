def series_resistance_calculator():
    try:
        # Step 1: Get the number of resistors in the series circuit
        num_resistors = int(input("Enter the number of resistors in the series circuit: "))
        
        # Initialize total resistance to 0
        total_resistance = 0

        # Step 2: Loop through each resistor and calculate the total resistance
        for i in range(1, num_resistors + 1):
            resistance = float(input(f"Enter the resistance value for resistor {i} (in ohms): "))
            total_resistance += resistance

        # Step 3: Calculate the total resistance
        print(f"The total resistance of the series circuit is {total_resistance} ohms.")

    except ValueError:
        print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    series_resistance_calculator()
