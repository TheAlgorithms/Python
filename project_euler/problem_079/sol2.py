"""
Project Euler Problem 79: https://projecteuler.net/problem=79

Passcode derivation

A common security method used for online banking is to ask the user for three
random characters from a passcode. For example, if the passcode was 531278,
they may ask for the 2nd, 3rd, and 5th characters; the expected reply would
be: 317.

The text file, keylog.txt, contains fifty successful login attempts.

Given that the three characters are always asked for in order, analyze the file
to determine the shortest possible secret passcode of unknown length.
"""

from collections import Counter


def find_secret_passcode(logins: list[str]) -> int:
    """
    Find the shortest possible secret passcode of unknown length.

    :param logins: A list of successful login attempts.
    :type logins: list[str]
    :return: The shortest possible secret passcode.
    :rtype: int

    >>> find_secret_passcode(["135", "259", "235", "189", "690", "168", "120", "136", "289", "589", "160", "165", "580", "369", "250", "280"])
    12356890

    >>> find_secret_passcode(["426", "281", "061", "819", "268", "406", "420", "428", "209", "689", "019", "421", "469", "261", "681", "201"])
    4206819
    """
    char_to_sum = Counter()
    char_to_count = Counter()
    result = []

    for login in logins:
        for idx, char in enumerate(login):
            if char not in char_to_sum:
                result.append(char)
            char_to_sum[char] += idx
            char_to_count[char] += 1

    result.sort(key=lambda character: char_to_sum[character] / char_to_count[character])

    return int("".join(result))


def solution(input_file: str = "keylog.txt") -> int:
    """
    Find the shortest possible passcode login by `input_file` text file.

    :param input_file: The name of the text file containing successful login attempts.
    :type input_file: str
    :return: The shortest possible secret passcode.
    :rtype: int

    >>> solution("keylog_test.txt")
    6312980
    """
    with open(input_file) as file:
        logins = [line.strip() for line in file.readlines()]

    return find_secret_passcode(logins)


if __name__ == "__main__":
    print(f"{solution() = }")
