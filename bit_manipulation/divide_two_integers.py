class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        """
        Divide two integers without using *, /, or % operators.

        LeetCode Problem: https://leetcode.com/problems/divide-two-integers/

        Args:
            dividend (int): The number to be divided.
            divisor (int): The number to divide by.

        Returns:
            int: The quotient after truncating toward zero.

        Examples:
        >>> sol = Solution()
        >>> sol.divide(43, 8)
        5
        >>> sol.divide(10, 3)
        3
        >>> sol.divide(-7, 2)
        -3
        >>> sol.divide(1, 1)
        1
        >>> sol.divide(-2147483648, -1)  # overflow case
        2147483647
        >>> sol.divide(24, 8)
        3
        >>> sol.divide(43, -8)
        -5
        """
        # Edge case: if both are equal, result is 1
        if dividend == divisor:
            return 1

        # Determine the sign of the result
        sign = not (
            (dividend < 0) ^ (divisor < 0)
        )  # True if same sign, False if different

        # Convert both numbers to positive
        d = abs(dividend)  # remaining dividend
        n = abs(divisor)  # divisor
        quo = 0  # quotient

        # Outer loop: subtract divisor multiples from dividend
        while d >= n:
            cnt = 0
            """Inner loop: find largest power-of-two multiple of divisor
            that fits in dividend """
            while d >= (n << (cnt + 1)):
                cnt += 1

            # Add this power-of-two chunk to quotient
            quo += 1 << cnt

            # Subtract the chunk from remaining dividend
            d -= n << cnt

        # Handle overflow for 32-bit signed integers
        if quo == (1 << 31):
            return (2**31 - 1) if sign else -(2**31)

        return quo if sign else -quo


if __name__ == "__main__":
    import doctest

    doctest.testmod()  # Run the doctest examples

    # Optional: interactive test
    sol = Solution()
    dividend = int(input("Enter dividend: "))
    divisor = int(input("Enter divisor: "))
    print(f"Quotient: {sol.divide(dividend, divisor)}")
