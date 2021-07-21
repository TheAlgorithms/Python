def binarySearch(numList, left, right, target):
    
    """
    Binary search for the range of number found in the exponential search algorithm
    :param left: the first number in the range of number
    :param right: the last number in the range of number
    :param numList: a list of number sorted in ascending order
    :param target: a number to be searched in the list of number
    :return: index of target or None if target is not found
    """
    
    if left > right:
        return -1
    mid = (left + right) // 2
    if target == numList[mid]:
        return mid
    elif target < numList[mid]:
        return binarySearch(numList, left, mid - 1, target)
    else:
        return binarySearch(numList, mid + 1, right, target)
 
def exponentialSearch(numList, target):
    
    """
    Pure implementation of exponential search algorithm in Python
    :param numList: a list of number sorted in ascending order
    :param target: a number to be searched in the list of number
    :return: the result return by binary search which is the index of target
    in the list of number or None if item is not found
    Examples:
    >>> exponentialSearch([1, 2, 3, 4, 5], 1)
    >>> binarySearch([1, 2, 3, 4, 5], 0, 1, 1)
    0
    >>> exponentialSearch([1, 2, 3, 4, 5], 5)
    >>> binarySearch([1, 2, 3, 4, 5], 2, 4, 5)
    4
    >>> exponentialSearch([1, 2, 3, 4, 5], 2)
    >>> binarySearch([1, 2, 3, 4, 5], 1, 2, 2)
    1
    >>> exponentialSearch([1, 2, 3, 4, 5], 6)
    >>> binarySearch([1, 2, 3, 4, 5], 0, 1, 6)
    """
    
    index = 1
    #find range of number where target may be present
    while index < len(numList) and numList[index] < target:
        index *= 2
    #binary search using a range of number with the target
    return binarySearch(numList, index // 2, min(index, len(numList)), target)
 
 
# Exponential search algorithm
if __name__ == '__main__':
 
    userInput = input ("Enter numbers seperated by comma:\n").strip()
    numList = sorted(int(item) for item in userInput.split(","))
    target = int(input("Enter a number to be searched in the number list:\n"))
    index = exponentialSearch(numList, target)
    if index != -1:
        print("Element found at index", index)
    else:
        print("Element found not in the list")