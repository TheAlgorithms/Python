from __future__ import print_function

def bubble_sort(arr):
  n = len(arr)
  # Traverse through all array elements
  for i in range(n):
    # Last i elements are already in place
      for j in range(0, n-i-1):
        # traverse the array from 0 to n-i-1
        # Swap if the element found is greater
        # than the next element
        if arr[j] > arr[j+1] :
              arr[j], arr[j+1] = arr[j+1], arr[j]
  return arr
 
if __name__ == '__main__':
    try:
        raw_input          # Python 2
    except NameError:
        raw_input = input  # Python 3
    user_input = raw_input('Enter numbers separated by a comma:').strip()
    unsorted = [int(item) for item in user_input.split(',')]
    print(*bubble_sort(unsorted), sep=',')
