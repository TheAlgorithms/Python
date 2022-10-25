"""
An isogram is a word in which no letter is repeated. 
Examples of isograms are uncopyrightable and ambidextrously.
"""

def check_isogram(string: str) -> bool:
    """
    >>> check_isogram('uncopyrightable')
    True
    >>> check_isogram('allowance')
    False
    """
    letters = sorted(string)

    for idx, letter in enumerate(letters):
        if letter == letters[idx - 1]:
            return False

    return True

if __name__ == "__main__":
    input_str = input("Enter a string ").strip().lower()

    isogram = check_isogram(input_str)
    print(f"{input_str} is {'an' if isogram else 'not an'} isogram.")