"""Implementation of a double-linear-search,
which iterates through the array from both sides: start and end."""


def double_linear_search(array: list, search_item: int) -> int:
    """:param array: the array to be searched
       :param search_item: the item to be searched
       :returns index of search_item, if search_item is in array, else -1

       Examples:

       >>> double_linear_search([1, 5, 5, 10], 5)
       1

       >>> double_linear_search([1, 5, 5, 10], 100)
       -1

       >>> double_linear_search([1, 5, 5, 10], 10)
       3
       """

    # define the start and end index of the given array
    start_ind, end_ind = 0, len(array) - 1

    while start_ind <= end_ind:

        if array[start_ind] == search_item:
            return start_ind
        elif array[end_ind] == search_item:
            return end_ind

        else:
            # increase start_ind, decrease end_ind
            start_ind += 1
            end_ind -= 1

    # returns -1 if the element x is not found in the given array
    return -1


if __name__ == "__main__":
    """
    Change ARRAY_LENGTH to a number you want to generate an example array,
    which goes up to the number you define:
    ARRAY_LENGTH = 50 --> [0, 1, 2, ..., 49, 50]
    """
    # change for bigger/smaller arrays
    ARRAY_LENGTH = 100
    
    # should be at index 40
    search_item = 40

    # this creates an array, which goes up to the number
    # ARRAY_LENGTH --> [0, 1, ... , 99, 100]
    array = [x for x in range(ARRAY_LENGTH + 1)]

    print(double_linear_search(array, search_item))
