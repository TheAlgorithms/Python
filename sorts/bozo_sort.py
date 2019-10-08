"""
Bozo sort consists out of checking if the input sequence is sorted and if not swapping randomly two elements.
This is repeated until eventually the sequence is sorted.
Takes in an array of numbers and provides a sorted array.
It may take O(infinity) at worst case as upper limit is not defined and best case will be O(1) when the array is sorted.
Since on average, it may take n! permutations, its average complexity is considered O(n!)
"""


import random

def sort_check(array):
    for i in range(0,len(array)-1):
        if array[i]>array[i+1]:
            return False
    return True
def bozo_sort(array):
    while not sort_check(array):
        i,j=random.randint(0,len(array)-1),random.randint(0,len(array)-1)
        array[i],array[j]=array[j],array[i]
    return array

n=int(input('Enter Size of Array: '))
arr=[input('Enter Element %d : '%(i+1)) for i in range(n)]

print ('Original Array : ',arr)
print ('Sorted Array : ',bozo_sort(arr))
