def checkPowerOf4(n):
    """
    Return true if `n` is a power of 2, and its only
    set bit is present at even position
    """
    return n and not (n & (n - 1)) and not (n & 0xAAAAAAAA)


if __name__ == "__main__":
    n = int(input("Please enter a starting number: ").strip())
    if checkPowerOf4(n):
        print(n, "is a power of 4")
    else:
        print(n, "is not a power of 4")
