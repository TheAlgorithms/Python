# Sortings in Python
### By: [Anmol Singh Yadav](https://github.com/IamLucif3r/)
Below is compilation of every kind of sortings in Python

The different implementations of sorting techniques in Python are:
- Bubble Sort
- Selection Sort
- Insertion Sort

## Bubble Sort
Bubble Sort is a simple sorting algorithm. This sorting algorithm repeatedly compares two adjacent elements and swaps them if they are in the wrong order. It is also known as the sinking sort. It has a time complexity of O(n2) in the average and worst cases scenarios and O(n) in the best-case scenario. Bubble sort can be visualized as a queue where people arrange themselves by swapping with each other so that they all can stand in ascending order of their heights.

### Bubble Sort Code

```python
# Python3 program for Bubble Sort Algorithm Implementation
def bubbleSort(arr):
	
	n = len(arr)

	# For loop to traverse through all
	# element in an array
	for i in range(n):
		for j in range(0, n - i - 1):
			
			# Range of the array is from 0 to n-i-1
			# Swap the elements if the element found
			#is greater than the adjacent element
			if arr[j] > arr[j + 1]:
				arr[j], arr[j + 1] = arr[j + 1], arr[j]
				
arr = [ 2, 1, 10, 23 ]

bubbleSort(arr)

print("Sorted array is:")
for i in range(len(arr)):
	print("%d" % arr[i])

```

<hr>

## Selection Sort

This sorting technique repeatedly finds the minimum element and sort it in order. Bubble Sort does not occupy any extra memory space. During the execution of this algorithm, two subarrays are maintained, the subarray which is already sorted, and the remaining subarray which is unsorted. During the execution of Selection Sort for every iteration, the minimum element of the unsorted subarray is arranged in the sorted subarray. Selection Sort is a more efficient algorithm than bubble sort. Sort has a Time-Complexity of O(n2) in the average, worst, and in the best cases.

### Selection Sort Code

```python
# Selection Sort algorithm in Python
def selectionSort(array, size):
	
	for s in range(size):
		min_idx = s
		
		for i in range(s + 1, size):
			
			# For sorting in descending order
			# for minimum element in each loop
			if array[i] < array[min_idx]:
				min_idx = i

		(array[s], array[min_idx]) = (array[min_idx], array[s])


data = [ 7, 2, 1, 6 ]
size = len(data)
selectionSort(data, size)

print('Sorted Array in Ascending Order is :')
print(data)

```

<hr>


## Insertion Sort

This sorting algorithm maintains a sub-array that is always sorted. Values from the unsorted part of the array are placed at the correct position in the sorted part. It is more efficient in practice than other algorithms such as selection sort or bubble sort. Insertion Sort has a Time-Complexity of O(n2) in the average and worst case, and O(n) in the best case.

### Insertion Sort Code

```python
# Creating a function for insertion sort algorithm
def insertion_sort(list1):

		# Outer loop to traverse on len(list1)
		for i in range(1, len(list1)):

			a = list1[i]

			# Move elements of list1[0 to i-1],
			# which are greater to one position
			# ahead of their current position
			j = i - 1
		
			while j >= 0 and a < list1[j]:
				list1[j + 1] = list1[j]
				j -= 1
				
			list1[j + 1] = a
			
		return list1
			
list1 = [ 7, 2, 1, 6 ]
print("The unsorted list is:", list1)
print("The sorted new list is:", insertion_sort(list1))

```
