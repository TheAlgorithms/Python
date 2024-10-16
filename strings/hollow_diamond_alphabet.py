def hollow_diamond_alphabet(n):
    """
    Prints a hollow diamond pattern using uppercase alphabet characters.
    
    :param n: An integer representing the number of rows in the diamond.
    :return: True if the pattern was successfully printed, False otherwise.
    """
    if not isinstance(n, int):
        print("Error: Input must be an integer.")
        return False
    
    if n <= 0:
        print("Error: Input must be a positive integer.")
        return False
    
    if n % 2 == 0:
        print("Error: Input must be an odd integer.")
        return False
    
    # Calculate the number of rows for the upper half of the diamond
    upper_rows = (n + 1) // 2
    
    # Print the upper half of the diamond
    for i in range(upper_rows):
        char = chr(65 + i)  # Convert number to uppercase alphabet
        if i == 0:
            print(" " * (upper_rows - 1) + char)
        else:
            print(" " * (upper_rows - i - 1) + char + " " * (2 * i - 1) + char)
    
    # Print the lower half of the diamond
    for i in range(upper_rows - 2, -1, -1):
        char = chr(65 + i)  # Convert number to uppercase alphabet
        if i == 0:
            print(" " * (upper_rows - 1) + char)
        else:
            print(" " * (upper_rows - i - 1) + char + " " * (2 * i - 1) + char)
    
    return True

def get_valid_input():
    """
    Prompts the user for input and validates it.
    
    :return: A valid positive odd integer, or None if the user chooses to quit.
    """
    while True:
        user_input = input("Enter the diamond size (positive odd integer) or 'q' to quit: ")
        
        if user_input.lower() == 'q':
            return None
        
        try:
            n = int(user_input)
            if n > 0 and n % 2 != 0:
                return n
            elif n <= 0:
                print("Error: Please enter a positive integer.")
            else:
                print("Error: Please enter an odd integer.")
        except ValueError:
            print("Error: Invalid input. Please enter a valid integer.")

# Main program
def main():
    while True:
        size = get_valid_input()
        if size is None:
            print("Thank you for using the Hollow Diamond Alphabet Pattern generator. Goodbye!")
            break
        
        if hollow_diamond_alphabet(size):
            print("\nDiamond pattern printed successfully!")
        
        print()  # Add a blank line for better readability

if __name__ == "__main__":
    main()
