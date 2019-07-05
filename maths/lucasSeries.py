"""Lucas Sequence Using Recursion."""


def recur_luc(n):
    """Calculate Lucas Sequence Using Recursion."""
    if n == 1:
        return n
    if n == 0:
        return 2
    return recur_luc(n - 1) + recur_luc(n - 2)


LIMIT = int(input("How many terms to include in Lucas series:"))
print("Lucas series:")
for i in range(LIMIT):
    print(recur_luc(i))
