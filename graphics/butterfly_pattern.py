def butterfly_pattern(n):
    # Upper part
    for i in range(1, n + 1):
        print("*" * i, end="")
        print(" " * (2 * (n - i)), end="")
        print("*" * i)

    # Lower part
    for i in range(n - 1, 0, -1):
        print("*" * i, end="")
        print(" " * (2 * (n - i)), end="")
        print("*" * i)


n = int(input("Enter the size: "))
butterfly_pattern(n)
