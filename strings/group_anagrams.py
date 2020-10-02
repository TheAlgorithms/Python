"""
wiki: https://en.wikipedia.org/wiki/Anagram
"""


from collections import defaultdict


def modify_word_and_get_offset(word: str, alphabet: int) -> tuple:
    """ If alphabet is 26 meaning case sensitive feature is off, the string is 
        converted to lowercase and the offset is set to 0
    """
    return (word.lower(), 0) if alphabet == 26 else (word, 25)


def get_key(word: str, alphabet: int) -> tuple:
    """ If case sensitive feature is on, then the alphabet size is 52 : A-Z, a-z (26+26=52).
        For case sensitive feature, first 26 positions are for uppercase characters and next 
        26 positions are for lowercase characters. So `offset` denotes that if case sensitive 
        feaure is on, then the lower case characters will be shifted 26 positions from the 
        starting of the `alphabet_list`. If you are wondering why is that, it's because 
        `ord('A')-ord('A') and ord('a') - ord('a')` gives the same value.
    """
    alphabet_lists = [0 for i in range(alphabet)]
    word, offset = modify_word_and_get_offset(word, alphabet)

    for char in word:
        if char.isupper():
                alphabet_lists[ord(char) - ord('A')] += 1
        else:
            alphabet_lists[ord(char) - ord('a') + offset] += 1

    return tuple(alphabet_lists)


def group_anagrams(words: str, case_sensitive=False) -> list:
    """
    A list of strings `words` is given. Group the strings as anagram together. 
    >>> group_anagrams(['cat', 'bat', 'nat', 'tac', 'tab'], False)
    [['cat', 'tac'], ['bat', 'tab'], ['nat']]
    >>> group_anagrams(['a'], False)
    [['a']]
    >>> group_anagrams([''], False)
    [['']]

    By default all the strings will be in lower case. If you want uppercase sensitive feature, 
    pass an optional parameter `case_sensitive` with the value `True`. Default value of `case_sensitive` 
    is False. So `cat` and `cAt` will be treated as the same strings.

    >>> group_anagrams(['cat', 'cAt', 'nat', 'Nat', 'tac'], True)
    [['cat', 'tac'], ['cAt'], ['nat'], ['Nat']]
    """
    anagram_lists = defaultdict(list)

    for word in words:
        alphabet = 26 if not case_sensitive else 52
        
        key = get_key(word, alphabet)
        anagram_lists[key].append(word)

    return [anagrams for anagrams in anagram_lists.values()]


def is_case_sensitive(case_sensitive: str) -> bool:
    return case_sensitive == 'y' or case_sensitive == "Y"


if __name__ == "__main__":
    from doctest import testmod

    testmod()
    words = input("Enter the strings ").strip().split(' ')
    case_sensitive = input("Do you want case sensitive feature in the Anagram? y/n: ").strip()

    ans = group_anagrams([word for word in words], is_case_sensitive(case_sensitive))
    print(f"Group Anagrams lists {ans}")
