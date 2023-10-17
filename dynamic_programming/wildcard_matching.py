"""
Given two strings, an input string and a pattern,
this program checks if the input string matches the pattern.

Example :
input_string = "baaabab"
pattern = "*****ba*****ab"
Output: True

This problem can be solved using the concept of "DYNAMIC PROGRAMMING".

We create a 2D boolean matrix, where each entry match_matrix[i][j] is True
if the first i characters in input_string match the first j characters
of pattern. We initialize the first row and first column based on specific
rules, then fill up the rest of the matrix using a bottom-up dynamic
programming approach.

The amount of match that will be determined is equal to match_matrix[n][m]
where n and m are lengths of the input_string and pattern respectively.

"""


def is_pattern_match(input_string: str, pattern: str) -> bool:
    """
    >>> is_pattern_match('baaabab','*****ba*****ba')
    False
    >>> is_pattern_match('baaabab','*****ba*****ab')
    True
    >>> is_pattern_match('aa','*')
    True
    """

    input_length = len(input_string)
    pattern_length = len(pattern)

    match_matrix = [[False] * (pattern_length + 1) for _ in range(input_length + 1)]

    match_matrix[0][0] = True

    for j in range(1, pattern_length + 1):
        if pattern[j - 1] == "*":
            match_matrix[0][j] = match_matrix[0][j - 1]

    for i in range(1, input_length + 1):
        for j in range(1, pattern_length + 1):
            if pattern[j - 1] in ("?", input_string[i - 1]):
                match_matrix[i][j] = match_matrix[i - 1][j - 1]
            elif pattern[j - 1] == "*":
                match_matrix[i][j] = match_matrix[i - 1][j] or match_matrix[i][j - 1]
            else:
                match_matrix[i][j] = False

    return match_matrix[input_length][pattern_length]


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    print(f"{is_pattern_match('baaabab','*****ba*****ab')}")
