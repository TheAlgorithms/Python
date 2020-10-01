def mergeSort(array):
    """
    >>> mergeSort([3, 2, 1])
    [1, 2, 3]
    >>> mergeSort([3, 2, 1, 0, 1, 2, 3, 5, 4])
    [0, 1, 1, 2, 2, 3, 3, 4, 5]
    >>> mergeSort([10])
    [10]
    """
    if len(array) == 1:
        return array

    middle = len(array) // 2

    # Split the array into halves till the array length becomes equal to One
    # merge the arrays of single length returned by mergeSort function and
    # pass them into the merge arrays function which merges the array
    leftHalf = array[:middle]
    rightHalf = array[middle:]

    return mergeArrays(mergeSort(leftHalf), mergeSort(rightHalf))


def mergeArrays(leftHalf, rightHalf):
    sortedArray = [None] * (len(rightHalf) + len(leftHalf))

    pointer1 = 0  # pointer to current index for left Half
    pointer2 = 0  # pointer to current index for the right Half
    index = 0  # pointer to current index for the sorted array Half

    while pointer1 < len(leftHalf) and pointer2 < len(rightHalf):
        if leftHalf[pointer1] < rightHalf[pointer2]:
            sortedArray[index] = leftHalf[pointer1]
            pointer1 += 1
            index += 1
        else:
            sortedArray[index] = rightHalf[pointer2]
            pointer2 += 1
            index += 1
    while pointer1 < len(leftHalf):
        sortedArray[index] = leftHalf[pointer1]
        pointer1 += 1
        index += 1

    while pointer2 < len(rightHalf):
        sortedArray[index] = rightHalf[pointer2]
        pointer2 += 1
        index += 1

    return sortedArray


if __name__ == "__main__":
    import doctest

    doctest.testmod()
