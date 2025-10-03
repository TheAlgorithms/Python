"""
Author  : Abhiraj Mandal
Date    : October 3, 2025

This is a pure Python implementation to calculate the cumulative XOR of all
sliding windows of size k in an array generated via a linear recurrence.

The problem is :
Given parameters n, k, x, multiplier, increment, modulo, generate an array:
    arr[0] = x
    arr[i] = (multiplier * arr[i-1] + increment) % modulo
Compute the XOR of each window of size k, and cumulatively XOR all windows.
"""


class SlidingWindowXOR:
    """
    Use:
    solver       = SlidingWindowXOR()
    result       = solver.compute(n, k, x, multiplier, increment, modulo)
    """

    def compute(
        self, n: int, k: int, x: int, multiplier: int, increment: int, modulo: int
    ) -> int:
        """
        Compute cumulative XOR of all sliding windows of size k.

        >>> SlidingWindowXOR().compute(5, 2, 1, 1, 1, 100)
        0
        >>> SlidingWindowXOR().compute(2, 1, 2, 3, 4, 5)
        2
        """
        # Generate the array using recurrence
        arr = [0] * n
        arr[0] = x
        for i in range(1, n):
            arr[i] = (multiplier * arr[i - 1] + increment) % modulo

        x1 = 0  # XOR of current window
        x2 = 0  # cumulative XOR of all windows
        left = 0

        for right in range(n):
            x1 ^= arr[right]  # include current element
            if right - left + 1 > k:
                x1 ^= arr[left]  # remove leftmost element
                left += 1
            if right - left + 1 == k:
                x2 ^= x1

        return x2


if __name__ == "__main__":
    solver = SlidingWindowXOR()

    print("************ Testing Sliding Window XOR Algorithm ************\n")

    # Example testcases
    test_cases = [
        (100, 20, 3, 7, 1, 997, 1019),
        (2, 1, 2, 3, 4, 5, 2),
        (5, 2, 1, 1, 1, 100, 4),
        (3, 5, 5, 2, 1, 100, 0),
        (4, 4, 3, 1, 0, 10, 0),
    ]

    for idx, (n, k, x, m, inc, mod, expected) in enumerate(test_cases, 1):
        result = solver.compute(n, k, x, m, inc, mod)
        print(f"Testcase {idx}: Expected={expected}, Got={result}")
        assert result == expected, f"Testcase {idx} failed!"

    print("\nAll test cases successfully passed!")
    print("********** End of Testing Sliding Window XOR Algorithm **********")
