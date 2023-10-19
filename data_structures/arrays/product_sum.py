"""
Calculate the Product Sum from a Special Array.
reference: https://dev.to/sfrasica/algorithms-product-sum-from-an-array-dc6

Python doctests can be run with the following command:
python -m doctest -v product_sum.py

Calculate the product sum of a "special" array which can contain integers or nested
arrays. The product sum is obtained by adding all elements and multiplying by their
respective depths.

For example, in the array [x, y], the product sum is (x + y). In the array [x, [y, z]],
the product sum is x + 2 * (y + z). In the array [x, [y, [z]]],
the product sum is x + 2 * (y + 3z).

Example Input:
[5, 2, [-7, 1], 3, [6, [-13, 8], 4]]
Output: 12

"""


def product_sum(arr: list[int | list], depth: int) -> int:
    """
    Recursively calculates the product sum of an array.

    The product sum of an array is defined as the sum of its elements multiplied by
    their respective depths.  If an element is a list, its product sum is calculated
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
        >>> product_sum([1, 2, 3], -1)
        -6
        >>> product_sum([1, 2, 3], 0)
        0
        >>> product_sum([1, 2, 3], 7)
        42
        >>> product_sum((1, 2, 3), 7)
        42
        >>> product_sum({1, 2, 3}, 7)
        42
        >>> product_sum([1, -1], 1)
        0
        >>> product_sum([1, -2], 1)
        -1
        >>> product_sum([-3.5, [1, [0.5]]], 1)
        1.5

    """
    total_sum = 0
    for ele in arr:
        total_sum += product_sum(ele, depth + 1) if isinstance(ele, list) else ele
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
        >>> product_sum_array([0])
        0
        >>> product_sum_array([-3.5, [1, [0.5]]])
        1.5
        >>> product_sum_array([1, -2])
        -1

    """
    return product_sum(array, 1)


def product_sum_iterative(arr: list[int | list | set | tuple]) -> int:
    """
    Calculates the product sum of an array using iterative approach.

    Logic :
        1. Loop until input list have nested list/tuple/set
            1. iterate on each item in input array
            2. if item is nested list/tuple/set then
                - multiply the nested item with it's depth and add it's elements
                  to new array
            3. if item is not nested then
                add item to total sum
            4. update old array with new array and increment depth value

    Algorithm flow example ->
        Step 1 --> Array - [5, 2, [-7, 1], 3, [6, [-13, 8], 4]]
                   total sum = 0 + () = 0
        Step 2 --> Array - [-7, 1, -7, 1, 6, [-13, 8], 4, 6, [-13, 8], 4]
                   total sum = 0 + (5 + 2 + 3) = 10
        Step 3 --> Array - [-13, 8, -13, 8, -13, 8, -13, 8, -13, 8, -13, 8]
                   total sum = 10 + (-7 + 1 -7 + 1 + 6 + 4 + 6 + 4) = 18
        Step 4 --> Array - [-13, 8, -13, 8, -13, 8, -13, 8, -13, 8, -13, 8]
                   total sum=18 +(-13 + 8 -13 + 8 -13 + 8 -13 + 8 -13 + 8 -13 + 8)= -12

    Args:
        array(List[Union[int, List, Set, Tuple]]): The array of integers/lists/tuple/set

    Returns:
        int: The product sum of the array.

    Examples:
        >>> product_sum_iterative([1, 2, 3])
        6
        >>> product_sum_iterative([1, [2, 3]])
        11
        >>> product_sum_iterative([1, [2, [3, 4]]])
        47
        >>> product_sum_iterative([0])
        0
        >>> product_sum_iterative([-3.5, [1, [0.5]]])
        1.5
        >>> product_sum_iterative([1, -2])
        -1

    """

    # depth of the nested list/tuple/set
    next_depth = 2

    # flag to check whether list has nested items or not
    nested_list_check = True

    total_sum = 0

    while nested_list_check:
        # list to store new items
        new_arr = []
        nested_list_check = False

        for item in arr:
            if isinstance(item, list | tuple | set):
                new_arr.extend(list(item) * next_depth)
                nested_list_check = True
            else:
                total_sum += item

        arr = new_arr
        next_depth += 1

    return total_sum


if __name__ == "__main__":
    import doctest

    doctest.testmod()
