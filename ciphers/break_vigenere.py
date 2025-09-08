LETTER_FREQUENCIES_DICT = {
    "A": 8.12,
    "B": 1.49,
    "C": 2.71,
    "D": 4.32,
    "E": 12.02,
    "F": 2.3,
    "G": 2.03,
    "H": 5.92,
    "I": 7.31,
    "J": 0.1,
    "K": 0.69,
    "L": 3.92,
    "M": 2.61,
    "N": 6.95,
    "O": 7.68,
    "P": 1.82,
    "Q": 0.11,
    "R": 6.02,
    "S": 6.28,
    "T": 9.10,
    "U": 2.88,
    "V": 1.11,
    "W": 2.09,
    "X": 0.17,
    "Y": 2.11,
    "Z": 0.07,
}
LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
PARAMETER = 0.0665  # index of confidence of the entire language (for
# english 0.0665)
MAX_KEYLENGTH = (
    None  # None is the default, you can also try a positive integer (
    # example: 10)
)


def index_of_coincidence(frequencies: dict, length: int) -> float:
    """
    Calculates the index of coincidence for a text.
    :param frequencies: dictionary of the form {letter_of_the_alphabet: amount
    of times it appears in the text as a percentage}
    :param length: the length of the text
    :return: the index of coincidence
    """
    index = 0.0
    for value in frequencies.values():
        index += value * (value - 1)
    return index / (length * (length - 1))


def calculate_indexes_of_coincidence(ciphertext: str, step: int) -> list:
    """
    For each number j in the range [0, step) the function checks the letters of
    the ciphertext whose position has the form j+n*step, where n is an integer
    and for these letters it calculates the index of coincidence. It returns a
    list with step elements, which represent the indexes of coincidence.
    :param ciphertext: s string (text)
    :param step: the step when traversing through the cipher
    :return: a list with the indexes of coincidence
    """
    indexes_of_coincidence = []
    length = len(ciphertext)

    # for every starting point in [0, step)
    for j in range(step):
        frequencies: dict[str, int] = {}
        c = 0
        for i in range(0 + j, length, step):
            c += 1
            try:  # in case the frequencies dictionary does not already have
                # this key
                letter = ciphertext[i]
                temp = frequencies[letter]
                frequencies[ciphertext[i]] = temp + 1
            except KeyError:
                frequencies[ciphertext[i]] = 1
        if c > 1:  # to avoid division by zero in the index_of_coincidence
            # function
            indexes_of_coincidence.append(index_of_coincidence(frequencies, c))

    return indexes_of_coincidence


def friedman_method(ciphertext: str, max_keylength: int | None = None) -> int:
    """
    Implements Friedman's method for finding the length of the key of a
    Vigenere cipher. It finds the length with an index of confidence closer
    to that of an average text in the english language. Check the wikipedia
    page: https://en.wikipedia.org/wiki/Vigen%C3%A8re_cipher The algorithm
    is in the book "Introduction to Cryptography", K. Draziotis
    https://repository.kallipos.gr/handle/11419/8183
    :param ciphertext: a string (text)
    :param max_keylength: the maximum length of key that Friedman's method
    should check, if None then it defaults to the length of the cipher
    :return: the length of the key
    """
    # sets the default value of max_keylength
    if max_keylength is None:
        max_keylength = len(ciphertext)

    frequencies = [
        1.5
    ]  # the zeroth position should not be used: length of key is greater
    # than zero

    # for every length of key
    for i in range(1, max_keylength + 1):
        # for a specific length it finds the minimum index of coincidence
        min1 = 15.0
        for val in calculate_indexes_of_coincidence(ciphertext, i):
            if abs(val - PARAMETER) < abs(min1 - PARAMETER):
                min1 = val
        frequencies.append(min1)

    # finds which length of key has the minimum difference with the language
    # PARAMETER
    li = (15.0, -1)  # initialization
    for i in range(len(frequencies)):
        if abs(frequencies[i] - PARAMETER) < abs(li[0] - PARAMETER):
            li = (frequencies[i], i)

    return li[1]


def get_frequencies() -> tuple:
    """Return the values of the global variable @LETTER_FREQUENCIES_DICT as a
    tuple ex. (0.25, 1.42, ...).
    """
    t = tuple(LETTER_FREQUENCIES_DICT[chr(i)] for i in range(ord("A"), ord("A") + 26))
    return tuple(num / 100 for num in t)


def find_key(ciphertext: str, key_length: int) -> str:
    """
    Finds the key of a text which has been encrypted with the Vigenere
    algorithm, using statistical analysis. The function needs an estimation
    of the length of the key. Firstly it finds the frequencies of the
    letters in the text. Then it compares these frequencies with those of an
    average text in the english language. For each letter it multiplies its
    frequency with the average one and adds them all together, then it
    shifts the frequencies of the text cyclically by one position and
    repeats the process. The shift that produces the largest sum corresponds
    to a letter of the key. The whole procedure takes place for every letter
    of the key (essentially as many times as the length of the key). See
    here: https://www.youtube.com/watch?v=LaWp_Kq0cKs
    :param ciphertext: a string (text)
    :param key_length: a supposed length of the key
    :return: the key as a string
    """
    a = ord("A")
    cipher_length = len(ciphertext)
    alphabet_length = 26  # the length of the english alphabet

    key = []

    # for every letter of the key
    for k in range(key_length):
        # find the frequencies of the letters in the message: the frequency
        # of 'A' is in the first position of the freq list and so on
        freq = [0.0] * alphabet_length
        c = 0
        for i in range(k, cipher_length, key_length):
            freq[ord(ciphertext[i]) - a] += 1
            c += 1
        freq = [num / c for num in freq]

        # find the max sum -> part of the key
        real_freq = get_frequencies()
        max1 = [-1, None]  # value, position
        for i in range(alphabet_length):
            new_val = sum((freq[j] * real_freq[j]) for j in range(alphabet_length))
            if max1[0] < new_val:
                max1 = [new_val, i]
            freq.append(
                freq.pop(0)
            )  # shift the list cyclically one position to the left
        key.append(max1[1])

    key_as_list_of_letters = []
    for num in key:
        if num is not None:
            key_as_list_of_letters.append(chr(num + a))

    return "".join(key_as_list_of_letters)  # return the key as a string


def find_key_from_vigenere_cipher(ciphertext: str) -> str:
    """
    Tries to find the key length and then the actual key of a Vigenere
    ciphertext. It uses Friedman's method and statistical analysis. It works
    best for large pieces of text written in the english language.
    """
    clean_ciphertext_list = []
    for symbol in ciphertext.upper():
        if symbol in LETTERS:
            clean_ciphertext_list.append(symbol)

    clean_ciphertext = "".join(clean_ciphertext_list)

    key_length = friedman_method(clean_ciphertext, max_keylength=MAX_KEYLENGTH)
    print(f"The length of the key is {key_length}")
    if key_length <= 0:
        raise ValueError("The length of the key should be strictly positive")

    key = find_key(clean_ciphertext, key_length)
    return key


if __name__ == "__main__":
    print("")
    # # how to execute
    # with open("out.txt") as file:
    #     ciphertext = file.read()
    #     key = find_key_from_vigenere_cipher(ciphertext)
    #     print(key)



# ---------- TESTS ----------
# def test_index_of_coincidence(f)

