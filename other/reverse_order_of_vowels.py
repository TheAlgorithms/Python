"""
Given a string 'S' reverse the vowels order in that string. return the modified string where the position
of constants are static and vowels got reversed.

You may assume that each input would have exactly one solution, if there are no vowels return the input.

Example:
>>> S = 'hello programming'
>>> reverse_vowels(S)
'hilla progrommeng'
"""
import doctest

def is_vowel(char: str) -> bool:
    """
        returns True if the character is vowel else False
        >>> is_vowel('A')
        True
        >>> is_vowel('e')
        True
        >>> is_vowel('f')
        False
    """
    vowels = ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']
    # Check for empty string
    if(not char):
        return False
    return (char[0] in vowels)


def get_vowels(string: str) -> list:
    """
        Given a string returns vowels from it

        >>> get_vowels('abcde')
        ['a', 'e']
        >>> get_vowels('AEIou')
        ['A', 'E', 'I', 'o', 'u']
        >>> get_vowels('bCFM')
        []
    """
    vowels = list()

    index = 0
    length = len(string)

    while index < length:
        if(is_vowel(string[index])):
            vowels.append(string[index])
        index += 1

    return vowels

def reverse_vowels(string: str) -> str:
    """
        Reverses the order of vowels in the given string
        
        >>> reverse_vowels('Hello World')
        'Hollo Werld'
        >>> reverse_vowels('Algo & DS')
        'olgA & DS'
        >>> reverse_vowels('why')
        'why'
    """
    vowels = get_vowels(string)
    answer = ""

    index = 0
    length = len(string)

    while index < length:
        if(is_vowel(string[index])):
            answer = answer + vowels.pop()
        else:
            answer = answer + string[index]
        index += 1

    return answer

if __name__ == "__main__":
    doctest.testmod()

    print(f"{ reverse_vowels('hello programming') }")
