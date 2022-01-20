# Python Program to search an element
# in a sorted and pivoted array


# sorted array arr[] of size n 
def pivoted_binary_search(arr, n, key) -> int:
    """Searches an element key in a pivoted
        Parameters
        ----------
        arr :
            Array to use.
        n : 
            Size of arr.
        key :
            Pivot value.
        Returns
        ---------
        int :
         Element of the array.
    
    """
    
    pivot = find_pivot(arr, 0, n-1);

    # If we didn't find a pivot, 
    # then array is not rotated at all
    if pivot == -1:
        return binary_search(arr, 0, n-1, key);

    # If we found a pivot, then first
    # compare with pivot and then
    # search in two subarrays around pivot
    if arr[pivot] == key:
        return pivot
    if arr[0] <= key:
        return binary_search(arr, 0, pivot-1, key);
    return binarys_earch(arr, pivot + 1, n-1, key);


# Function to get pivot. For array 
# 3, 4, 5, 6, 1, 2 it returns 3 
# (index of 6) 
def find_pivot(arr, low, high) -> int:
   """Searches an element key in a pivoted
        Parameters
        ----------
        arr :
            Array to use.
        low : 
            Low value.
        high:
            High value.
        Returns
        ---------
        int:
            Element of the array.
    
    """
    
    # base cases
    if high < low:
        return -1
    if high == low:
        return low
    
    # low + (high - low)/2;
    mid = int((low + high)/2)
    
    if mid < high and arr[mid] > arr[mid + 1]:
        return mid
    if mid > low and arr[mid] < arr[mid - 1]:
        return (mid-1)
    if arr[low] >= arr[mid]:
        return find_pivot(arr, low, mid-1)
    return find_pivot(arr, mid + 1, high)

# Standard Binary Search function*/
def binary_search(arr, low, high, key) -> int:
    """Binary search
        ----------
        arr :
            Array to use.
        low : 
            Low value
        high :
            High value
        key : 
            value were looking for.
        
        Returns
        ---------
         int   
            Element of the array.
    
    """
    if high < low:
        return -1
        
    # low + (high - low)/2;    
    mid = int((low + high)/2)
    
    if key == arr[mid]:
        return mid
    if key > arr[mid]:
        return binary_search(arr, (mid + 1), high,
                                            key);
    return binary_search(arr, low, (mid -1), key);
