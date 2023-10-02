"""
The below function will convert any binary string to gray string.

>>> bin_to_gray("1001001")
'1101101'

>>> bin_to_gray("1001")
'1101'

>>> bin_to_gray("1111")
'1000'
"""


def bin_to_gray(bin_code: str) -> str:
    """
    Convert a binary code to gray code equivalent
    https://en.wikipedia.org/wiki/Gray_code

    --------------LOGIC----------------
    Binary to Gray:
        Here the most significant bit of the gray code is same as
        the given binary code so we don't need to make any changes
        Further traversing the binary from 1st index
        (i.e 2nd position) we take the xor of current
        index character  of binary code with the previous index
        character of binary code and add it to our converted
        gray code
    """
    if not all(char in "01" for char in bin_code):
        raise ValueError("Non-binary value was passed to the function")
    if not bin_code:
        raise ValueError("Empty string was passed to the function")
    sb = []
    matrice = [[None, None] for _ in range(len(bin_code))]
    matrice[0][0] = bin_code[0]
    matrice[0][1] = bin_code[0]
    for i in range(1, len(bin_code)):
        x = "0" if bin_code[i] == bin_code[i - 1] else "1"
        matrice[i][1] = x
        matrice[i][0] = bin_code[i]
    for i in range(len(bin_code)):
        sb.append(matrice[i][1])
    return "".join(sb)


if __name__ == "__main__":
    from doctest import testmod

    testmod()
