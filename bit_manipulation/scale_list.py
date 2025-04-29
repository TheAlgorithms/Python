"""
Scale List Elements
-------------------
This function multiplies every element of the input list by a given factor.
"""


def scale_list(numbers: list, factor: float) -> list:
    """
    Scale each number in the list by a given factor.

    Args:
        numbers (list): List of numbers.
        factor (float): The factor to scale each number by.

    Returns:
        list: Scaled list of numbers.
    """
    return [num * factor for num in numbers]


if __name__ == "__main__":
    # Example usage
    print(scale_list([1, 2, 3], 2))  # Output: [2, 4, 6]
