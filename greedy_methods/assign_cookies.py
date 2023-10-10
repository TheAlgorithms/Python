"""
You're a caring parent, and you want to give your children cookies. Each child has a specific cookie size they like (their "greed factor").
You have different-sized cookies. Your goal is to give cookies to as many children as possible by matching the cookie size to
each child's greed factor. How many children can you make happy?

Example: g = [1,2,3], s = [1,1], where g is the greed factor and s is the cookie size.
Answer: 1
Explanation: You have 3 children and 2 cookies. The child with greed factor 1 will be content with the cookie of size 1.


This problem can be solved using the concept of "GREEDY ALGORITHM."

As a caring parent, when distributing cookies to your children, prioritize efficiency by following this approach:

1) Sort the children's greed factors (g) and cookie sizes (s).

2) Begin with the smallest cookie and allocate it to the child with the lowest greed factor.

3) Continue this process, moving to the next child as soon as their greed is satisfied with a cookie.

4) Keep track of how many children you satisfy and return that count.

This method ensures that you maximize the number of happy children efficiently."
"""
from typing import List


def max_happy_children(greed_factors: List[int], cookie_sizes: List[int]) -> int:
    """
    Calculate the maximum number of happy children by distributing cookies.

    Args:
        greed_factors (List[int]): List of children's greed factors.
        cookie_sizes (List[int]): List of cookie sizes.

    Returns:
        int: The maximum number of happy children.

    >>> max_happy_children([1, 2, 3], [1, 1])
    1
    >>> max_happy_children([1, 2, 3], [1, 2])
    2
    >>> max_happy_children([1, 2, 3], [2, 2])
    2
    """
    greed_factors.sort()
    cookie_sizes.sort()

    child = 0
    for cookie in cookie_sizes:
        if child < len(greed_factors) and cookie >= greed_factors[child]:
            child += 1

    return child
