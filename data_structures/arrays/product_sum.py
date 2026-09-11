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
Output: -12

"""

from timeit import timeit


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


def product_sum_iterative(arr: list[int | list]) -> int:
    """
    It Calculates the product sum of an array using iterative approach.
    It's similar to BFS algorithm (Breadth first search algorithm).
    It's won't run into stack overflow as compared to recursion approach

    Args:
        array(List[Union[int, List]]): The array of integers/lists

    Returns:
        int: The product sum of the array.

    Logic :
        1. Initialize a queue which stores the list, current
            depth and it's multiplication factor
            eg. queue -> [(arr, depth, multiplication_factor)]

        2. Loop until queue is empty
            1. Take front item from Queue and pop it
            2. Iterate on front element
                If current element is nested list
                    - then add that into queue with updated depth
                      and multiplication factor
                Else if current element is not nested
                    - then update product sum variable by multiplying
                      current element with multiplicaton factor

    Algorithm flow example ->
        Input list - [5, 2, [-7, 1], 3, [6, [-13, 8], 4]]

        Initialize queue - [([5, 2, [-7, 1], 3, [6, [-13, 8], 4]], 1, 1)]

        Step 0
            Queue - [([5, 2, [-7, 1], 3, [6, [-13, 8], 4]], 1, 1)]
            Queue front item -
                List - [5, 2, [-7, 1], 3, [6, [-13, 8], 4]]
                depth - 1
                multiplication factor - 1

            product sum = 0 (previous) + 5 * 1 + 2 * 1 + 3 * 1 = 10
        -------------------------------------------------------
        Step 1
            Queue - [([-7, 1], 2, 2), ([6, [-13, 8], 4], 2, 2)]
            Queue front item -
                List - [-7, 1]
                depth - 2
                multiplication factor - 2

            product sum = 10 (previous) +  (-7) * 2 + 1 * 2 = -2
        -------------------------------------------------------
        Step 2
            Queue - [([6, [-13, 8], 4], 2, 2)]
            Queue front item -
                List - [6, [-13, 8], 4]
                depth - 2
                multiplication factor - 2

            product sum = -2 (previous) + 6 * 2 +  4 * 2 = 18
        -------------------------------------------------------
        Step 3
            Queue - [([-13, 8], 3, 6)]
            Queue front item -
                List - [-13, 8]
                depth - 3
                multiplication factor - 6

            product sum = 18 (previous) + (-13) * 6 + 8 * 6 = -12
        -------------------------------------------------------

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

    # Initialize queue with depth and multiplication factor
    queue = [(arr, 1, 1)]

    product_sum = 0

    while queue:
        queue_front_list, depth, multiplication_factor = queue.pop(0)

        for element in queue_front_list:
            if isinstance(element, list):
                queue.append((element, depth + 1, multiplication_factor * (depth + 1)))
            else:
                product_sum += element * multiplication_factor

    return product_sum


def benchmark() -> None:
    """
    Benchmark code comparing different version.
    """

    setup = "from __main__ import product_sum_array, product_sum_iterative"

    print(
        timeit("product_sum_array([5, 2, [-7, 1], 3, [6, [-13, 8], 4]])", setup=setup)
    )
    # 1.1448657000437379

    print(
        timeit(
            "product_sum_iterative([5, 2, [-7, 1], 3, [6, [-13, 8], 4]])", setup=setup
        )
    )
    # 1.6824490998405963


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    benchmark()
