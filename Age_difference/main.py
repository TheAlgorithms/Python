"""
Algorithm to calculate age difference and display a message with safe input handling.

Wikipedia: https://en.wikipedia.org/wiki/Chronological_age
"""


def age_difference(boy_age: int, girl_age: int) -> int:
    """
    Returns the absolute age difference between two people.

    >>> age_difference(22, 20)
    2
    >>> age_difference(20, 22)
    2
    >>> age_difference(30, 30)
    0
    """
    return abs(boy_age - girl_age)


def get_valid_age(prompt: str) -> int:
    """Prompt the user until a valid non-negative integer age is entered."""
    while True:
        try:
            age = int(input(prompt))
            if age < 0:
                raise ValueError("Age cannot be negative.")
            return age
        except ValueError as e:
            print(f"Invalid input: {e}. Please enter a valid positive integer age.\n")


if __name__ == "__main__":
    try:
        boy_name = input("Boy Name: ").strip().capitalize()
        boy_age = get_valid_age("Boy age: ")
        girl_name = input("Girl Name: ").strip().capitalize()
        girl_age = get_valid_age("Girl age: ")

        diff = age_difference(boy_age, girl_age)
        print(f"{boy_name} loves {girl_name}. Age difference is {diff}\n")

    except KeyboardInterrupt:
        print("\nProgram interrupted by user. Exiting safely...")
