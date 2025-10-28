"""
A simple program to reverse a string.

Author: Eric Butler Jr.
Date: 2025-10-28
"""

def reverse_string(s: str) -> str:
    """Return the reverse of the given string."""
    return s[::-1]


if __name__ == "__main__":
    text = input("Enter a string: ")
    print("Reversed string:", reverse_string(text))
