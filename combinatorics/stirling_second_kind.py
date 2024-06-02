"""
https://en.wikipedia.org/wiki/Stirling_numbers_of_the_second_kind
"""


def validate_elements_count(
    total_elements_count: int, selected_elements_count: int
) -> None:
    """
    # If either of the conditions are true, the function is being asked
    # to calculate a factorial of a negative number, which is not possible
    Examples:
    >>> validate_elements_count(6, 3)
    >>> validate_elements_count(10, 5)
    """
    if total_elements_count < selected_elements_count or selected_elements_count < 0:
        raise ValueError(
            "Please enter positive integers for total_elements_count"
            "and selected_elements_count where total_elements_count >= selected_elements_count"
        )


def stirling_second(total_elements_count: int, selected_elements_count: int) -> None:
    """
    Returns the number of different combinations of 
    selected_elements_count length which can be made from 
    total_elements_count values,  where 
    total_elements_count >= selected_elements_count.

    Examples:
    >>> stirling_second(6, 3)
    122
    >>> stirling_second(10, 5)
    50682
    >>> stirling_second(8, 3)
    1389
    """

    validate_elements_count(total_elements_count, selected_elements_count)
    permutations_count = [
        [0] * (selected_elements_count + 1) for _ in range(total_elements_count + 1)
    ]

    for i in range(total_elements_count + 1):
        permutations_count[i][0] = 1

    for i in range(1, total_elements_count + 1):
        for j in range(1, selected_elements_count + 1):
            permutations_count[i][j] = (
                j * permutations_count[i - 1][j] + permutations_count[i - 1][j - 1]
            )

    return permutations_count[total_elements_count][selected_elements_count]


if __name__ == "__main__":
    __import__("doctest").testmod()
