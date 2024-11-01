FLAG = "~"
ESC = "#"


def char_stuffing(string: str) -> str:
    """
    Return the char stuffed message
    >>> char_stuffing("abc")
    'abc'
    >>> char_stuffing("a#b#c")
    'a##b##c'
    """
    arr = []
    # Create a list of characters from the string
    for character in string:
        arr.append(character)
    for i in range(len(arr)):
        # If we encounter the FLAG and it's not the first or last character
        if arr[i] == FLAG and not (i == 0 or i == len(arr) - 1):
            arr[i] = ESC + arr[i]  # Prepend ESC to FLAG
        elif arr[i] == ESC:
            arr[i] += ESC  # Duplicate ESC
    return "".join(arr)  # Join the list of characters back into a string


string = "~abc#~cde~ab~"
print(char_stuffing(string))
