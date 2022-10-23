"""For reference
https://en.wikipedia.org/wiki/Odd%E2%80%93even_sort
"""


def odd_even_sort(input_list: list) -> list:
    """this algorithm uses the same idea of bubblesort,
    but by first dividing in two phase (odd and even).
    Originally developed for use on parallel processors
    with local interconnections.
    :param collection: mutable ordered sequence of elements
    :return: same collection in ascending order
    Examples:
    >>> odd_even_sort([5 , 4 ,3 ,2 ,1])
    [1, 2, 3, 4, 5]
    >>> odd_even_sort([])
    []
    >>> odd_even_sort([-10 ,-1 ,10 ,2])
    [-10, -1, 2, 10]
    >>> odd_even_sort([1 ,2 ,3 ,4])
    [1, 2, 3, 4]
    """
    is_sorted = False
    while is_sorted is False:  # Until all the indices are traversed keep looping
        is_sorted = True
        for i in range(0, len(input_list) - 1, 2):  # iterating over all even indices
            if input_list[i] > input_list[i + 1]:

                input_list[i], input_list[i + 1] = input_list[i + 1], input_list[i]
                # swapping if elements not in order
                is_sorted = False

        for i in range(1, len(input_list) - 1, 2):  # iterating over all odd indices
            if input_list[i] > input_list[i + 1]:
                input_list[i], input_list[i + 1] = input_list[i + 1], input_list[i]
                # swapping if elements not in order
                is_sorted = False
    return input_list


if __name__ == "__main__":
    print("Enter list to be sorted")
    input_list = [int(x) for x in input().split()]
    # inputing elements of the list in one line
    sorted_list = odd_even_sort(input_list)
    print("The sorted list is")
    print(sorted_list)
