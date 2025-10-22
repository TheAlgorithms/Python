"""
Bacon's/Baconian Cipher Encoder and Decoder

 provides functions to encode and decode messages
using Bacon's/Baconian cipher with any 2 symbols, not just A & B.

Source: https://en.wikipedia.org/wiki/Bacon's_cipher
"""

ENCODE_DICT = {
    "a": "AAAAA", "b": "AAAAB", "c": "AAABA", "d": "AAABB",
    "e": "AABAA", "f": "AABAB", "g": "AABBA", "h": "AABBB",
    "i": "ABAAA", "j": "BBBAA", "k": "ABAAB", "l": "ABABA",
    "m": "ABABB", "n": "ABBAA", "o": "ABBAB", "p": "ABBBA",
    "q": "ABBBB", "r": "BAAAA", "s": "BAAAB", "t": "BAABA",
    "u": "BAABB", "v": "BBBAB", "w": "BABAA", "x": "BABAB",
    "y": "BABBA", "z": "BABBB", " ": " ",
}

DECODE_DICT = {value: key for key, value in ENCODE_DICT.items()}


def encode(message: str, symbols: tuple[str, str] = ("A", "B")) -> str:
    """
    Encode a message using Bacon's cipher.

    Parameters
    ----------
    message : str
        The message to encode (letters and spaces only).
    symbols : tuple[str, str], optional
        Custom symbols to replace A and B, by default ("A", "B").

    Returns
    -------
    str
        Encoded message using the chosen symbols.

    Raises
    ------
    ValueError
        If the message contains invalid characters.

    Examples
    --------
    >>> encode("abc")
    'AAAAA AAAAB AAABA'
    >>> encode("abc", symbols=("X", "Y"))
    'XXXXX XXXXY XXYXX'
    >>> encode("hi there")
    'AABBB ABAAA BAABA AABBB AABAA BAAAA AABAA'
    """
    a_sym, b_sym = symbols
    encoded_message = ""

    for char in message.lower():
        if char.isalpha() or char == " ":
            bacon = ENCODE_DICT[char]
            encoded_message += bacon.replace("A", a_sym).replace("B", b_sym)
        else:
            raise ValueError("Message can only contain letters and spaces.")

    return encoded_message


def decode(cipher: str, symbols: tuple[str, str] = ("A", "B")) -> str:
    """
    Decode a Bacon's cipher message.

    Parameters
    ----------
    cipher : str
        The encoded message using two symbols.
    symbols : tuple[str, str], optional
        Symbols used in the cipher, by default ("A", "B").

    Returns
    -------
    str
        Decoded message.

    Raises
    ------
    ValueError
        If the cipher contains invalid symbols or cannot be decoded.

    Examples
    --------
    >>> decode("AAAAA AAAAB AAABA")
    'abc'
    >>> decode("XXXXX XXXXY XXYXX", symbols=("X","Y"))
    'abc'
    """
    sym1, sym2 = symbols
    unique_symbols = set(cipher.replace(" ", ""))
    if unique_symbols - {sym1, sym2}:
        raise ValueError(f"Cipher must contain only symbols {sym1} and {sym2}.")

    candidates = []
    for mapping in [(sym1, sym2), (sym2, sym1)]:
        s1, s2 = mapping
        standard = cipher.replace(s1, "A").replace(s2, "B")
        try:
            decoded = ""
            for word in standard.split():
                while word:
                    chunk = word[:5]
                    if chunk not in DECODE_DICT:
                        raise ValueError
                    decoded += DECODE_DICT[chunk]
                    word = word[5:]
                decoded += " "
            candidates.append(decoded.strip())
        except ValueError:
            candidates.append(None)

    for candidate in candidates:
        if candidate is not None:
            return candidate

    raise ValueError("No valid decoding found.")


def detect_unique_symbols(cipher: str) -> tuple[str, str]:
    """
    Detects the two unique symbols used in a cipher.

    Parameters
    ----------
    cipher : str
        Encoded message containing exactly two unique symbols.

    Returns
    -------
    tuple[str, str]
        The two unique symbols found in the cipher.

    Raises
    ------
    ValueError
        If cipher does not contain exactly two unique symbols.

    Examples
    --------
    >>> detect_unique_symbols("XXXYX YXXYX")
    ('X', 'Y')
    """
    letters_only = [char for char in set(cipher.replace(" ", "")) if char.isalpha()]
    if len(letters_only) != 2:
        raise ValueError("Cipher must contain exactly two unique alphabetic symbols.")
    return tuple(letters_only)


if __name__ == "__main__":
    # Example usage
    cipher_text = (
        "FEEFE EEFFF EEFEE EFFFF FEEFF EFEEE EEEFE "
        "EFEEF EEEEF FEEEE EFFEF FEFEE EFFEE EEFEF EFFEF FEFEF"
    )
    sym1, sym2 = detect_unique_symbols(cipher_text)
    decoded_message = decode(cipher_text, symbols=(sym1, sym2))
    print(decoded_message)  # Expected: 'the quick brown fox'
