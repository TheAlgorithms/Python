def butterflyPattern(n):
    for i in range(n // 2):
        print("* " * (i + 1), end="")
        print(" " * (((n + 1) // 2 - 2) * 4 - 4 * i + 1), end="")
        print(" *" * (i + 1))
    print("* " * (n // 2), end="*")
    print(" *" * (n // 2))
    for i in range(n // 2):
        print("* " * (n // 2 - i), end="")
        print(" " * (1 + 4 * i), end="")
        print(" *" * (n // 2 - i))


n = int(input())
butterflyPattern(n)
