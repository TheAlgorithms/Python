import math


def is_power_of_four_logarithm(num: int) -> bool:
    """
    Check if a given number is a power of four using logarithms.

    Args:
        num (int): The number to be checked.

    Returns:
        bool: True if the number is a power of 4, False otherwise.

    Raises:
        ValueError: If the input number is not positive.
    """
    if num <= 0:
        raise ValueError("Input number must be positive")

    # Calculate the logarithm base 4 of the number
    log_base_4 = math.log(num, 4)

    # Check if the result is an integer
    return log_base_4.is_integer()


# Test cases
if __name__ == "__main__":
    num1 = 16  # 4^2 = 16
    num2 = 4096  # 4^6 = 4096
    num3 = 18  # Not a power of 4

    print(f"{num1} is a power of 4: {is_power_of_four_logarithm(num1)}")
    print(f"{num2} is a power of 4: {is_power_of_four_logarithm(num2)}")
    print(f"{num3} is a power of 4: {is_power_of_four_logarithm(num3)}")
