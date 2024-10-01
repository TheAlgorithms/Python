"""
Program to encode and decode using Baconian (Bacon's) Cipher.
Wikipedia reference: https://en.wikipedia.org/wiki/Bacon%27s_cipher
"""

# Dictionary for encoding letters into Baconian cipher
encode_dict = {
    "a": "AAAAA", "b": "AAAAB", "c": "AAABA", "d": "AAABB", "e": "AABAA",
    "f": "AABAB", "g": "AABBA", "h": "AABBB", "i": "ABAAA", "j": "BBBAA",
    "k": "ABAAB", "l": "ABABA", "m": "ABABB", "n": "ABBAA", "o": "ABBAB",
    "p": "ABBBA", "q": "ABBBB", "r": "BAAAA", "s": "BAAAB", "t": "BAABA",
    "u": "BAABB", "v": "BBBAB", "w": "BABAA", "x": "BABAB", "y": "BABBA",
    "z": "BABBB", " ": " "
}

# Reverse dictionary for decoding Baconian cipher back into letters
decode_dict = {value: key for key, value in encode_dict.items()}

def encode(word: str) -> str:
    """
    Encodes a given word into Baconian cipher.
    
    Only letters of the alphabet and spaces are accepted. Any other characters will raise a ValueError.
    
    Args:
        word (str): The word or phrase to encode.
    
    Returns:
        str: The encoded message in Baconian cipher.
    
    Raises:
        ValueError: If the input contains characters other than letters and spaces.

    Examples:
        >>> encode("hello")
        'AABBBAABAAABABAABABAABBAB'
        >>> encode("hello world")
        'AABBBAABAAABABAABABAABBAB BABAAABBABBAAAAABABAAAABB'
        >>> encode("hello world!")
        Traceback (most recent call last):
            ...
        ValueError: encode() accepts only letters of the alphabet and spaces
    """
    encoded = []
    for letter in word.lower():
        if letter in encode_dict:
            encoded.append(encode_dict[letter])
        else:
            raise ValueError("encode() accepts only letters of the alphabet and spaces")
    return ''.join(encoded)

def decode(coded: str) -> str:
    """
    Decodes a Baconian cipher message back into plain text.
    
    The message must contain only 'A', 'B', and spaces. Other characters will raise a ValueError.
    
    Args:
        coded (str): The encoded message to decode.
    
    Returns:
        str: The decoded plain text message.
    
    Raises:
        ValueError: If the input contains characters other than 'A', 'B', and spaces.

    Examples:
        >>> decode("AABBBAABAAABABAABABAABBAB BABAAABBABBAAAAABABAAAABB")
        'hello world'
        >>> decode("AABBBAABAAABABAABABAABBAB")
        'hello'
        >>> decode("AABBBAABAAABABAABABAABBAB BABAAABBABBAAAAABABAAAABB!")
        Traceback (most recent call last):
            ...
        ValueError: decode() accepts only 'A', 'B' and spaces
    """
    if set(coded) - {"A", "B", " "}:
        raise ValueError("decode() accepts only 'A', 'B' and spaces")
    
    decoded = []
    for word in coded.split():
        for i in range(0, len(word), 5):
            chunk = word[i:i+5]
            decoded.append(decode_dict.get(chunk, ''))
        decoded.append(' ')  # Add space between words
    
    return ''.join(decoded).strip()

if __name__ == "__main__":
    from doctest import testmod
    testmod()
