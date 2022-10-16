# BUBBLE SORT
def bubblesort(customList):
    for i in range(len(customList) - 1):  # O(n)
        for j in range(len(customList) - i - 1):  # O(n)
            if customList[j] > customList[j + 1]:  # O(1)
                customList[j], customList[j + 1] = customList[j + 1], customList[j]
    print(customList)


# cList=[2,1,3,6,9,7,4,8,5]
# bubblesort(cList)

# SELECTION SORT
def selectionSort(customList):
    for i in range(len(customList)):
        min_index = i
        for j in range(i + 1, len(customList)):
            if customList[min_index] > customList[j]:
                min_index = j
        customList[i], customList[min_index] = customList[min_index], customList[i]
    print(customList)


# cList=[2,1,3,6,9,7,4,8,5]
# selectionSort(cList)


# INSERTION SORT


def insertionSort(customList):
    for i in range(1, len(customList)):
        key = customList[i]
        j = i - 1
        while j >= 0 and key < customList[j]:
            customList[j + 1] = customList[j]
            j -= 1
        customList[j + 1] = key
    return customList


# cList=[2,1,3,6,9,7,4,8,5]
# print(insertionSort(cList))

# BUCKET SORT

import math
from xmlrpc.server import MultiPathXMLRPCServer


def bucketSort(customList):
    numberofBuckets = round(math.sqrt(len(customList)))
    maxValue = max(customList)
    arr = []

    for i in range(numberofBuckets):
        arr.append([])
    for j in customList:
        index_b = math.ceil(j * numberofBuckets / maxValue)
        arr[index_b - 1].append(j)

    for i in range(numberofBuckets):
        arr[i] = insertionSort(arr[i])

    k = 0
    for i in range(numberofBuckets):
        for j in range(len(arr[i])):
            customList[k] = arr[i][j]
            k += 1
    return customList


# cList=[2,1,3,6,9,7,4,8,5]
# print(bucketSort(cList))


# MERGE SORT ALGORITHM


def merge(customList, l, m, r):
    n1 = m - l + 1
    n2 = r - m

    L = [0] * (n1)
    R = [0] * (n2)

    for i in range(0, n1):
        L[i] = customList[l + i]

    for j in range(0, n2):
        R[j] = customList[m + 1 + j]

    i = 0
    j = 0
    k = l
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            customList[k] = L[i]
            i += 1
        else:
            customList[k] = R[j]
            j += 1
        k += 1
    while i < n1:
        customList[k] = L[i]
        i += 1
        k += 1
    while j < n2:
        customList[k] = R[j]
        j += 1
        k += 1


# TIME COMPLEXITY : O(N)


def mergeSort(customList, l, r):
    if l < r:
        m = (l + (r - 1)) // 2
        mergeSort(customList, l, m)  # T(n/2)
        mergeSort(customList, m + 1, r)  # T(n/2)
        merge(customList, l, m, r)
    return customList


# cList=[2,1,3,6,9,7,4,8,5]
# print(mergeSort(cList ,0 ,8))


# QUICK SORT


def partition(customList, low, high):
    i = low - 1
    pivot = customList[high]
    for j in range(low, high):
        if customList[j] <= pivot:
            i += 1
            customList[i], customList[j] = customList[j], customList[i]
    customList[i + 1], customList[high] = customList[high], customList[i + 1]
    return i + 1


def quickSort(customList, low, high):
    if low < high:
        pi = partition(customList, low, high)  # O(n)
        quickSort(customList, low, pi - 1)  # T(n/2)
        quickSort(customList, pi + 1, high)  # T(n/2)
        # combined = O(N LogN)


# cList=[2,1,3,6,9,7,4,8,5]
# quickSort(cList ,0 ,8)
# print(cList)


# HEAP SORT ALGORITHM


def heapify(customList, n, i):
    smallest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and customList[l] < customList[smallest]:
        smallest = l
    if r < n and customList[r] < customList[smallest]:
        smallest = r
    if smallest != i:
        customList[i], customList[smallest] = customList[smallest], customList[i]
        heapify(customList, n, smallest)


def heapSort(customList):
    n = len(customList)
    for i in range(int(n / 2) - 1, -1, -1):
        heapify(customList, n, i)

    for i in range(n - 1, 0, -1):
        customList[i], customList[0] = customList[0], customList[i]
        heapify(customList, i, 0)
    customList.reverse()


cList = [2, 1, 3, 6, 9, 7, 4, 8, 5]
heapSort(cList)
print(cList)
