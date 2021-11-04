from __future__ import annotations

arr = [-10, -5, 0, 5, 5.1, 11, 13, 21, 3, 4, -21, -10, -5, -1, 0]
expect = [-5, 0, 5, 5.1, 11, 13, 21, -1, 4, -1, -10, -5, -1, 0, -1]


def next_greatest_element_slow(arr: list[float]) -> list[float]:
    """
    Get the Next Greatest Element (NGE) for all elements in a list.
    Maximum element present after the current one which is also greater than the
    current one.
    >>> next_greatest_element_slow(arr) == expect
    True
    """

    result = []
    arr_size = len(arr)

    for i in range(arr_size):
        next: float = -1
        for j in range(i + 1, arr_size):
            if arr[i] < arr[j]:
                next = arr[j]
                break
        result.append(next)
    return result


def next_greatest_element_fast(arr: list[float]) -> list[float]:
    """
    Like next_greatest_element_slow() but changes the loops to use
    enumerate() instead of range(len()) for the outer loop and
    for in a slice of arr for the inner loop.
    >>> next_greatest_element_fast(arr) == expect
    True
    """
    result = []
    for i, outer in enumerate(arr):
        next: float = -1
        for inner in arr[i + 1 :]:
            if outer < inner:
                next = inner
                break
        result.append(next)
    return result


def next_greatest_element(arr: list[float]) -> list[float]:
    """
    Get the Next Greatest Element (NGE) for all elements in a list.
    Maximum element present after the current one which is also greater than the
    current one.

    A naive way to solve this is to take two loops and check for the next bigger
    number but that will make the time complexity as O(n^2). The better way to solve
    this would be to use a stack to keep track of maximum number giving a linear time
    solution.
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
