def addBinary(a: str, b: str) -> str:
    i, j = len(a) - 1, len(b) - 1
    carry = 0
    result = []

    while i >= 0 or j >= 0 or carry:
        total = carry

        if i >= 0:
            total += int(a[i])
            i -= 1
        if j >= 0:
            total += int(b[j])
            j -= 1

        result.append(str(total % 2))  # current bit
        carry = total // 2             # carry for next bit

    return ''.join(reversed(result))


# Example usage
if __name__ == "__main__":
    a = "1010"
    b = "1011"
    print("Input: a =", a, ", b =", b)
    print("Output:", addBinary(a, b))
