class DualPivotQuickSort:
    def sort(self, array):
        if len(array) <= 1:
            return array

        self.dual_pivot_quick_sort(array, 0, len(array) - 1)
        return array

    def dual_pivot_quick_sort(self, array, left, right):
        if left < right:
            pivots = self.partition(array, left, right)

            self.dual_pivot_quick_sort(array, left, pivots[0] - 1)
            self.dual_pivot_quick_sort(array, pivots[0] + 1, pivots[1] - 1)
            self.dual_pivot_quick_sort(array, pivots[1] + 1, right)

    def partition(self, array, left, right):
        if array[left] > array[right]:
            array[left], array[right] = array[right], array[left]

        pivot1 = array[left]
        pivot2 = array[right]

        pivot1_end = left + 1
        low = left + 1
        high = right - 1

        while low <= high:
            if array[low] < pivot1:
                array[low], array[pivot1_end] = array[pivot1_end], array[low]
                pivot1_end += 1
            elif array[low] >= pivot2:
                while low < high and array[high] > pivot2:
                    high -= 1
                array[low], array[high] = array[high], array[low]
                high -= 1

                if array[low] < pivot1:
                    array[low], array[pivot1_end] = array[pivot1_end], array[low]
                    pivot1_end += 1
            low += 1

        pivot1_end -= 1
        high += 1

        array[left], array[pivot1_end] = array[pivot1_end], array[left]
        array[right], array[high] = array[high], array[right]

        return low, high

# Example usage
if __name__ == "__main__":
    sorter = DualPivotQuickSort()
    sample_array = [3, 7, 8, 5, 2, 1, 9, 5, 4]
    sorted_array = sorter.sort(sample_array)
    print("Sorted array:", sorted_array)
