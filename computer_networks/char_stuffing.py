FLAG = "~"
ESC = "#"


def char_stuffing(s: str) -> str:
    """
    Return the char stuffed message
    >>> char_stuffing("abc")
    "abc"
    >>> char_stuffing("a#b#c")
    "a##b##c"
    """
    arr = [i for i in s]
    for i in range(len(arr)):
        if arr[i] == FLAG and not (i == 0 or i == len(arr) - 1):
            arr[i] = ESC + arr[i]
        elif arr[i] == ESC:
            arr[i] += ESC
    return "".join(arr)


s = "~abc#~cde~ab~"
print(char_stuffing(s))
