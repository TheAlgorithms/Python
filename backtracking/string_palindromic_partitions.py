def is_palindrome(word: str, start_index: int, end_index: int) -> bool:
    """
    This function checks if a given string is palindromic between two indices

    >>> is_palindrome("racecar", 0, 6)
    True

    >>> is_palindrome("racecar", 2, 6)
    False

    >>> is_palindrome("github", 0, 5)
    False

    :param word: current word to be checked
    :param start_index: first index of word from which palindrome check should begin
    :param end_index: last index of word at which palindrome check should end
    :return: returns True if substring between start_index and end_index is palindrome
    , False otherwise
    """
    while start_index < end_index:
        if word[start_index] != word[end_index]:
            return False
        start_index += 1
        end_index -= 1
    return True


def find_palindrome_partitions(
    word: str, start: int, end: int, result: list, current_result: list
):
    """
    This functions recursively separates the input word into segments and checks if the
    segment forms a palindrome.
    If the segment forms a palindrome, it stores the current segment into the solution
    list and recursively segregates the remaining string.
    If the segment doesn't form a palindrome, a character is appended to the existing
    segment and the above steps repeat.

    :param current_result: stores the palindromic partitions till this point
    :param result: stores the list of valid partitions of the input word
    :param end: the last index of the word
    :param start: the first index of current partition
    :param word: the input word to be partitioned
    :return: None
    """
    if start > end:
        result.append(current_result.copy())
        return

    for index in range(start, end + 1):
        if is_palindrome(word, start, index):
            current_result.append(word[start : index + 1])
            find_palindrome_partitions(word, index + 1, end, result, current_result)
            current_result.remove(word[start : index + 1])


def get_palindrome_partitions(word: str) -> list:
    """
    This function prints the list of all the possible palindromic partitions

    >>> get_palindrome_partitions("madam")
    [['m', 'a', 'd', 'a', 'm'], ['m', 'ada', 'm'], ['madam']]

    >>> get_palindrome_partitions("github")
    [['g', 'i', 't', 'h', 'u', 'b']]

    :param word: input word for which the partitions need to be found
    :return: list of valid palindromic partitions
    """
    # storing all the possible partitions as a list
    result = []

    # passing the list by reference to update it with actual partitions
    find_palindrome_partitions(word, 0, len(word) - 1, result, [])

    # printing the list of all possible partitions
    return result


if __name__ == "__main__":
    """
    This program prints all possible palindromic partitions of a string.
    https://leetcode.com/problems/palindrome-partitioning/
    """
    import doctest

    doctest.testmod()

    # sample input words
    words = ["racecar", "code", "dummy"]

    # Printing results for each input word
    for input_word in words:
        print(get_palindrome_partitions(input_word))
