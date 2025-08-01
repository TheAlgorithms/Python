# This program checks if k is a power of n.

def is_k_power_of_n(n, k):
    """
    Checks if k can be reduced to 1 by repeatedly dividing it by n.

    >>> 2
    >>> 8
    True

    >>> 1092
    >>> 20,21,99,97,93,72,24,99,35,25,59,616
    True

    >>>12
    >>>100
    False
    """
    if n == 1:
        return k == 1
    if n <= 0 or k <= 0:
        return False
    while k % n == 0:
        k //= n
    return k == 1

n = int(input("Enter the base (n): "))
k = int(input("Enter the number to check (k): "))
print(is_k_power_of_n(n, k))
