class PrefixSum:
    def __init__(self, array: list[int]) -> None:
        len_array = len(array)
        self.prefix_sum = [0] * len_array

        if len_array > 0:
            self.prefix_sum[0] = array[0]

        for i in range(1, len_array):
            self.prefix_sum[i] = self.prefix_sum[i - 1] + array[i]

    def get_sum(self, start: int, end: int) -> int:
        """
        Returns the sum of the array from index start to end (inclusive).
        Raises ValueError if the indices are invalid.
        """
        if not self.prefix_sum:
            raise ValueError("The array is empty.")

        if start < 0 or end >= len(self.prefix_sum) or start > end:
            raise ValueError("Invalid range specified.")

        return (
            self.prefix_sum[end]
            if start == 0
            else self.prefix_sum[end] - self.prefix_sum[start - 1]
        )

    def contains_sum(self, target_sum: int) -> bool:
        """
        Returns True if any subarray sum equals target_sum, otherwise False.
        """
        sums = {0}  # Initialize with 0 to check subarrays from the start
        for sum_item in self.prefix_sum:
            if (sum_item - target_sum) in sums:
                return True
            sums.add(sum_item)

        return False


if __name__ == "__main__":
    import doctest

    doctest.testmod()
