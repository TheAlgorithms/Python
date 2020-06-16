#!/usr/bin/env python

"""Illustrate how to implement bucket sort algorithm."""

# Author: OMKAR PATHAK
# This program will illustrate how to implement bucket sort algorithm

# Wikipedia says: Bucket sort, or bin sort, is a sorting algorithm that works
# by distributing the elements of an array into a number of buckets.
# Each bucket is then sorted individually, either using a different sorting
# algorithm, or by recursively applying the bucket sorting algorithm. It is a
# distribution sort, and is a cousin of radix sort in the most to least
# significant digit flavour.
# Bucket sort is a generalization of pigeonhole sort. Bucket sort can be
# implemented with comparisons and therefore can also be considered a
# comparison sort algorithm. The computational complexity estimates involve the
# number of buckets.

#  Time Complexity of Solution:
#  Worst case scenario occurs when all the elements are placed in a single bucket. The
# overall performance would then be dominated by the algorithm used to sort each bucket.
# In this case, O(n log n), because of TimSort
#
#  Average Case O(n + (n^2)/k + k), where k is the number of buckets
#
#  If k = O(n), time complexity is O(n)

DEFAULT_BUCKET_SIZE = 5


def bucket_sort(my_list, bucket_size=DEFAULT_BUCKET_SIZE):
    if len(my_list) == 0:
        raise Exception("Please add some elements in the array.")

    min_value, max_value = (min(my_list), max(my_list))
    bucket_count = (max_value - min_value) // bucket_size + 1
    buckets = [[] for _ in range(int(bucket_count))]

    for i in range(len(my_list)):
        buckets[int((my_list[i] - min_value) // bucket_size)].append(my_list[i])

    return sorted(
        [buckets[i][j] for i in range(len(buckets)) for j in range(len(buckets[i]))]
    )


if __name__ == "__main__":
    user_input = input("Enter numbers separated by a comma:").strip()
    unsorted = [float(n) for n in user_input.split(",") if len(user_input) > 0]
    print(bucket_sort(unsorted))
