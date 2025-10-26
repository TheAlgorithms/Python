"""
digital_root.py
----------------
Calculates the digital root of a given number.

A digital root is obtained by summing the digits of a number repeatedly
until only a single-digit number remains.

Example:
    >>> digital_root(942)
    6
    >>> digital_root(132189)
    6
    >>> digital_root(493193)
    2
"""

def digital_root(n: int) -> int:
    """Return the digital root of a non-negative integer."""
    while n >= 10:
        n = sum(map(int, str(n)))
    return n


if __name__ == "__main__":
    num = int(input("Enter a number: "))
    print(digital_root(num))
