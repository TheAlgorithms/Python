"""
Picks a pivot that is based on the median between 3 values
"""
def partition(A, left_index, right_index):
    pivot = A[left_index]
    i = left_index + 1
    for j in range(left_index + 1, right_index):
        if A[j] < pivot:
            A[j], A[i] = A[i], A[j]
            i += 1
    A[left_index], A[i - 1] = A[i - 1], A[left_index]
    return i - 1

def quick_sort_median(A, left, right):
    if left < right:
        get_median(A, left, right - 1)
        pivot_index = partition(A, left, right)
        quick_sort_median(A, left, pivot_index)
        quick_sort_median(A, pivot_index + 1, right)

#Helper function to get the median value and then swap it into the left most position
#at a given recursive call
def get_median(A, left, right):
    if right - left <= 1:
        if A[left] > A[right]:
            A[left], A[right] = A[right], A[left]
    else:
        first = A[left]
        middle = A[left + ((right - left) // 2)]
        last = A[right]

        if middle > first and middle < last or middle < first and middle > last:
            A[left + ((right - left) // 2)], A[left] = first, middle
        elif last > first and last < middle or last < first and last > middle:
            A[right], A[left] = first, last

if __name__ == "__main__":
    try:
        raw_input          # Python 2
    except NameError:
        raw_input = input  # Python 3
        
    user_input = raw_input('Enter numbers separated by a comma:\n').strip()
    arr = [int(item) for item in user_input.split(',')]

    quick_sort_median(arr, 0, len(arr))

    print(arr)