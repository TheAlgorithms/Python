def merge(arr, left, mid, right): 
    # overall array will divided into 2 array
    # l contain left portion of array from left to mid of array
    # r contain right portion of array from mid+1 to till last of array
    l = arr[left : mid + 1]  # noqa: E741
    r = arr[mid + 1 : right + 1]
    k = left
    i = 0
    j = 0
    while i < len(l) and j < len(r):
        # change sign for Descending order
        if l[i] < r[j]:
            arr[k] = l[i]
            i += 1
        else:
            arr[k] = r[j]
            j += 1
        k += 1
    while i < len(l):
        arr[k] = l[i]
        i += 1
        k += 1
    while j < len(r):
        arr[k] = r[j]
        j += 1
        k += 1
    return arr


def mergesort(arr, left, right):
    """
    >>> mergesort([3,2,1],0,2)
    [1, 2, 3]
    >>> mergesort([3,2,1,0,1,2,3,5,4],0,8)
    [0, 1, 1, 2, 2, 3, 3, 4, 5]
    """
    if left < right:
        mid = (left + right) // 2
        # print("ms1",a,b,m)
        mergesort(arr, left, mid)
        # print("ms2",a,m+1,e)
        mergesort(arr, mid + 1, right)
        # print("m",a,b,m,e)
        merge(arr, left, mid, right)
        return arr


if __name__ == "__main__":
    import doctest

    doctest.testmod()
