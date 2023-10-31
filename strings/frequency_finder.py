# Frequency Finder

import string

# Frequency of each English letter taken from https://en.wikipedia.org/wiki/Letter_frequency
english_letter_freq = {
    # Letter frequencies in percentages
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

# Ordering of English letters from most to least frequent
ETAOIN = "ETAOINSHRDLCUMWFGYPBVKJXQZ"
LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def get_letter_count(message: str) -> dict[str, int]:
    """
    Count the occurrence of each letter in the given message.
    """
    # Initialize a dictionary to store the count of each letter
    letter_count = {letter: 0 for letter in string.ascii_uppercase}

    # Count each uppercase letter in the message
    for letter in message.upper():
        if letter in LETTERS:
            letter_count[letter] += 1

    return letter_count


def get_item_at_index_zero(x: tuple) -> str:
    """
    Helper function to get the first item in a tuple.
    """
    return x[0]


def get_frequency_order(message: str) -> str:
    """
    Get the frequency order of the letters in the given message.
    """
    # Get the letter count in the message
    letter_to_freq = get_letter_count(message)

    # Create a dictionary to map frequency to letters
    freq_to_letter = {freq: [] for letter, freq in letter_to_freq.items()}

    # Populate the dictionary
    for letter in LETTERS:
        freq_to_letter[letter_to_freq[letter]].append(letter)

    # Create a dictionary to store sorted letters for each frequency
    freq_to_letter_str = {}
    for freq in freq_to_letter:
        freq_to_letter[freq].sort(key=ETAOIN.find, reverse=True)
        freq_to_letter_str[freq] = "".join(freq_to_letter[freq])

    # Sort by frequency
    freq_pairs = list(freq_to_letter_str.items())
    freq_pairs.sort(key=get_item_at_index_zero, reverse=True)

    # Create a string of letters sorted by their frequency in the message
    freq_order = [freq_pair[1] for freq_pair in freq_pairs]

    return "".join(freq_order)


def english_freq_match_score(message: str) -> int:
    """
    Calculate a match score based on how many of the six most frequent
    and six least frequent letters are present in the message.
    """
    freq_order = get_frequency_order(message)
    match_score = 0

    # Check how many of the six most common English letters are in the most common letters of the message
    for common_letter in ETAOIN[:6]:
        if common_letter in freq_order[:6]:
            match_score += 1

    # Check how many of the six least common English letters are in the least common letters of the message
    for uncommon_letter in ETAOIN[-6:]:
        if uncommon_letter in freq_order[-6:]:
            match_score += 1

    return match_score


if __name__ == "__main__":
    import doctest

    doctest.testmod()
