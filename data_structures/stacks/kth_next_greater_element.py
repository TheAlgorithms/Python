"""
Implement the function to find kth Next Greatest Element (NGE) for all elements.
Idea comes from my blog:
https://starsexpress.github.io/SkyHorse/docs/stack/2454_hard/second_next_greater
"""

test_k = 10
test_array = list(range(10000))
expected_answers = [value + test_k for value in range(10000 - test_k)] + [None] * test_k


def find_kth_next_greater_element(
    array: list[int | float], kth_ord: int
) -> list[int | float | None]:
    """
    Efficient general method to seek the kth NGE for all elements.
    Approach is entirely based on k stacks, which are actually very easy to understand.
    These k stacks symbolize how many NGEs an element has already found.

    For example, for 1 <= j <= k, if an element is currently at the jth stack,
    it means that this element has found its (j - 1)th NGE, now looking for jth NGE.

    By processing stacks from higher to lower ordinals, we can always ensure that
    each stack secures decreasing monotonicity in terms of element value.

    Time complexity: O(kn) where n is the length of input array.
    However, if k >= n, all elements won't find their respective kth NGE.
    As a result, worst case time complexity is O(n^2) when k < n but k ≈ n.

    Space complexity: O(n), since at any point, an element is only in one of k stacks.

    Args:
        array (list[int | float]): A list for which the kth NGE is computed.
                                   A mix of integers and floats in list is allowed.

        kth_ord (int): Ordinal of the NGE to find. k must be a positive integer.

    Returns:
        A list containing each element's kth NGE. If an element can't find its kth NGE,
        None, instead of -1, is put as its entry, because input array might have -1.

    Example:
    >>> find_kth_next_greater_element([1, 2, 3, 4, 5], 3) == [4, 5, None, None, None]
    True
    >>> find_kth_next_greater_element([2.5, 1.9, 4.3, 6.0], 1) == [4.3, 4.3, 6.0, None]
    True
    >>> find_kth_next_greater_element(list(range(1000)), 1000) == [None] * 1000
    True
    >>> find_kth_next_greater_element(test_array, test_k) == expected_answers
    True
    """
    if not isinstance(kth_ord, int) or kth_ord < 1:
        raise ValueError("k must be a positive integer.")

    kth_next_greater_elements: list[int | float | None] = [None] * len(array)
    if kth_ord >= len(array):  # Trivial cases: nobody can have kth NGE.
        return kth_next_greater_elements

    # For 1 <= j <= k, the jth stack is at the jth idx of stacks list.
    # stacks[0]: a transporter that transfer entries between stacks.
    # Each stack's entry is a tuple of (element, idx).
    stacks: list[list[tuple[int | float, int]]] = [[] for _ in range(kth_ord + 1)]

    for idx, element in enumerate(array):
        # From kth stack to answer found.
        while stacks[kth_ord] and stacks[kth_ord][-1][0] < element:
            _, prev_idx = stacks[kth_ord].pop()
            kth_next_greater_elements[prev_idx] = element

        for stack_ord in range(kth_ord - 1, 0, -1):  # From (k - 1)th to 1st stack.
            while stacks[stack_ord] and stacks[stack_ord][-1][0] < element:
                stacks[0].append(stacks[stack_ord].pop())

            while stacks[0]:  # Move to the next ordered stack.
                stacks[stack_ord + 1].append(stacks[0].pop())

        unvisited_elements_count = len(array) - 1 - idx
        if unvisited_elements_count >= kth_ord:  # Element has a chance to find kth NGE.
            stacks[1].append((element, idx))  # Always join 1st stack to begin search.

    return kth_next_greater_elements


if __name__ == "__main__":
    from doctest import testmod
    from timeit import timeit

    testmod()
    setup = "from __main__ import test_array, test_k, find_kth_next_greater_element"
    print(
        "find_kth_next_greater_element():",
        timeit("find_kth_next_greater_element(test_array, test_k)", setup=setup),
    )
