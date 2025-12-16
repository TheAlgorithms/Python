"""
Count Inversions in an array using a modified Merge Sort algorithm.

An inversion is a pair of indices (i, j) such that:
    - i < j
    - arr[i] > arr[j]
This represents a disorder in the array relative to a sorted order.

This implementation efficiently counts the number of such inversions
in O(n log n) time by modifying the merge step of Merge Sort.

Use Cases:
----------
- Measuring how far a sequence is from being sorted.
- Evaluating disorder in datasets (e.g., in rankings or sequences).
- Useful in computer vision, bioinformatics, and comparison of lists.
- Core concept in Kendall tau distance and other similarity metrics.
"""


def count_inversions(arr):
    def merge_sort(arr):
        if len(arr) <= 1:
            return arr, 0

        mid = len(arr) // 2
        left, inv_left = merge_sort(arr[:mid])
        right, inv_right = merge_sort(arr[mid:])
        merged, inv_split = merge(left, right)

        total_inversions = inv_left + inv_right + inv_split
        return merged, total_inversions

    def merge(left, right):
        i = j = inv_count = 0
        merged = []

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                j += 1
                inv_count += len(left) - i  # All remaining in left > right[j]

        merged += left[i:]
        merged += right[j:]
        return merged, inv_count

    _, total_inversions = merge_sort(arr)
    return total_inversions


# Example usage
if __name__ == "__main__":
    sample = [2, 4, 1, 3, 5]
    print(f"Inversion count: {count_inversions(sample)}")
