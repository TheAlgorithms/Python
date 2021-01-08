# You have given some element with its weight in an array, you task is to find the minimum possible weight element and print the weight.
# You can combine two elements and the resultant element will be the absoulte difference of the weight of these two elements.

def minElement(arr):
  global min, count

  if len(arr) == 1:
    return min

  if(min == 0):
    return min
    
  for i in range(0, len(arr) - 1):
    for j in range(i + 1, len(arr)):
      count = count + 1
      temp = arr.copy()
      temp.pop(j)
      temp.pop(i)
      temp.append(abs(arr[i] - arr[j]))
      if min > abs(arr[i] - arr[j]):
        min = abs(arr[i] - arr[j])
        if min == 0:
          return min
      minElement(temp)

  return min


if __name__ == "__main__":
    min = 0
    count = 0
    arr = [100, 90, 19, 88, 95]
    min = arr[0] + 1
    print("Ans -> ", minElement(arr))
