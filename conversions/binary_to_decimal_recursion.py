def binaryToDecimal(b, i = 0):
    n = len(b)
    if i == n - 1:
        return int(b[i]) - 0

    return (((int(b[i]) - 0) << (n - i - 1)) + binaryToDecimal(b, i + 1))

binary_string = "1010"
print(binaryToDecimal(binary_string))