"""
In cryptography, the ADFGVX cipher was a field cipher
used by the German Army on the Western Front during World War I.
The cipher is named after the six possible letters
used in the ciphertext: A, D, F, G, V and X. The letters
were chosen deliberately because they are very different from
one another in the Morse code. That reduced the possibility of
operator error.

References:
https://en.wikipedia.org/wiki/ADFGVX_cipher
"""


def main():
    """
    >>> key = "u2rle3o068mz95afyicngkt7p1vdqxwb4jhs"
    >>> keyword = "white"
    >>> msg = "arigato"
    >>> decrypt(key,keyword, encrypt(key, keyword, msg)) == msg
    True
    """
    message = input("Enter the message\n").strip()
    key = input(
        "Enter the alphabetical key of length 36 (i and j are same). \n"
    ).strip()
    keyword = input("Enter the keyword \n").strip()
    mode = input("Enter e/d  for encryption/decryption").strip().lower()

    if mode == "e":
        print("Encrypted message is", encrypt(key, keyword, message))
    elif mode == "d":
        print("Decrypted message is", decrypt(key, keyword, message))
    else:
        print("Wrong input. Please enter either e or d.\n")


def get_polybius_encoded_letters(key: str, letter: str) -> str:
    """
    >>> get_polybius_encoded_letters('7yvorqhkdbmp12g90n3z8tcfws6uexj4l5ai',\
         'a')
    'xv'
    """
    position = key.find(letter)
    row_in_polybius_square = position // 6
    col_in_polybius_square = position % 6
    return "adfgvx"[row_in_polybius_square] + "adfgvx"[col_in_polybius_square]


def get_polybius_decoded_letters(key: str, letter_pair: str) -> str:
    """
    >>> get_polybius_decoded_letters('7yvorqhkdbmp12g90n3z8tcfws6uexj4l5ai',\
         'xv')
    'a'
    """
    row = "adfgvx".find(letter_pair[0])
    col = "adfgvx".find(letter_pair[1])
    return key[(6 * row + col) % 36]


def encrypt(key: str, keyword: str, message: str) -> str:
    """
    >>> encrypt('7yvorqhkdbmp12g90n3z8tcfws6uexj4l5ai', 'number', 'attack')
    'gvgdggxxgdvv'

    >>> encrypt('7yvorqhkdbmp12g90n3z8tcfws6uexj4l5ai', 'walter', 'try')
    'gaadvg'
    """

    message = message.lower()
    message.replace("i", "j")
    key = key.lower()
    key.replace("i", "j")

    if len(key) != 36:
        raise ValueError("Please make sure that key length is 36")

    polybius_encoded = ""
    for i in message:
        polybius_encoded += get_polybius_encoded_letters(key, i)

    keyword_arrays = [[] for i in range(len(keyword))]

    for i, letter in enumerate(polybius_encoded):
        keyword_arrays[i % len(keyword)].append(letter)

    sorted_index_pairs = list(enumerate(keyword))
    sorted_index_pairs.sort(key=lambda x: x[1])

    ciphertext = []

    for i, val in sorted_index_pairs:
        ciphertext.extend(keyword_arrays[i])

    return "".join(ciphertext)


def decrypt(key: str, keyword: str, cipher: str) -> str:
    """
    >>> decrypt('7yvorqhkdbmp12g90n3z8tcfws6uexj4l5ai', 'number',\
         'gvgdggxxgdvv')
    'attack'

    >>> decrypt('7yvorqhkdbmp12g90n3z8tcfws6uexj4l5ai', 'walter', 'gaadvg')
    'try'
    """
    if len(key) != 36:
        raise ValueError("Please make sure that key length is 36")

    key = key.lower()
    cipher = cipher.lower()

    sorted_keyword = list(keyword)
    sorted_keyword.sort()

    num_longer_cols = len(cipher) % len(keyword)
    min_len_cols = len(cipher) // len(keyword)
    num_cols = len(keyword)

    start_index = 0

    sorted_keyword_array = []

    for i in range(num_cols):
        current_col_len = min_len_cols
        if keyword.find(sorted_keyword[i]) < num_longer_cols:
            current_col_len += 1

        if current_col_len > min_len_cols:
            sorted_keyword_array.append(
                list(cipher[start_index : start_index + current_col_len])
            )
        else:
            sorted_keyword_array.append(
                list(cipher[start_index : start_index + current_col_len]) + [""]
            )
        start_index = start_index + current_col_len

    keyword_array = []
    for i in keyword:
        index = sorted_keyword.index(i)
        keyword_array.append(sorted_keyword_array[index])

    polybius_encoded = list(zip(*keyword_array))
    polybius_encoded = "".join([j for i in polybius_encoded for j in i])

    message = ""
    for i in range(0, len(polybius_encoded), 2):
        message += get_polybius_decoded_letters(key, polybius_encoded[i : i + 2])

    return message


if __name__ == "__main__":
    main()
