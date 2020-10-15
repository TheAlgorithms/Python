def merge(left_list, right_list, aux_array):
  i = 0
  j = 0
  k = 0

  while i < len(left_list) and j < len(right_list):

      if left_list[i] < right_list[j]:
          aux_array[k]=left_list[i]
          i += 1
      else:
          aux_array[k]=right_list[j]
          j += 1
      k += 1

  while i < len(left_list):

      aux_array[k]=left_list[i]
      i += 1
      k += 1

  while j < len(right_list):
      aux_array[k]=right_list[j]
      j += 1
      k += 1


def merge_sort(array, aux_array=[]):
  if len(array) > 1:

    half = len(array)//2

    left_list = array[:half]
    right_list = array[half:]

    merge_sort(left_list, array)
    merge_sort(right_list, array)
    merge(left_list,right_list, array)

numbers = [100,55,80,20,15,98,76,500,480]

merge_sort(numbers)
print(numbers)
