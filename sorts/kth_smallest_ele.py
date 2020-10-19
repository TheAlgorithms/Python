# //using pivot element and partition and merge sort basically
import random

def swap(A, i, j):
    A[i], A[j] = A[j], A[i]

def partition(A, lo, hi):
    pivot = A[lo]
    i = lo + 1
    j = hi

    while True:
        while A[i] < pivot:
            i += 1
            if i == hi:
                break
        while A[j] > pivot:
            j -= 1
            if j == lo:
                break
        if j <= i:
            break
        swap(A, i, j)
    swap(A, lo, j)
    print(A)
    return j

def k_smallest(A, k):
    lo = 0
    hi = len(A) - 1
    k = k - 1
    random.shuffle(A)

    while hi > lo:
        j = partition(A, lo, hi)
        if j == k:
            return A[k]
        elif j > k:
            hi = j - 1
        else:
            lo = j + 1

    return A[k]

if __name__ == '__main__':
	test_case = int(input())

	for _ in range(test_case):
		number_of_elements = int(input())
		A = [int(x) for x in input().strip().split(' ')]
		k = int(input())

		print(k_smallest(A, k))