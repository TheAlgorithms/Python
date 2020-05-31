# Python program for Bitonic Sort. Note that this program
# works only when size of input is a power of 2.


# The parameter dir indicates the sorting direction, ASCENDING
# or DESCENDING; if (a[i] > a[j]) agrees with the direction,
# then a[i] and a[j] are interchanged.
def compAndSwap(a, i, j, dire):
    if (dire == 1 and a[i] > a[j]) or (dire == 0 and a[i] < a[j]):
        a[i], a[j] = a[j], a[i]

        # It recursively sorts a bitonic sequence in ascending order,


# if dir = 1, and in descending order otherwise (means dir=0).
# The sequence to be sorted starts at index position low,
# the parameter cnt is the number of elements to be sorted.
def bitonic_merge(a, low, cnt, dire):
    if cnt > 1:
        k = int(cnt / 2)
        for i in range(low, low + k):
            compAndSwap(a, i, i + k, dire)
        bitonic_merge(a, low, k, dire)
        bitonic_merge(a, low + k, k, dire)

        # This function first produces a bitonic sequence by recursively


# sorting its two halves in opposite sorting orders, and then
# calls bitonic_merge to make them in the same order
def bitonic_sort(a, low, cnt, dire):
    if cnt > 1:
        k = int(cnt / 2)
        bitonic_sort(a, low, k, 1)
        bitonic_sort(a, low + k, k, 0)
        bitonic_merge(a, low, cnt, dire)

        # Caller of bitonic_sort for sorting the entire array of length N


# in ASCENDING order
def sort(a, N, up):
    bitonic_sort(a, 0, N, up)


if __name__ == "__main__":

    a = []

    n = int(input().strip())
    for i in range(n):
        a.append(int(input().strip()))
    up = 1

    sort(a, n, up)
    print("\n\nSorted array is")
    for i in range(n):
        print("%d" % a[i])
