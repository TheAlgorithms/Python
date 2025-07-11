LETTER_FREQUENCIES_DICT = {
    'A': 8.12, 'B': 1.49, 'C': 2.71, 'D': 4.32, 'E': 12.02, 'F': 2.3, 'G': 2.03,
    'H': 5.92, 'I': 7.31, 'J': 0.1, 'K': 0.69, 'L': 3.92, 'M': 2.61,
    'N': 6.95, 'O': 7.68, 'P': 1.82, 'Q': 0.11, 'R': 6.02, 'S': 6.28,
    'T': 9.10, 'U': 2.88, 'V': 1.11, 'W': 2.09, 'X': 0.17, 'Y': 2.11, 'Z': 0.07
}

LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def index_of_coincidence(frequencies: dict, length: int) -> float:
    """
    Calculates the index of coincidence for a text.
    :param frequencies: dictionary of the form {letter_of_the_alphabet: amount of times it appears in the text as a percentage}
    :param length: the length of the text
    :return the index of coincidence:
    """
    index = 0.0
    for value in frequencies.values():
        index += (value/length)**2
    return index


def find_key_from_vigenere_cipher(ciphertext: str) -> str:
    clean_ciphertext = list()
    for symbol in ciphertext:
        if symbol in LETTERS:
            clean_ciphertext.append(symbol.upper())

    clean_ciphertext = "".join(clean_ciphertext)

    key = ""  # todo replace with function
    return key