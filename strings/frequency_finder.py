# Frequency Finder

import string

# frequency taken from https://en.wikipedia.org/wiki/Letter_frequency
english_letter_freq = {
    "E": 12.70,
    "T": 9.06,
    "A": 8.17,
    "O": 7.51,
    "I": 6.97,
    "N": 6.75,
    "S": 6.33,
    "H": 6.09,
    "R": 5.99,
    "D": 4.25,
    "L": 4.03,
    "C": 2.78,
    "U": 2.76,
    "M": 2.41,
    "W": 2.36,
    "F": 2.23,
    "G": 2.02,
    "Y": 1.97,
    "P": 1.93,
    "B": 1.29,
    "V": 0.98,
    "K": 0.77,
    "J": 0.15,
    "X": 0.15,
    "Q": 0.10,
    "Z": 0.07,
}
ETAOIN = "ETAOINSHRDLCUMWFGYPBVKJXQZ"
LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def get_letter_count(message: str) -> dict[str, int]:
    """
    Get the count of the letters in the given string
    >>> get_letter_count('Hello World')
    {'A': 0, 'B': 0, 'C': 0, 'D': 1, 'E': 1, 'F': 0, 'G': 0, 'H': 1, 'I': 0, 'J': 0, 'K': 0, 'L': 3, 'M': 0, 'N': 0, 'O': 2, 'P': 0, 'Q': 0, 'R': 1, 'S': 0, 'T': 0, 'U': 0, 'V': 0, 'W': 1, 'X': 0, 'Y': 0, 'Z': 0}
    >>> get_letter_count('Hello@ Man')
    {'A': 1, 'B': 0, 'C': 0, 'D': 0, 'E': 1, 'F': 0, 'G': 0, 'H': 1, 'I': 0, 'J': 0, 'K': 0, 'L': 2, 'M': 1, 'N': 1, 'O': 1, 'P': 0, 'Q': 0, 'R': 0, 'S': 0, 'T': 0, 'U': 0, 'V': 0, 'W': 0, 'X': 0, 'Y': 0, 'Z': 0}
    >>> get_letter_count('h')
    {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0, 'H': 1, 'I': 0, 'J': 0, 'K': 0, 'L': 0, 'M': 0, 'N': 0, 'O': 0, 'P': 0, 'Q': 0, 'R': 0, 'S': 0, 'T': 0, 'U': 0, 'V': 0, 'W': 0, 'X': 0, 'Y': 0, 'Z': 0}
    """
    letter_count = {letter: 0 for letter in string.ascii_uppercase}
    for letter in message.upper():
        if letter in LETTERS:
            letter_count[letter] += 1

    return letter_count


def get_item_at_index_zero(x: tuple) -> str:
    return x[0]


def get_frequency_order(message: str) -> str:
    """
    Get the frequency order of the letters in the given string
    >>> get_frequency_order('Hello World')
    'LOWDRHEZQXJKVBPYGFMUCSNIAT'
    >>> get_frequency_order('Hello@')
    'LHOEZQXJKVBPYGFWMUCDRSNIAT'
    >>> get_frequency_order('h')
    'HZQXJKVBPYGFWMUCLDRSNIOATE'
    """
    letter_to_freq = get_letter_count(message)
    freq_to_letter: dict[int, list[str]] = {
        freq: [] for letter, freq in letter_to_freq.items()
    }
    for letter in LETTERS:
        freq_to_letter[letter_to_freq[letter]].append(letter)

    freq_to_letter_str: dict[int, str] = {}

    for freq in freq_to_letter:
        freq_to_letter[freq].sort(key=ETAOIN.find, reverse=True)
        freq_to_letter_str[freq] = "".join(freq_to_letter[freq])

    freq_pairs = list(freq_to_letter_str.items())
    freq_pairs.sort(key=get_item_at_index_zero, reverse=True)

    freq_order: list[str] = [freq_pair[1] for freq_pair in freq_pairs]

    return "".join(freq_order)


def english_freq_match_score(message: str) -> int:
    """
    >>> english_freq_match_score('Hello World')
    1
    """
    freq_order = get_frequency_order(message)
    match_score = 0
    for common_letter in ETAOIN[:6]:
        if common_letter in freq_order[:6]:
            match_score += 1

    for uncommon_letter in ETAOIN[-6:]:
        if uncommon_letter in freq_order[-6:]:
            match_score += 1

    return match_score


if __name__ == "__main__":
    import doctest

    doctest.testmod()
