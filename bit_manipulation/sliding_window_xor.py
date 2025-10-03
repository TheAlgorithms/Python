"""
Author  : Abhiraj Mandal
Date    : October 3, 2025

This is a pure Python implementation to calculate the cumulative XOR of all
sliding windows of size window_size in an array generated via a linear recurrence.

The problem is :
Given parameters array_length, window_size, first_element, multiplier, increment,
modulo, generate an array:

    arr[0] = first_element
    arr[i] = (multiplier * arr[i-1] + increment) % modulo
Compute the XOR of each window of size window_size, and cumulatively XOR all windows.
"""


class SlidingWindowXOR:
    """
        Use:
        solver       = SlidingWindowXOR()
        result = solver.compute(
        array_length,
        window_size,
        first_element,
        multiplier,
        increment,
        modulo
    )

    """

    def compute(
        self,
        array_length: int,
        window_size: int,
        first_element: int,
        multiplier: int,
        increment: int,
        modulo: int,
    ) -> int:
        """
        Compute cumulative XOR of all sliding windows of size window_size.

        >>> SlidingWindowXOR().compute(5, 2, 1, 1, 1, 100)
        4
        >>> SlidingWindowXOR().compute(2, 1, 2, 3, 4, 5)
        2
        """
        # Generate the array using recurrence
        arr = [0] * array_length
        arr[0] = first_element
        for i in range(1, array_length):
            arr[i] = (multiplier * arr[i - 1] + increment) % modulo

        x1 = 0  # XOR of current window
        x2 = 0  # cumulative XOR of all windows
        left = 0

        for right in range(array_length):
            x1 ^= arr[right]  # include current element
            if right - left + 1 > window_size:
                x1 ^= arr[left]  # remove leftmost element
                left += 1
            if right - left + 1 == window_size:
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

    for idx, test_case in enumerate(test_cases, 1):
        (
            array_length,
            window_size,
            first_element,
            multiplier,
            increment,
            modulo,
            expected,
        ) = test_case
        result = solver.compute(
            array_length, window_size, first_element, multiplier, increment, modulo
        )
        print(f"Testcase {idx}: Expected={expected}, Got={result}")
        assert result == expected, f"Testcase {idx} failed!"

    print("\nAll test cases successfully passed!")
    print("********** End of Testing Sliding Window XOR Algorithm **********")
