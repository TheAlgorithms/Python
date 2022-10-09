import doctest


def find_anagrams(_list: list) -> list[list[str]]:
    test_find_anagrams()
    """
    Find the characters and number of occurrence in each words
    """
    char_map = {}
    anagrams = []
    for each in _list:
        char_map[each] = {}
        char_map[each]["is_visited"] = False
        for char in each:
            # if the letter is not present already add it
            # if it is already present add the count of each letter
            if char not in char_map[each]:
                char_map[each][char] = 1
            else:
                char_map[each][char] += 1

    """
    Match each words with the occurrence count
    """
    _keys = list(char_map)
    for itr1 in range(0, len(_keys)):
        # One word is taken at a time
        res = []
        for itr2 in range(itr1 + 1, len(_keys)):
            # now the character count of each work is compared with the main word
            # if the character count is matched it is considered as an anagram
            if char_map[_keys[itr1]] == char_map[_keys[itr2]] and not char_map[_keys[itr2]]["is_visited"]:
                res.append(_keys[itr1])
                res.append(_keys[itr2])
                # once the word is compared and match is found it is marked as visited
                char_map[_keys[itr2]]["is_visited"] = True
        # now sort the words and remove the duplicates if present
        _set = sorted(set(res))

        # if there are anagrams, push it to the res array
        if len(_set) != 0:
            anagrams.append(_set)
        # if there are no anagrams found return []
    return anagrams


def test_find_anagrams() -> None:
    """
    Determine whether the list can be grouped into anagrams
    >>> input = ['could', 'cloud', 'grips', 'hello', 'parts', 'prigs', 'strap', 'traps']
    >>> find_anagrams(input)
    [['cloud', 'could'], ['grips', 'prigs'], ['parts', 'strap', 'traps']]
    >>> find_anagrams(['could', 'arena'])
    []
    """


if __name__ == "__main__":
    doctest.testfile("group_anagram.txt")
    test_find_anagrams()
