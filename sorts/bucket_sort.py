# Author: OMKAR PATHAK
# This program will illustrate how to implement bucket sort algorithm

# Wikipedia says: Bucket sort, or bin sort, is a sorting algorithm that works by distributing the
# elements of an array into a number of buckets. Each bucket is then sorted individually, either using 
# a different sorting algorithm, or by recursively applying the bucket sorting algorithm. It is a
# distribution sort, and is a cousin of radix sort in the most to least significant digit flavour.
# Bucket sort is a generalization of pigeonhole sort. Bucket sort can be implemented with comparisons
# and therefore can also be considered a comparison sort algorithm. The computational complexity estimates
# involve the number of buckets.

#  Time Complexity of Solution:
#  Best Case O(n); Average Case O(n); Worst Case O(n)

from P26_InsertionSort import insertionSort
import math

DEFAULT_BUCKET_SIZE = 5

def bucketSort(myList, bucketSize=DEFAULT_BUCKET_SIZE):
    if(len(myList) == 0):
        print('You don\'t have any elements in array!')

    minValue = myList[0]
    maxValue = myList[0]

    # For finding minimum and maximum values
    for i in range(0, len(myList)):
        if myList[i] < minValue:
            minValue = myList[i]
        elif myList[i] > maxValue:
            maxValue = myList[i]

    # Initialize buckets
    bucketCount = math.floor((maxValue - minValue) / bucketSize) + 1
    buckets = []
    for i in range(0, bucketCount):
        buckets.append([])

    # For putting values in buckets
    for i in range(0, len(myList)):
        buckets[math.floor((myList[i] - minValue) / bucketSize)].append(myList[i])

    # Sort buckets and place back into input array
    sortedArray = []
    for i in range(0, len(buckets)):
        insertionSort(buckets[i])
        for j in range(0, len(buckets[i])):
            sortedArray.append(buckets[i][j])

    return sortedArray

if __name__ == '__main__':
    sortedArray = bucketSort([12, 23, 4, 5, 3, 2, 12, 81, 56, 95])
    print(sortedArray)
