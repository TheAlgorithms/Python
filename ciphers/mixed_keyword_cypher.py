from string import ascii_uppercase


def mixed_keyword(
    keyword: str, plaintext: str, verbose: bool = False, alphabet: str = ascii_uppercase
) -> str:
    """
    For keyword: hello

    H E L O
    A B C D
    F G I J
    K M N P
    Q R S T
    U V W X
    Y Z
    and map vertically

    >>> mixed_keyword("college", "UNIVERSITY", True)  # doctest: +NORMALIZE_WHITESPACE
    {'A': 'C', 'B': 'A', 'C': 'I', 'D': 'P', 'E': 'U', 'F': 'Z', 'G': 'O', 'H': 'B',
     'I': 'J', 'J': 'Q', 'K': 'V', 'L': 'L', 'M': 'D', 'N': 'K', 'O': 'R', 'P': 'W',
     'Q': 'E', 'R': 'F', 'S': 'M', 'T': 'S', 'U': 'X', 'V': 'G', 'W': 'H', 'X': 'N',
     'Y': 'T', 'Z': 'Y'}
    'XKJGUFMJST'

    >>> mixed_keyword("college", "UNIVERSITY", False)  # doctest: +NORMALIZE_WHITESPACE
    'XKJGUFMJST'
    """
    keyword = keyword.upper()
    plaintext = plaintext.upper()
    alphabet_set = set(alphabet)

    # create a list of unique characters in the keyword - their order matters
    # it determines how we will map plaintext characters to the ciphertext
    unique_chars = []
    for char in keyword:
        if char in alphabet_set and char not in unique_chars:
            unique_chars.append(char)
    # the number of those unique characters will determine the number of rows
    num_unique_chars_in_keyword = len(unique_chars)

    # create a shifted version of the alphabet
    shifted_alphabet = unique_chars + [
        char for char in alphabet if char not in unique_chars
    ]

    # create a modified alphabet by splitting the shifted alphabet into rows
    modified_alphabet = [
        shifted_alphabet[k : k + num_unique_chars_in_keyword]
        for k in range(0, 26, num_unique_chars_in_keyword)
    ]

    # map the alphabet characters to the modified alphabet characters
    # going 'vertically' through the modified alphabet - consider columns first
    mapping = {}
    letter_index = 0
    for column in range(num_unique_chars_in_keyword):
        for row in modified_alphabet:
            # if current row (the last one) is too short, break out of loop
            if len(row) <= column:
                break

            # map current letter to letter in modified alphabet
            mapping[alphabet[letter_index]] = row[column]
            letter_index += 1

    if verbose:
        print(mapping)
    # create the encrypted text by mapping the plaintext to the modified alphabet
    return "".join(mapping.get(char, char) for char in plaintext)


if __name__ == "__main__":
    # example use
    print(mixed_keyword("college", "UNIVERSITY"))
