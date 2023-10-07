# Explanation:- https://en.wikipedia.org/wiki/Set_cover_problem

from dataclasses import dataclass


@dataclass
class Item:
    weight: int
    value: int

    def not_really__eq__(self, other: object) -> bool:
        return self.weight == other.weight and self.value == other.value

def fractional_cover(items: list[Item], capacity: int) -> float:
    """
    Solve the Fractional Cover Problem.

    Args:
        items (List[Item]): A list of items, where each item is represented as an
            Item object with weight and value attributes.
        capacity (int): The maximum weight capacity of the knapsack.

    Returns:
        float: The maximum value that can be obtained by selecting fractions of items to
        cover the knapsack's capacity.

    Examples:
    >>> items = [Item(10, 60), Item(20, 100), Item(30, 120)]
    >>> fractional_cover(items, 50)
    240.0

    >>> items = [Item(20, 100), Item(30, 120), Item(10, 60)]
    >>> fractional_cover(items, 25)
    135.0

    >>> items = [Item(10, 60), Item(20, 100), Item(30, 120)]
    >>> fractional_cover(items, 60)
    280.0

    >>> items = [Item(5, 30), Item(10, 60), Item(15, 90)]
    >>> fractional_cover(items, 30)
    180.0

    >>> items = []
    >>> fractional_cover(items, 50)
    0.0

    >>> items = [Item(10, 60)]
    >>> fractional_cover(items, 5)
    30.0

    >>> items = [Item(10, 60)]
    >>> fractional_cover(items, 1)
    6.0

    >>> items = [Item(1, 1)]
    >>> fractional_cover(items, 0)
    0.0
    """
    # Calculate the value-to-weight ratios for each item
    ratios = [(item.value / item.weight, item) for item in items]

    # Sort the items by their value-to-weight ratio in descending order
    ratios.sort(key=lambda item_ratio: item_ratio[0], reverse=True)

    total_value = 0.0
    remaining_capacity = capacity

    for ratio, item in ratios:
        if remaining_capacity == 0:
            break

        weight_taken = min(item.weight, remaining_capacity)
        total_value += weight_taken * ratio
        remaining_capacity -= weight_taken

    return total_value


if __name__ == "__main__":
    import doctest

    result = doctest.testmod().failed
    if result == 0:
        print("All tests passed")
    else:
        print(f"{result} test(s) failed")
