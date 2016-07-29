
def quicksort(A, p, r):
    if p < r:
        q = partition(A, p, r)
        quicksort(A, p, q - 1)
        quicksort(A, q + 1, r)


def partition(A, p, r):
    x = A[r]
    i = p - 1
    for j in range(p, r):
        if A[j] <= x:
            i += 1
            tmp = A[i]
            A[i] = A[j]
            A[j] = tmp
    tmp = A[i+1]
    A[i+1] = A[r]
    A[r] = tmp
    return i + 1


if __name__ == "__main__":
    print('Enter values seperated by space:')
    A = [int (item) for item in input().split(' ')]
    # A = [23, 45, 43, 12, 67, 98, 123, 99]
    # partition(A, 0, 7)
    print(A)
    quicksort(A, 0, 7)
    print(A)
