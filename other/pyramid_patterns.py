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

def pyramid(height: int) -> None:
    """Prints a pyramid pattern of the specified height."""
    for i in range(height):
        print(" " * (height - i - 1) + "*" * (2 * i + 1))


def inverted_pyramid(height: int) -> None:
    """Prints an inverted pyramid pattern of the specified height."""
    for i in range(height - 1, -1, -1):
        print(" " * (height - i - 1) + "*" * (2 * i + 1))


def diamond(height: int) -> None:
    """Prints a diamond pattern of the specified height."""
    pyramid(height)
    for i in range(height - 2, -1, -1):
        print(" " * (height - i - 1) + "*" * (2 * i + 1))


if __name__ == "__main__":
    print("Pyramid:")
    pyramid(5)
    print("\nInverted Pyramid:")
    inverted_pyramid(5)
    print("\nDiamond:")
    diamond(5)
