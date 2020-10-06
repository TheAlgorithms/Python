# binary insertion sort
def insertion_sort(arr):
   for i in range(1, len(arr)):
      temp = arr[i]
      pos = binary_search(arr, temp, 0, i) + 1
      for k in range(i, pos, -1):
         arr[k] = arr[k - 1]
      arr[pos] = temp
    
def binary_search(arr, key, start, end):
   if end - start <= 1:
      if key < arr[start]:
         return start - 1
      else:
         return start
   mid = (start + end)//2
   if arr[mid] < key:
      return binary_search(arr, key, mid, end)
   elif arr[mid] > key:
      return binary_search(arr, key, start, mid)
   else:
      return mid

# main function
arr =[]
n = int(input("Enter the number of elements "))
for i in range(0, n):
    j = int(input())
    arr.append(j)

insertion_sort(arr)
print("Sorted array is:")
for i in range(n):
   print(arr[i],end=" ")
