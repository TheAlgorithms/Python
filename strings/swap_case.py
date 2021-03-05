"""
This algorithm helps you to swap cases.

User will give input and then program will perform swap cases.

In other words, convert all lowercase letters to uppercase letters and vice versa.
For example:
1. Please input sentence: Algorithm.Python@89
  aLGORITHM.pYTHON@89
2. Please input sentence: github.com/mayur200
  GITHUB.COM/MAYUR200

"""


def swap_case(sentence: str) -> str:
    """
    This function will convert all lowercase letters to uppercase letters
    and vice versa.

    >>> swap_case('Algorithm.Python@89')
    'aLGORITHM.pYTHON@89'
    """
    new_string = ""
    for char in sentence:
        if char.isupper():
            new_string += char.lower()
        elif char.islower():
            new_string += char.upper()
        else:
            new_string += char

    return new_string


if __name__ == "__main__":
    print(swap_case(input("Please input sentence: ")))
