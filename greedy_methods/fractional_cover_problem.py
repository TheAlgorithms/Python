# https://en.wikipedia.org/wiki/Set_cover_problem

from dataclasses import dataclass
from operator import attrgetter


@dataclass
class Item:
    weight: int
    value: int

    @property
    def ratio(self) -> float:
        """
        Return the value-to-weight ratio for the item.

        Returns:
            float: The value-to-weight ratio for the item.

        Examples:
        >>> Item(10, 65).ratio
        6.5

        >>> Item(20, 100).ratio
        5.0

        >>> Item(30, 120).ratio
        4.0
        """
        return self.value / self.weight


def fractional_cover(items: list[Item], capacity: int) -> float:
    """
    Solve the Fractional Cover Problem.

    Args:
        items: A list of items, where each item has weight and value attributes.
        capacity: The maximum weight capacity of the knapsack.

    Returns:
        The maximum value that can be obtained by selecting fractions of items to cover
        the knapsack's capacity.

    Raises:
        ValueError: If capacity is negative.

    Examples:
    >>> fractional_cover((Item(10, 60), Item(20, 100), Item(30, 120)), capacity=50)
    240.0

    >>> fractional_cover([Item(20, 100), Item(30, 120), Item(10, 60)], capacity=25)
    135.0

    >>> fractional_cover([Item(10, 60), Item(20, 100), Item(30, 120)], capacity=60)
    280.0

    >>> fractional_cover(items=[Item(5, 30), Item(10, 60), Item(15, 90)], capacity=30)
    180.0

    >>> fractional_cover(items=[], capacity=50)
    0.0

    >>> fractional_cover(items=[Item(10, 60)], capacity=5)
    30.0

    >>> fractional_cover(items=[Item(10, 60)], capacity=1)
    6.0

    >>> fractional_cover(items=[Item(10, 60)], capacity=0)
    0.0

    >>> fractional_cover(items=[Item(10, 60)], capacity=-1)
    Traceback (most recent call last):
        ...
    ValueError: Capacity cannot be negative
    """
    if capacity < 0:
        raise ValueError("Capacity cannot be negative")

    total_value = 0.0
    remaining_capacity = capacity

    # Sort the items by their value-to-weight ratio in descending order
    for item in sorted(items, key=attrgetter("ratio"), reverse=True):
        if remaining_capacity == 0:
            break

        weight_taken = min(item.weight, remaining_capacity)
        total_value += weight_taken * item.ratio
        remaining_capacity -= weight_taken

    return total_value


if __name__ == "__main__":
    import doctest

    if result := doctest.testmod().failed:
        print(f"{result} test(s) failed")
    else:
        print("All tests passed")
