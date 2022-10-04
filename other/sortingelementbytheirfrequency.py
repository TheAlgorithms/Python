# Please uncomment the file before running


# method 1 (long method)
# def sortingelebyfreq(arr):
#   d = {}
#   narr = []
#   for i in arr:
#       if i not in d:
#           d[i] = 1
#       else:
#           d[i] += 1
# #   print(d)
#   d = dict(sorted(d.items(), key=lambda item: item[1], reverse=True))
# #   print(d)
#   for key, values in d.items():
#       while values >= 1:
#           narr.append(key)
#           values -= 1
#   return narr


# method 2 (easy method) using built in function
# from collections import Counter


# def sortingelebyfreq(arr):
#   counter = Counter(arr)
#   return sorted(arr, key = lambda x: (-counter[x],x))


# method 3 (one liner)
def sortingelebyfreq(arr):
  return sorted(arr, key = arr.count, reverse = True)


# main function
if __name__ == "__main__":
  arr = [1,2,2,6,5]
  print(sortingelebyfreq(arr))
