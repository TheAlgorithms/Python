"""
This is a non-parallelized implementation of odd-even transpostiion sort.

Normally the swaps in each set happen simultaneously, without that the algorithm
is no better than bubble sort.
"""


def OddEvenTransposition(arr):
    for i in range(0, len(arr)):
        for i in range(i % 2, len(arr) - 1, 2):
            if arr[i + 1] < arr[i]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
        print(*arr)

    return arr


# creates a list and sorts it
def main():
    list = []

    for i in range(10, 0, -1):
        list.append(i)
    print("Initial List")
    print(*list)

    list = OddEvenTransposition(list)

    print("Sorted List\n")
    print(*list)


if __name__ == "__main__":
    main()
