def is_armstrong(num: int) -> bool:
    """
    Check if a number is an Armstrong number.

    Args:
        num (int): Number to check

    Returns:
        bool: True if Armstrong, False otherwise
    """
    digits = str(num)
    power = len(digits)
    total = sum(int(digit) ** power for digit in digits)
    return total == num


if __name__ == "__main__":  # <-- corrected here
    # Example usage
    number = 153
    if is_armstrong(number):
        print(f"{number} is an Armstrong number.")
    else:
        print(f"{number} is not an Armstrong number.")