"""
Python implementation to find an alphabet in a list of 
alphabets using binary search algorithm and ASCII system

Time Complexity = O(log n)

For doctests run following command:
python3 -m doctest -v binary_search_alphabet.py

For manual testing run:
python3 binary_search_alphabet.py
"""


def binary_search_alphabet(array, target):
    """
    Locates the alphabet in a sorted array.

    Examples:
    >>> binary_search_alphabet(['a', 'b', 'z'], 'z')
    The alphabet (z) was found at position 2 in ['a', 'b', 'z'].

    >>> binary_search_alphabet(['x', 'y', 'z'], 'y')
    The alphabet (y) was found at position 1 in ['x', 'y', 'z'].

    """

    low = 0
    high = len(array) - 1

    target_in_ascii = ord(target)

    while high >= low:
        middle = low + (high - low) // 2  # ignore decimals by // operator
        item = array[middle]

        if item == target_in_ascii:
            return middle

        elif item > target_in_ascii:
            high = middle - 1

        else:
            low = middle + 1

    return None


if __name__ == "__main__":
    user_input = input(
        "Enter alphabets separated by comma(without spaces between): "
    ).strip()

    try:
        array = sorted(alphabet[0] for alphabet in user_input.split(","))
    except IndexError:
        """
        If user input ended with a comma => simply ignor the comma
        If user input empty              => prompt user
        """
        if len(user_input) > 0:
            if user_input[-1] == ",":
                array = sorted(alphabet[0] for alphabet in user_input.split(",")[:-1])
        else:
            print("Input error")

    array_in_ascii = [ord(alphabet) for alphabet in array]
    target = input("Enter an alphabet to search for in the list: ")[0]
    result = binary_search_alphabet(array_in_ascii, target)

    if result is None:
        print(f"The alphabet ({target}) was not found in {array}.")
    else:
        print(f"The alphabet ({target}) was found at position {result} in {array}.")