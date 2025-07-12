LETTER_FREQUENCIES_DICT = {
    'A': 8.12, 'B': 1.49, 'C': 2.71, 'D': 4.32, 'E': 12.02, 'F': 2.3, 'G': 2.03,
    'H': 5.92, 'I': 7.31, 'J': 0.1, 'K': 0.69, 'L': 3.92, 'M': 2.61,
    'N': 6.95, 'O': 7.68, 'P': 1.82, 'Q': 0.11, 'R': 6.02, 'S': 6.28,
    'T': 9.10, 'U': 2.88, 'V': 1.11, 'W': 2.09, 'X': 0.17, 'Y': 2.11, 'Z': 0.07
}
LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
PARAMETER = 0.0665  # index of confidence of the entire language (for english 0.0665)


def index_of_coincidence(frequencies: dict, length: int) -> float:
    """
    Calculates the index of coincidence for a text.
    :param frequencies: dictionary of the form {letter_of_the_alphabet: amount of times it appears in the text as a percentage}
    :param length: the length of the text
    :return the index of coincidence:
    """
    index = 0.0
    for value in frequencies.values():
        index += (value / length) ** 2
    return index


def calculate_indexes_of_coincidence(ciphertext: str, step: int) -> list:
    """
    For each number j in the range [0, step) the function checks the letters of the ciphertext whose position has the
    form j+n*step, where n is an integer and for these letters it calculates the index of coincidence. It returns a list
    with step elements, which represent the indexes of coincidence.
    :param ciphertext: s string (text)
    :param step: the step when traversing through the cipher
    :return: a list with the indexes of coincidence
    """
    indexes_of_coincidence = list()
    length = len(ciphertext)

    # for every starting point in [0, step)
    for j in range(step):
        frequencies = dict()
        c = 0
        for i in range(0 + j, length, step):
            c += 1
            try:  # in case the frequencies dictionary does not already have this key
                frequencies[ciphertext[i]] += 1
            except KeyError:
                frequencies[ciphertext[i]] = 1
        indexes_of_coincidence.append(index_of_coincidence(frequencies, c))

    return indexes_of_coincidence


def friedman_method(ciphertext: str, max_keylength: int=None) -> int:
    """
    Implements Friedman's method for finding the length of the key of a Vigenere cipher. It finds the length with an
    index of confidence closer to that of an average text in the english language.
    :param ciphertext: a string (text)
    :param max_keylength: the maximum length of key that Friedman's method should check, if None then it defaults to the
    length of the cipher
    :return: the length of the key
    """
    # sets the default value of MAX_KEYLEBGTH
    if max_keylength is None:
        max_keylength = len(ciphertext)

    frequencies = [1.5]  # the zeroth position should not be used: length of key is greater than zero

    # for every length of key
    for i in range(1, max_keylength + 1):

        # for a specific length it finds the minimum index of coincidence
        min1 = 15.0
        for val in calculate_indexes_of_coincidence(ciphertext, i):
            if abs(val - PARAMETER) < abs(min1 - PARAMETER):
                min1 = val
        frequencies.append(min1)

    # finds which length of key has the minimum difference with the language PARAMETER
    li = (15.0, -1)  # initialization
    for i in range(len(frequencies)):
        if abs(frequencies[i] - PARAMETER) < abs(li[0] - PARAMETER):
            li = (frequencies[i], i)

    return li[1]


def find_key_from_vigenere_cipher(ciphertext: str) -> str:
    clean_ciphertext = list()
    for symbol in ciphertext:
        if symbol in LETTERS:
            clean_ciphertext.append(symbol.upper())

    clean_ciphertext = "".join(clean_ciphertext)

    key = ""  # todo replace with function
    return key


if __name__ == '__main__':
    print(index_of_coincidence(LETTER_FREQUENCIES_DICT, 1000))
