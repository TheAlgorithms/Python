"""
Calculate Product Sum from an Array.
reference: https://dev.to/sfrasica/algorithms-product-sum-from-an-array-dc6

For doctests run following command:
python -m doctest -v product_sum.py

We need to create a function that calculates the product sum of a "special" array.
This array can contain integers or nested arrays. The product sum is obtained by
adding all the elements together and multiplying by their respective depth.

For example, in the array [x, y], the product sum is (x + y). In the array [x, [y, z]],
the product sum is x + 2 * (y + z). In the array [x, [y, [z]]],
the product sum is x + 2 * (y + 3z).

Example Input:

[5, 2, [-7, 1], 3, [6, [-13, 8], 4]]
"""


def product_sum(arr: list[int | list], depth: int) -> int:
    """
    Recursively calculates the product sum of an array.

    The product sum of an array is defined as the sum of its elements multiplied by
    their respective depths.If an element is a list, its product sum is calculated
    recursively by multiplying the sum of its elements with its depth plus one.

    Args:
        arr: The array of integers and nested lists.
        depth: The current depth level.

    Returns:
        int: The product sum of the array.

    Examples:
        >>> product_sum([1, 2, 3], 1)
        6
        >>> product_sum([-1, 2, [-3, 4]], 2)
        8
    """
    total_sum = 0
    for ele in arr:
        if isinstance(ele, list):
            total_sum += product_sum(ele, depth + 1)
        else:
            total_sum += ele
    return total_sum * depth


def product_sum_array(array: list[int | list]) -> int:
    """
    Calculates the product sum of an array.

    Args:
        array (List[Union[int, List]]): The array of integers and nested lists.

    Returns:
        int: The product sum of the array.

    Examples:
        >>> product_sum_array([1, 2, 3])
        6
        >>> product_sum_array([1, [2, 3]])
        11
        >>> product_sum_array([1, [2, [3, 4]]])
        47
    """
    return product_sum(array, 1)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
