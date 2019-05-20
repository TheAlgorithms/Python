#!/usr/bin/env python
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

DEFAULT_BUCKET_SIZE=5
def bucket_sort(my_list,bucket_size=DEFAULT_BUCKET_SIZE):
    if(my_list==0):
        print("you don't have any elements in array!")


    min_value=min(my_list)
    max_value=max(my_list)

    bucket_count=(max_value-min_value)//bucket_size+1
    buckets=[]
    for i in range(bucket_count):
        buckets.append([])
    for i in range(len(my_list)):
        buckets[(my_list[i]-min_value)//bucket_size].append(my_list[i])


    sorted_array=[]
    for i in range(len(buckets)):
        buckets[i].sort()
        for j in range(len(buckets[i])):
            sorted_array.append(buckets[i][j])
    return sorted_array




#test
#best on python 3.7.3
user_input =input('Enter numbers separated by a comma:').strip()
unsorted =[int(item) for item in user_input.split(',')]
print(bucket_sort(unsorted))
