"""
Project Euler Problem 25: https://projecteuler.net/problem=25
1000-digit Fibonacci Number
The Fibonacci sequence is defined by the recurrence relation:
    Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.
Hence the first 12 terms will be:
    F1 = 1
    F2 = 1
    F3 = 2
    F4 = 3
    F5 = 5
    F6 = 8
    F7 = 13
    F8 = 21
    F9 = 34
    F10 = 55
    F11 = 89
    F12 = 144
The 12th term, F12, is the first term to contain three digits.
What is the index of the first term in the Fibonacci sequence to contain 1000
digits?
"""


def solution(first_digit_occurrence: int = 1000) -> int:
    """Returns the index of the first term in the Fibonacci sequence to contain
    n digits.

    >>> solution(1000)
    4782
    >>> solution(100)
    476
    >>> solution(50)
    237
    >>> solution(3)
    12
    """

    if first_digit_occurrence < 1:
        raise ValueError("Parameter search_limit must be greater than or equal to one.")

    last_number, new_number = 0, 1

    last_two_numbers, sequenced_numbers = [last_number, new_number], [1]

    while len(str(last_two_numbers[last_number])) <= first_digit_occurrence:
        output = last_two_numbers[last_number] + last_two_numbers[new_number]

        if len(str(output)) == first_digit_occurrence:
            break

        last_two_numbers[last_number], last_two_numbers[new_number] = (
            last_two_numbers[new_number],
            output,
        )

        sequenced_numbers.append(output)

    return len(sequenced_numbers) + 1


if __name__ == "__main__":
    print(f"{solution() = }")
