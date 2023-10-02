class Solution:
    def find_median_sorted_arrays(self, nums1: list[int], nums2: list[int]) -> float:
        """
        Find the median of two sorted arrays.

        Args:
            nums1: The first sorted array.
            nums2: The second sorted array.

        Returns:
            The median of the two sorted arrays.

        Example:
        >>> sol = Solution()
        >>> sol.find_median_sorted_arrays([1, 3], [2])
        2.0

        >>> sol.find_median_sorted_arrays([1, 2], [3, 4])
        2.5

        >>> sol.find_median_sorted_arrays([0, 0], [0, 0])
        0.0
        """
        # Merge the arrays into a single sorted array.
        merged = nums1 + nums2

        # Sort the merged array.
        merged.sort()

        # Calculate the total number of elements in the merged array.
        total = len(merged)

        if total % 2 == 1:
            # If the total number of elements is odd, return the
            # middle element as the median.
            return float(merged[total // 2])
        else:
            # If the total number of elements is even, calculate
            # the average of the two middle elements as the median.
            middle1 = merged[total // 2 - 1]
            middle2 = merged[total // 2]
            return (float(middle1) + float(middle2)) / 2.0


if __name__ == "__main__":
    import doctest

    doctest.testmod()
