This Folder shows 3 different version of the Sorting Algorithm Quick Sort.

Summary of the Algorithm
----------------------
Quick Sort takes an unsorted array and sorts it recursively by picking a pivot point which is an index in the array.
This value at this point is compared to every other value in the array. All of the values that are smaller than the
pivot value get pushed to the left side of the pivot value and all of the values larger than the pivot value gets
pushed to the right side of the pivot value. Once every value is placed, the pivot changes places with a variable
that keeps track of where the pivot's final position should be. Now a recursive call happens on the left and right side
of where the pivot is places. A pivot point is picked on each and the steps are repeated all over again.

Explaining the Partition Function
----------------------
def partition(A, left_index, right_index):
    pivot = A[left_index]
    i = left_index + 1 #position to swap the pivot point after it has been compared
    for j in range(left_index + 1, right_index): #increments through the bounds to compare with the pivot
        if A[j] < pivot:
            A[j], A[i] = A[i], A[j]
            i += 1 #increments if it finds a value smaller than the pivot. This ensures the pivot will be places in the correct point in the end
    A[left_index], A[i - 1] = A[i - 1], A[left_index] #swapping the pivot into its final position
    return i - 1

Key Notes of Quick Sort
----------------------
1. The pivot point is the major factor of the efficiency of this algorithm.
	a. The worse possible pivot point every time leads to a run time of O(n^2)
	b. The best possible pivot point every time leads to a run time of O(nlogn)
	c. The interesting part is if on average a decent point is picked then the run time is O(nlogn)
2. Very little memory is used because all of the sorting is done within the array.

This implementation uses 3 different ways to select the pivot point.
Quick Sort First: always takes the first element in the array and then partitions it.
Quick Sort Median3: takes the median value of the first, middle and last value.
Quick Sort Random: takes a random index value in the left and right bound as the pivot

How each quick sort function generates it's code will be the same but each pivot point implementation really shows the
tradeoffs between each of the methods

Tutorial of how to Run
----------------------
Change to quick_sort_variations direction
Run the program and use the path "./test_files/<test file you want to run>" when prompted