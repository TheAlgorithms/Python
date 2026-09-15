from __future__ import annotations

arr = [-10, -5, 0, 5, 5.1, 11, 13, 21, 3, 4, -21, -10, -5, -1, 0]
expect = [-5, 0, 5, 5.1, 11, 13, 21, -1, 4, -1, -10, -5, -1, 0, -1]


def next_greatest_element_slow(arr: list[float]) -> list[float]:
    """
    Get the Next Greatest Element (NGE) for each element in the array
    by checking all subsequent elements to find the next greater one.

    This is a brute-force implementation, and it has a time complexity
    of O(n^2), where n is the size of the array.

    Args:
        arr: List of numbers for which the NGE is calculated.

    Returns:
        List containing the next greatest elements. If no
        greater element is found, -1 is placed in the result.

    Example:
    >>> next_greatest_element_slow(arr) == expect
    True
    """

    result = []
    arr_size = len(arr)

    for i in range(arr_size):
        next_element: float = -1
        for j in range(i + 1, arr_size):
            if arr[i] < arr[j]:
                next_element = arr[j]
                break
        result.append(next_element)
    return result


def next_greatest_element_fast(arr: list[float]) -> list[float]:
    """
    Find the Next Greatest Element (NGE) for each element in the array
    using a more readable approach. This implementation utilizes
    enumerate() for the outer loop and slicing for the inner loop.

    While this improves readability over next_greatest_element_slow(),
    it still has a time complexity of O(n^2).

    Args:
        arr: List of numbers for which the NGE is calculated.

    Returns:
        List containing the next greatest elements. If no
        greater element is found, -1 is placed in the result.

    Example:
    >>> next_greatest_element_fast(arr) == expect
    True
    """
    result = []
    for i, outer in enumerate(arr):
        next_item: float = -1
        for inner in arr[i + 1 :]:
            if outer < inner:
                next_item = inner
                break
        result.append(next_item)
    return result


def next_greatest_element(arr: list[float]) -> list[float]:
    """
    Efficient solution to find the Next Greatest Element (NGE) for all elements
    using a stack. The time complexity is reduced to O(n), making it suitable
    for larger arrays.

    The stack keeps track of elements for which the next greater element hasn't
    been found yet. By iterating through the array in reverse (from the last
    element to the first), the stack is used to efficiently determine the next
    greatest element for each element.

    Args:
        arr: List of numbers for which the NGE is calculated.

    Returns:
        List containing the next greatest elements. If no
        greater element is found, -1 is placed in the result.

    Example:
    >>> next_greatest_element(arr) == expect
    True
    """
    arr_size = len(arr)
    stack: list[float] = []
    result: list[float] = [-1] * arr_size

    for index in reversed(range(arr_size)):
        if stack:
            while stack[-1] <= arr[index]:
                stack.pop()
                if not stack:
                    break
        if stack:
            result[index] = stack[-1]
        stack.append(arr[index])
    return result


if __name__ == "__main__":
    from doctest import testmod
    from timeit import timeit

    testmod()
    print(next_greatest_element_slow(arr))
    print(next_greatest_element_fast(arr))
    print(next_greatest_element(arr))

    setup = (
        "from __main__ import arr, next_greatest_element_slow, "
        "next_greatest_element_fast, next_greatest_element"
    )
    print(
        "next_greatest_element_slow():",
        timeit("next_greatest_element_slow(arr)", setup=setup),
    )
    print(
        "next_greatest_element_fast():",
        timeit("next_greatest_element_fast(arr)", setup=setup),
    )
    print(
        "     next_greatest_element():",
        timeit("next_greatest_element(arr)", setup=setup),
    )
