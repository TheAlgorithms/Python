# Python program to impleament cycle sort 
  
def cycleSort(array): 
  writes = 0
    
  # Loop through the array to find cycles to rotate. 
  for cycleStart in range(0, len(array) - 1): 
    item = array[cycleStart] 
      
    # Find where to put the item. 
    pos = cycleStart 
    for i in range(cycleStart + 1, len(array)): 
      if array[i] < item: 
        pos += 1
      
    # If the item is already there, this is not a cycle. 
    if pos == cycleStart: 
      continue
      
    # Otherwise, put the item there or right after any duplicates. 
    while item == array[pos]: 
      pos += 1
    array[pos], item = item, array[pos] 
    writes += 1
      
    # Rotate the rest of the cycle. 
    while pos != cycleStart: 
        
      # Find where to put the item. 
      pos = cycleStart 
      for i in range(cycleStart + 1, len(array)): 
        if array[i] < item: 
          pos += 1
        
      # Put the item there or right after any duplicates. 
      while item == array[pos]: 
        pos += 1
      array[pos], item = item, array[pos] 
      writes += 1
    
  return writes 
    
#  driver code  
arr = [1, 8, 3, 9, 10, 10, 2, 4 ] 
n = len(arr)  
cycleSort(arr) 
  
print("After sort : ") 
for i in range(0, n) :  
    print(arr[i], end = \' \') 
