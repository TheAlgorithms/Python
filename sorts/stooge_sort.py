def stooge_sort(arr):
    """
    >>> arr = [2, 4, 5, 3, 1]
    >>> stooge_sort(arr)
    >>> print(arr)
    [1, 2, 3, 4, 5]
    """
    stooge(arr,0,len(arr)-1)

    
def stooge(arr, i, h):


    if i >= h:
        return
  
    # If first element is smaller than the last then swap them
    if arr[i]>arr[h]:
        arr[i], arr[h] = arr[h], arr[i]
  
    # If there are more than 2 elements in the array
    if h-i+1 > 2: 
        t = (int)((h-i+1)/3)
  
        # Recursively sort first 2/3 elements
        stooge(arr, i, (h-t))
  
        # Recursively sort last 2/3 elements
        stooge(arr, i+t, (h))
  
        # Recursively sort first 2/3 elements
        stooge(arr, i, (h-t))

        
