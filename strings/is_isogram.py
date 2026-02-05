"""
wiki: https://en.wikipedia.org/wiki/Heterogram_(literature)#Isograms
"""


def is_isogram(string: str) -> bool:
    """
    An isogram is a word or phrase in which no letter is repeated.
    Non-alphabetic characters are ignored.

    >>> is_isogram('Uncopyrightable')
    True
    >>> is_isogram('allowance')
    False
    >>> is_isogram('six-year-old')
    True
    >>> is_isogram('copy1')
    True
    """
    letters = [char.lower() for char in string if char.isalpha()]
    return len(letters) == len(set(letters))


if __name__ == "__main__":
    input_str = input("Enter a string ").strip()
    isogram = is_isogram(input_str)
    print(f"{input_str} is {'an' if isogram else 'not an'} isogram.")

   
