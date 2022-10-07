"""Online Reference: https://www.geeksforgeeks.org/merge-sort/"""


def mergesort(arr):
    if len(arr) == 1:
        return arr
    length = len(arr)
    mid = length // 2
    # dividing
    left = arr[:mid]
    right = arr[mid:]
    # operating
    print(f"Left {left}")
    print(f"Right {right}")
    return merge(mergesort(left), mergesort(right))


# merging
def merge(left, right):
    result = []
    leftindex = 0
    rightindex = 0
    while leftindex < len(left) and rightindex < len(right):
        if left[leftindex] < right[rightindex]:
            result.append(left[leftindex])
            leftindex += 1
        else:
            result.append(right[rightindex])
            rightindex += 1
    print(left, right)
    print(result + left[leftindex:] + right[rightindex:])
    return result + left[leftindex:] + right[rightindex:]


arr = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]
x = mergesort(arr)
print(x)
