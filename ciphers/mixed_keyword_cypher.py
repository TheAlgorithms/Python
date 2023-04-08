from string import ascii_uppercase


def mixed_keyword(keyword: str = "college", plaintext: str = "UNIVERSITY") -> str:
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

    >>> mixed_keyword("college", "UNIVERSITY")  # doctest: +NORMALIZE_WHITESPACE
    {'A': 'C', 'B': 'A', 'C': 'I', 'D': 'P', 'E': 'U', 'F': 'Z', 'G': 'O', 'H': 'B',
     'I': 'J', 'J': 'Q', 'K': 'V', 'L': 'L', 'M': 'D', 'N': 'K', 'O': 'R', 'P': 'W',
     'Q': 'E', 'R': 'F', 'S': 'M', 'T': 'S', 'U': 'X', 'V': 'G', 'W': 'H', 'X': 'N',
     'Y': 'T', 'Z': 'Y'}
    'XKJGUFMJST'
    """
    keyword = keyword.upper()
    plaintext = plaintext.upper()

    unique_chars = []
    for char in keyword:
        if char not in unique_chars:
            unique_chars.append(char)

    num_unique_chars_in_keyword = len(unique_chars)

    alphabet = list(ascii_uppercase)
    # add the rest of the alphabet to the unique_chars list
    for char in alphabet:
        if char not in unique_chars:
            unique_chars.append(char)

    rows = int(26 / 4)
    # k is an index variable
    k = 0
    modified_alphabet = []
    for _ in range(rows):
        row = []
        for _ in range(num_unique_chars_in_keyword):
            row.append(unique_chars[k])
            if k >= 25:
                break
            k += 1
        modified_alphabet.append(row)

    mapping = {}
    k = 0
    for j in range(num_unique_chars_in_keyword):
        for row in modified_alphabet:
            if not len(row) - 1 >= j:
                break
            mapping[alphabet[k]] = row[j]
            if not k < 25:
                break
            k += 1

    # create the encrypted text by mapping the plaintext to the modified alphabet
    return "".join(mapping[char] for char in plaintext)


if __name__ == "__main__":
    print(mixed_keyword("college", "UNIVERSITY"))
