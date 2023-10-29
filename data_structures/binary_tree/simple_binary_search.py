"""This binary search tree searchs through a set list of integers for chosen integer"""


def binary_search(alist, start, end, key):
    if not start < end:
        return -1

    mid = (start + end) // 2
    if alist[mid] < key:
        return binary_search(alist, mid + 1, end, key)
    elif alist[mid] > key:
        return binary_search(alist, start, mid, key)
    else:
        return mid


alist = [
    "2",
    "4",
    "6",
    "8",
    "10",
    "12",
    "14",
    "16",
    "18",
    "20",
    "22",
    "24",
    "26",
    "28",
    "30",
    "32",
    "34",
    "36",
    "38",
    "40",
    "42",
    "44",
    "46",
    "48",
    "50",
]
alist = [int(x) for x in alist]
key = int(input("The number to search for: "))

index = binary_search(alist, 0, len(alist), key)
if index < 0:
    print("{} was not found.".format(key))
else:
    print("{} was found at index {}.".format(key, index))
