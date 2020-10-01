import statistics


def mode(input_list):  # Defining function "mode."
    """This function returns the mode(Mode as in the measures of
    central tendency) of the input data.

    The input list may contain any Datastructure or any Datatype.

    >>> input_list = [2, 3, 4, 5, 3, 4, 2, 5, 2, 2, 4, 2, 2, 2]
    >>> mode(input_list)
    2
    >>> input_list = [2, 3, 4, 5, 3, 4, 2, 5, 2, 2, 4, 2, 2, 2]
    >>> mode(input_list) == statistics.mode(input_list)
    True
    """
    # Copying input_list to check with the index number later.
    check_list = input_list.copy()
    result = list()  # Empty list to store the counts of elements in input_list
    for x in input_list:
        result.append(input_list.count(x))
        input_list.remove(x)
        y = max(result)  # Gets the maximum value in the result list.
        # Returns the value with the maximum number of repetitions.
        return check_list[result.index(y)]


if __name__ == "__main__":
    data = [2, 3, 4, 5, 3, 4, 2, 5, 2, 2, 4, 2, 2, 2]
    print(mode(data))
    print(statistics.mode(data))
