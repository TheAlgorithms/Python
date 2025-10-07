def generate_square(keyword: str) -> list:
    """
    Generate a 5x5 Playfair square (I/J combined) from a keyword.
    """
    keyword = keyword.upper().replace("J", "I")
    seen = set()
    square = []
    for char in keyword:
        if char.isalpha() and char not in seen:
            seen.add(char)
            square.append(char)
    for char in "ABCDEFGHIKLMNOPQRSTUVWXYZ":
        if char not in seen:
            seen.add(char)
            square.append(char)
    return [square[i : i + 5] for i in range(0, 25, 5)]


def find_position(square, char):
    """
    Return (row, col) of char in given 5x5 square.
    """
    if char == "J":
        char = "I"
    for r in range(5):
        for c in range(5):
            if square[r][c] == char:
                return r, c
    return None


def two_square_encrypt(plaintext: str, key1: str, key2: str) -> str:
    """
    Encrypt plaintext using the Two-Square cipher.

    >>> two_square_encrypt("HELLO", "KEYWORD", "EXAMPLE")
    'CEYLBX'
    """
    plaintext = plaintext.upper().replace("J", "I")
    plaintext = "".join([c for c in plaintext if c.isalpha()])

    # split into digraphs
    pairs = []
    i = 0
    while i < len(plaintext):
        a = plaintext[i]
        b = plaintext[i + 1] if i + 1 < len(plaintext) else "X"
        if a == b:
            b = "X"
            i += 1
        else:
            i += 2
        pairs.append((a, b))

    square1 = generate_square(key1)
    square2 = generate_square(key2)

    ciphertext = ""
    for a, b in pairs:
        r1, c1 = find_position(square1, a)
        r2, c2 = find_position(square2, b)
        ciphertext += square2[r1][c2]
        ciphertext += square1[r2][c1]
    return ciphertext


def two_square_decrypt(ciphertext: str, key1: str, key2: str) -> str:
    """
    Decrypt ciphertext using the Two-Square cipher.

    >>> two_square_decrypt("CEYLBX", "KEYWORD", "EXAMPLE")
    'HELLOX'
    """
    ciphertext = ciphertext.upper().replace("J", "I")
    ciphertext = "".join([c for c in ciphertext if c.isalpha()])

    if len(ciphertext) % 2 != 0:
        raise ValueError("Ciphertext must have even length")

    square1 = generate_square(key1)
    square2 = generate_square(key2)

    plaintext = ""
    for i in range(0, len(ciphertext), 2):
        a, b = ciphertext[i], ciphertext[i + 1]
        r1, c1 = find_position(square2, a)
        r2, c2 = find_position(square1, b)
        plaintext += square1[r1][c2]
        plaintext += square2[r2][c1]
    return plaintext


if __name__ == "__main__":
    from doctest import testmod

    testmod()

    # Example usage
    plaintext = "HELLO"
    key1 = "KEYWORD"
    key2 = "EXAMPLE"
    encrypted = two_square_encrypt(plaintext, key1, key2)
    decrypted = two_square_decrypt(encrypted, key1, key2)

    print("\n\n")
    print("Plaintext:", plaintext)
    print("Encrypted:", encrypted)
    print("Decrypted:", decrypted)
