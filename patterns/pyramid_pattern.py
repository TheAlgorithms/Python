"""
Prints a pyramid star pattern.

Example (n = 5):
    *
   ***
  *****
 *******
*********
"""


def pyramid(n: int) -> None:
    for i in range(n):
        print(" " * (n - i - 1) + "*" * (2 * i + 1))


if __name__ == "__main__":
    pyramid(5)
