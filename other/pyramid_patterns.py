"""
patterns/pyramid_patterns.py

Pattern Printing Examples:
- Pyramid
- Inverted Pyramid
- Diamond

Demonstrates loops, functions, and conditionals for beginners.

Example:
>>> pyramid(3)
  *
 ***
*****

>>> inverted_pyramid(3)
*****
 ***
  *

>>> diamond(3)
  *
 ***
*****
 ***
  *
"""

# No import needed for None type annotation

def pyramid(n: int) -> None:
    """Prints a pyramid pattern of height n."""
    for i in range(n):
        print(" " * (n - i - 1) + "*" * (2 * i + 1))


def inverted_pyramid(n: int) -> None:
    """Prints an inverted pyramid pattern of height n."""
    for i in range(n - 1, -1, -1):
        print(" " * (n - i - 1) + "*" * (2 * i + 1))


def diamond(n: int) -> None:
    """Prints a diamond pattern of height n."""
    pyramid(n)
    for i in range(n - 2, -1, -1):
        print(" " * (n - i - 1) + "*" * (2 * i + 1))


if __name__ == "__main__":
    print("Pyramid:")
    pyramid(5)
    print("\nInverted Pyramid:")
    inverted_pyramid(5)
    print("\nDiamond:")
    diamond(5)
