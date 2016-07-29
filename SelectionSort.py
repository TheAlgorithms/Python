def selectionsort( aList ):
  for i in range( len( aList ) ):
    least = i
    for k in range( i + 1 , len( aList ) ):
      if aList[k] < aList[least]:
        least = k
 
    aList = swap( aList, least, i )
  print(aList)
 
def swap( A, x, y ):
  tmp = A[x]
  A[x] = A[y]
  A[y] = tmp
  return A

print ("Enter numbers seprated by comma ")
response = input()
aList = [int(item) for item in (response.split(','))]
selectionsort(aList)
