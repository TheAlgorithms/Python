""" https://en.wikipedia.org/wiki/Jaro%E2%80%93Winkler_distance """
import math


def jaro_winkler(first_string: str, second_string: str) -> float:
    """
    >>> jaro_winkler("something", "gmosehitt")
    52
    """
    max_distance = math.floor(max(len(first_string), len(second_string)) / 2) - 1
    match_count = 0

    # matching characters
    for i, c1 in enumerate(first_string):
        for j, c2 in enumerate(second_string):
            if c1 == c2 and abs(i - j) < max_distance:
                match_count += 1

    # transposition
    not_match = 0
    for c1, c2 in zip(first_string, second_string):
        if c1 != c2:
            not_match += 1

    if not match_count:
        jaro = 0
    else:
        jaro = 1/3 * (match_count/len(first_string) + match_count/len(second_string) + (match_count - not_match/2)/match_count)

    # common prefix
    prefix_len = 0
    for c1, c2 in zip(first_string[:4], second_string[:4]):
        if c1 == c2:
            prefix_len += 1
        else:
            break

    return jaro + 0.1 * prefix_len * (1 - jaro)


if __name__ == '__main__':
    print(jaro_winkler("martha", "marhta"))