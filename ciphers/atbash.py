""" https://en.wikipedia.org/wiki/Atbash """
import string


def atbash(sequence: str) -> str:
    """
    >>> atbash("ABCDEFG")
    'ZYXWVUT'

    >>> atbash("aW;;123BX")
    'zD;;123YC'
    """
    letters = string.ascii_letters
    letters_reversed = string.ascii_lowercase[::-1] + string.ascii_uppercase[::-1]
    return "".join(
        letters_reversed[letters.index(_)] if _ in letters else _ for _ in sequence
    )


if __name__ == "__main__":
    for sequence in ["ABCDEFGH", "123GGjj", "testStringtest", "with space"]:
        print(f"{sequence} encrypted in atbash: {atbash(sequence)}")
