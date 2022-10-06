def sort_by_datatype(array: list) -> None:
    """
    Inplace sorting of an heterogenous (str,int,float) list with numbers on the
    left side of the array and strings on the right side of the array (default)
    Parameters
        array : 1D array of items of types int, float and/or str
    >>> a1 = ['sharron', 1, 0, 5, 'querry']
    >>> sort_by_datatype(a1)
    >>> a1
    [0, 1, 5, 'querry', 'sharron']
    >>> a2 = [4,9,'50','ant',3,6]
    >>> sort_by_datatype(a2)
    >>> a2
    [3, 4, 6, 9, '50', 'ant']
    >>> a3 = ['c','a','z','a']
    >>> sort_by_datatype(a3)
    >>> a3
    ['a', 'a', 'c', 'z']
    """

    valid_types = {int, float, str}
    i, j = 0, len(array) - 1
    while i <= j:  # Put numbers on the left side and strings on the right
        if (type(array[i]) not in valid_types) or (type(array[j]) not in valid_types):
            raise TypeError("Function supports only str, int and float data types")

        if type(array[i]) == str:
            if type(array[j]) != str:
                array[i], array[j] = array[j], array[i]
                i += 1
            j -= 1
        else:
            if type(array[j]) == str:
                j -= 1
            i += 1

    for i in range(len(array)):  # Sort the list in-place
        for j in range(i + 1, len(array)):
            if type(array[i]) != str and type(array[j]) == str:
                break
            if array[i] > array[j]:
                array[i], array[j] = array[j], array[i]

    return


if __name__ == "__main__":
    sort_by_datatype([(1, 2), "2", "15", 1, 0])  # TypeError
