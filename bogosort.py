def bogo_sort(arr):
    """
    Bogo sort is a highly inefficient sorting algorithm based on the generate and test paradigm. 
    The algorithm successively generates permutations of its input until it finds one that is sorted.
    """
    while not all(arr[i] <= arr[i+1] for i in range(len(arr)-1)):
        random.shuffle(arr)
    return arr
