#!/bin/env python3
# Python program for implementation of Radix Sort
# Modified by CoolCat467

__version__ = '0.1.0'

def radix_sort(lst):
    sort = data
    origmax = max(sort)
    exp = 1
    while origmax/exp > 0:
        arr = list(sort)
        n = len(arr)
        output = [0] * (n)
        count = [0] * (10)
        for i in range(0, n):
            index = (arr[i]/exp)
            count[int((index)%10)] += 1
        
        for i in range(1,10):
            count[i] += count[i-1]
        i = n-1
        while i>=0:
            index = (arr[i]/exp)
            output[count[int((index)%10)] - 1] = arr[i]
            count[int((index)%10)] -= 1
            i -= 1
        i = 0
        for i in range(0,len(arr)):
            arr[i] = output[i]
        sort = arr
        exp *= 10
    return sort
