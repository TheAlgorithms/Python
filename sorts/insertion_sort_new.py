"""
This is a fast insertion sort algorithm in python 
which it's time complixity is less than other shared
algorithms.

Just run `insertion_sort` function to see the result.
"""

def insertion_sort(arr):
  for i in range(1, len(arr)):
      j = i - 1
      for k in range(i):
          if arr[i] < arr[j]:
              arr[i], arr[j] = arr[j], arr[i]
              i = i -1
              j = j - 1


"""Create a random list in order to test insertion sort algorithm"""
from random import shuffle
arr = list(range(2000))    #very huge list!
shuffle(arr)
insertion_sort(arr)
print(arr)
