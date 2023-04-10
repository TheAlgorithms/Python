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
    alphabet = list(ascii_uppercase)

    # create a list of unique characters in the keyword
    unique_chars = []
    for char in keyword:
        if char not in unique_chars:
            unique_chars.append(char)

    num_unique_chars_in_keyword = len(unique_chars)

    # add any uppercase letters from the alphabet
    # that are not in the keyword to the unique_chars list.
    for char in alphabet:
        if char not in unique_chars:
            unique_chars.append(char)

    rows = (26 // num_unique_chars_in_keyword) + 1
    # k is an index variable
    k = 0
    # create a modified version of the alphabet by dividing it into rows number of rows
    # and mapping the letters in the unique_chars list to the rows
    modified_alphabet = []
    for _ in range(rows):
        row = []
        for _ in range(num_unique_chars_in_keyword):
            row.append(unique_chars[k])
            k += 1
            # break out of the loop if we have reached the end of the alphabet
            if k >= 26:
                break
        modified_alphabet.append(row)

    mapping = {}
    k = 0
    for j in range(num_unique_chars_in_keyword):
        for row in modified_alphabet:
            # if current row is too short, break out of loop
            if len(row) <= j:
                break

            # map current letter to letter in modified alphabet
            mapping[alphabet[k]] = row[j]
            k += 1
            if k >= 26:
                break

    print(mapping)
    # create the encrypted text by mapping the plaintext to the modified alphabet
    return "".join(mapping[char] for char in plaintext)


if __name__ == "__main__":
    print(mixed_keyword("college", "UNIVERSITY"))
