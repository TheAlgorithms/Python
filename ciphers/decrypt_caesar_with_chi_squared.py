#!/usr/bin/env python3
from __future__ import annotations


def decrypt_caesar_with_chi_squared(
    ciphertext: str,
    cipher_alphabet: list[str] | None = None,
    frequencies_dict: dict[str, float] | None = None,
    case_sensitive: bool = False,
) -> tuple[int, float, str]:
    """
    Basic Usage
    ===========
    Arguments:
    * ciphertext (str): the text to decode (encoded with the caesar cipher)

    Optional Arguments:
    * cipher_alphabet (list): the alphabet used for the cipher (each letter is
      a string separated by commas)
    * frequencies_dict (dict): a dictionary of word frequencies where keys are
      the letters and values are a percentage representation of the frequency as
      a decimal/float
    * case_sensitive (bool): a boolean value: True if the case matters during
      decryption, False if it doesn't

    Returns:
    * A tuple in the form of:
      (
        most_likely_cipher,
        most_likely_cipher_chi_squared_value,
        decoded_most_likely_cipher
      )

      where...
      - most_likely_cipher is an integer representing the shift of the smallest
        chi-squared statistic (most likely key)
      - most_likely_cipher_chi_squared_value is a float representing the
        chi-squared statistic of the most likely shift
      - decoded_most_likely_cipher is a string with the decoded cipher
        (decoded by the most_likely_cipher key)


    The Chi-squared test
    ====================

    The caesar cipher
    -----------------
    The caesar cipher is a very insecure encryption algorithm, however it has
    been used since Julius Caesar. The cipher is a simple substitution cipher
    where each character in the plain text is replaced by a character in the
    alphabet a certain number of characters after the original character. The
    number of characters away is called the shift or key. For example:

    Plain text: hello
    Key: 1
    Cipher text: ifmmp
    (each letter in hello has been shifted one to the right in the eng. alphabet)

    As you can imagine, this doesn't provide lots of security. In fact
    decrypting ciphertext by brute-force is extremely easy even by hand. However
     one way to do that is the chi-squared test.

    The chi-squared test
    -------------------
    Each letter in the english alphabet has a frequency, or the amount of times
    it shows up compared to other letters (usually expressed as a decimal
    representing the percentage likelihood). The most common letter in the
    english language is "e" with a frequency of 0.11162 or 11.162%. The test is
    completed in the following fashion.

    1. The ciphertext is decoded in a brute force way (every combination of the
       26 possible combinations)
    2. For every combination, for each letter in the combination, the average
       amount of times the letter should appear the message is calculated by
       multiplying the total number of characters by the frequency of the letter

       For example:
       In a message of 100 characters, e should appear around 11.162 times.

     3. Then, to calculate the margin of error (the amount of times the letter
        SHOULD appear with the amount of times the letter DOES appear), we use
        the chi-squared test. The following formula is used:

        Let:
        - n be the number of times the letter actually appears
        - p be the predicted value of the number of times the letter should
          appear (see #2)
        - let v be the chi-squared test result (referred to here as chi-squared
          value/statistic)

        (n - p)^2
        --------- = v
           p

    4. Each chi squared value for each letter is then added up to the total.
       The total is the chi-squared statistic for that encryption key.
    5. The encryption key with the lowest chi-squared value is the most likely
       to be the decoded answer.

    Further Reading
    ================

    * http://practicalcryptography.com/cryptanalysis/text-characterisation/chi-squared-
        statistic/
    * https://en.wikipedia.org/wiki/Letter_frequency
    * https://en.wikipedia.org/wiki/Chi-squared_test
    * https://en.m.wikipedia.org/wiki/Caesar_cipher

    Doctests
    ========
    >>> decrypt_caesar_with_chi_squared(
    ...    'dof pz aol jhlzhy jpwoly zv wvwbshy? pa pz avv lhzf av jyhjr!'
    ... )  # doctest: +NORMALIZE_WHITESPACE
    (7, 3129.228005747531,
     'why is the caesar cipher so popular? it is too easy to crack!')

    >>> decrypt_caesar_with_chi_squared('crybd cdbsxq')
    (10, 233.35343938980898, 'short string')

    >>> decrypt_caesar_with_chi_squared('Crybd Cdbsxq', case_sensitive=True)
    (10, 233.35343938980898, 'Short String')

    >>> decrypt_caesar_with_chi_squared(12)
    Traceback (most recent call last):
    AttributeError: 'int' object has no attribute 'lower'
    """
    alphabet_letters = cipher_alphabet or [chr(i) for i in range(97, 123)]

    # If the argument is None or the user provided an empty dictionary
    if not frequencies_dict:
        # Frequencies of letters in the english language (how much they show up)
        frequencies = {
            "a": 0.08497,
            "b": 0.01492,
            "c": 0.02202,
            "d": 0.04253,
            "e": 0.11162,
            "f": 0.02228,
            "g": 0.02015,
            "h": 0.06094,
            "i": 0.07546,
            "j": 0.00153,
            "k": 0.01292,
            "l": 0.04025,
            "m": 0.02406,
            "n": 0.06749,
            "o": 0.07507,
            "p": 0.01929,
            "q": 0.00095,
            "r": 0.07587,
            "s": 0.06327,
            "t": 0.09356,
            "u": 0.02758,
            "v": 0.00978,
            "w": 0.02560,
            "x": 0.00150,
            "y": 0.01994,
            "z": 0.00077,
        }
    else:
        # Custom frequencies dictionary
        frequencies = frequencies_dict

    if not case_sensitive:
        ciphertext = ciphertext.lower()

    # Chi squared statistic values
    chi_squared_statistic_values: dict[int, tuple[float, str]] = {}

    # cycle through all of the shifts
    for shift in range(len(alphabet_letters)):
        decrypted_with_shift = ""

        # decrypt the message with the shift
        for letter in ciphertext:
            try:
                # Try to index the letter in the alphabet
                new_key = (alphabet_letters.index(letter.lower()) - shift) % len(
                    alphabet_letters
                )
                decrypted_with_shift += (
                    alphabet_letters[new_key].upper()
                    if case_sensitive and letter.isupper()
                    else alphabet_letters[new_key]
                )
            except ValueError:
                # Append the character if it isn't in the alphabet
                decrypted_with_shift += letter

        chi_squared_statistic = 0.0

        # Loop through each letter in the decoded message with the shift
        for letter in decrypted_with_shift:
            if case_sensitive:
                letter = letter.lower()
                if letter in frequencies:
                    # Get the amount of times the letter occurs in the message
                    occurrences = decrypted_with_shift.lower().count(letter)

                    # Get the excepcted amount of times the letter should appear based
                    # on letter frequencies
                    expected = frequencies[letter] * occurrences

                    # Complete the chi squared statistic formula
                    chi_letter_value = ((occurrences - expected) ** 2) / expected

                    # Add the margin of error to the total chi squared statistic
                    chi_squared_statistic += chi_letter_value
            elif letter.lower() in frequencies:
                # Get the amount of times the letter occurs in the message
                occurrences = decrypted_with_shift.count(letter)

                # Get the excepcted amount of times the letter should appear based
                # on letter frequencies
                expected = frequencies[letter] * occurrences

                # Complete the chi squared statistic formula
                chi_letter_value = ((occurrences - expected) ** 2) / expected

                # Add the margin of error to the total chi squared statistic
                chi_squared_statistic += chi_letter_value

        # Add the data to the chi_squared_statistic_values dictionary
        chi_squared_statistic_values[shift] = (
            chi_squared_statistic,
            decrypted_with_shift,
        )

    # Get the most likely cipher by finding the cipher with the smallest chi squared
    # statistic
    def chi_squared_statistic_values_sorting_key(key: int) -> tuple[float, str]:
        return chi_squared_statistic_values[key]

    most_likely_cipher: int = min(
        chi_squared_statistic_values,
        key=chi_squared_statistic_values_sorting_key,
    )

    # Get all the data from the most likely cipher (key, decoded message)
    (
        most_likely_cipher_chi_squared_value,
        decoded_most_likely_cipher,
    ) = chi_squared_statistic_values[most_likely_cipher]

    # Return the data on the most likely shift
    return (
        most_likely_cipher,
        most_likely_cipher_chi_squared_value,
        decoded_most_likely_cipher,
    )
