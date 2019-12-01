def double_sort(lst):
    """this sorting algorithm sorts an array using the principle of bubble sort , 
    but does it both from left to right and right to left , 
    hence i decided to call it "double sort"
    :param collection: mutable ordered sequence of elements
    :return: the same collection in ascending order
    Examples:
    >>> double_sort([-1 ,-2 ,-3 ,-4 ,-5 ,-6 ,-7])
    [-7, -6, -5, -4, -3, -2, -1]
    >>> double_sort([])
    []
    >>> double_sort([-1 ,-2 ,-3 ,-4 ,-5 ,-6])
    [-6, -5, -4, -3, -2, -1]
    >>> double_sort([-3, 10, 16, -42, 29]) == sorted([-3, 10, 16, -42, 29])
    True
    """
    no_of_elements = len(lst)
    for i in range(
        0, int(((no_of_elements - 1) / 2) + 1)
    ):  # we dont need to traverse to end of list as
        for j in range(0, no_of_elements - 1):
            if (
                lst[j + 1] < lst[j]
            ):  # applying bubble sort algorithm from left to right (or forwards)
                temp = lst[j + 1]
                lst[j + 1] = lst[j]
                lst[j] = temp
            if (
                lst[no_of_elements - 1 - j] < lst[no_of_elements - 2 - j]
            ):  # applying bubble sort algorithm from right to left (or backwards)
                temp = lst[no_of_elements - 1 - j]
                lst[no_of_elements - 1 - j] = lst[no_of_elements - 2 - j]
                lst[no_of_elements - 2 - j] = temp
    return lst


if __name__ == "__main__":
    print("enter the list to be sorted")
    lst = [int(x) for x in input().split()]  # inputing elements of the list in one line
    sorted_lst = double_sort(lst)
    print("the sorted list is")
    print(sorted_lst)
