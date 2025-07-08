"""
This script prompts the user to input their age
and validates that it is a non-negative integer.
"""

def get_valid_age() -> int:
    """
    Continuously prompts user for a valid age input until a non-negative integer is provided.

    Returns:
        int: The validated age input.
    """
    while True:
        age = input("Enter your age: ")
        if age.isdigit():
            num = int(age)
            if num < 0:
                print("Age can't be negative.")
            else:
                return num
        else:
            print("Invalid input. Please enter a valid number.")


if __name__ == "__main__":
    age = get_valid_age()
    print(f"Your age is {age}")
