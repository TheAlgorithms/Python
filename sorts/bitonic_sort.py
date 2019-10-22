# Python program for Bitonic Sort. Note that this program
# works only when size of input is a power of 2.

# The parameter dir indicates the sorting direction, ASCENDING
# or DESCENDING; if (a[i] > a[j]) agrees with the direction,
# then a[i] and a[j] are interchanged.*/
def compAndSwap(a, i, j, dire):
    if (dire == 1 and a[i] > a[j]) or (dire == 0 and a[i] < a[j]):
        a[i], a[j] = a[j], a[i]

        # It recursively sorts a bitonic sequence in ascending order,


# if dir = 1, and in descending order otherwise (means dir=0).
# The sequence to be sorted starts at index position low,
# the parameter cnt is the number of elements to be sorted.
def bitonicMerge(a, low, cnt, dire):
    if cnt > 1:
        k = int(cnt / 2)
        for i in range(low, low + k):
            compAndSwap(a, i, i + k, dire)
        bitonicMerge(a, low, k, dire)
        bitonicMerge(a, low + k, k, dire)

        # This funcion first produces a bitonic sequence by recursively


# sorting its two halves in opposite sorting orders, and then
# calls bitonicMerge to make them in the same order
def bitonicSort(a, low, cnt, dire):
    if cnt > 1:
        k = int(cnt / 2)
        bitonicSort(a, low, k, 1)
        bitonicSort(a, low + k, k, 0)
        bitonicMerge(a, low, cnt, dire)

        # Caller of bitonicSort for sorting the entire array of length N


# in ASCENDING order
def sort(a, N, up):
    bitonicSort(a, 0, N, up)


if __name__ == "__main__":
    # Driver code to test above
    a = []

    n = int(input().strip())
    for i in range(n):
        a.append(int(input().strip()))
    up = 1

    sort(a, n, up)
    print("\n\nSorted array is")
    for i in range(n):
        print("%d" % a[i])
