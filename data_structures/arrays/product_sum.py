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
from typing import List, Union

def product_sum_recursive(arr: List[Union[int, List]], depth: int) -> int:
    total_sum = 0
    for ele in arr:
        if isinstance(ele, list):
            total_sum += product_sum_recursive(ele, depth + 1)
        else:
            total_sum += ele
    return total_sum * depth

def product_sum_array(array: List[Union[int, List]]) -> int:
    if not isinstance(array, list):
        raise ValueError("Input must be a list.")
    return product_sum_recursive(array, 1)

if __name__ == "__main__":
    import doctest
    doctest.testmod()
