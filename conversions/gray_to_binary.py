"""
The below function will convert any binary string to gray string.

>>> gray_to_bin("1101101")
'1001001'

>>> gray_to_bin("1101")
'1001'

>>> gray_to_bin("1000")
'1111'
"""


def gray_to_bin(gray_code: str) -> str:
    """
    Convert a gray code to binary code equivalent
    https://en.wikipedia.org/wiki/Gray_code

    --------------LOGIC----------------
    Gray to Binary:
        Here the most significant bit of the Binary code is same
        as the given Gray code, so we direclty copy it. Further
        traversing the Gray code we check if the current character
        of Gray code is '0', if it is '0' we copy the value of
        previous index of converted Binary code, else we copy
        the flipped value of  current Gray character to our
        binary code.
    """
    if not all(char in "01" for char in gray_code):
        raise ValueError("Non-gray value was passed to the function")
    if not gray_code:
        raise ValueError("Empty string was passed to the function")
    sb = []
    matrice = [["", ""] for _ in range(len(gray_code))]
    matrice[0][0] = gray_code[0]
    matrice[0][1] = gray_code[0]
    for i in range(1, len(gray_code)):
        matrice[i][0] = gray_code[i]
        if gray_code[i] == "0":
            matrice[i][1] = matrice[i - 1][1]
        else:
            matrice[i][1] = "1" if matrice[i - 1][1] == "0" else "0"
    for i in range(len(gray_code)):
        sb.append(matrice[i][1])
    return "".join(sb)


if __name__ == "__main__":
    from doctest import testmod

    testmod()
