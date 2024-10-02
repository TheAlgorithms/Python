"""
Given an array of both positive and negative integers, the task is to compute sum of minimum and maximum elements of all sub-array of size k.

https://www.geeksforgeeks.org/sum-minimum-maximum-elements-subarrays-size-k/
"""

#this function will return sum of min and max of the window
def get_min_max(array:list ,start:int ,end:int) -> int:
    
    max = min = array[start]
    
    for i in range(start+1,end+1):
        if array[i] < min:
            min = array[i]
        if array[i] > max:
            max = array[i]
    
    return max+min

def sum(array:list ,size:int ,k:int) -> int:
    """
    Args:
        array (list): the input array
        size (int): size of the array
        k (int): size of the sub-array
    
    Returns:
        int : sum of the minimum and maximum elements of all sub-arrays of size-k
    """
    
    # create first window of size k
    start ,end = 0 ,k-1
    result = 0
    #get the minimum and maximum element from the window and add it to the result
    result += get_min_max(array,size,start,end)
    
    
    while start < size-k and end < size:
        start += 1
        end += 1
        result += get_min_max(array,start,end)
    
    return result

if __name__ == '__main__':
    array = [2, 5, -1, 7, -3, -1, -2]
    K = 4
    size = 7
    print(sum(array,size,K))