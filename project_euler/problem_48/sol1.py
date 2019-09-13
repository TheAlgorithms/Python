"""
Self Powers
Problem 48

The series, 11 + 22 + 33 + ... + 1010 = 10405071317.

Find the last ten digits of the series, 11 + 22 + 33 + ... + 10001000.
"""


def solution():
    """Returns the last 10 digits of the series, 11 + 22 + 33 + ... + 10001000.

    >>> solution()
    '9110846700'
    """
    total = 0
    for i in range(1, 1001):
        total += i ** i
    return str(total)[-10:]


if __name__ == "__main__":
    print(solution())
