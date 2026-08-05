"""
Move to Front (MTF) is a data compression technique that reorders
symbols based on their frequency of occurrence.
    - type of context based methods
    - it lays somewhere between coding and transforming data
    - it is core of the Burrows-Wheeler Transform (BWT)
    - for simplicity we do not distinguish between upper and lower case


Sources:
    - https://en.wikipedia.org/wiki/Move-to-front_transform
    - https://www.mbit.edu.in/wp-content/uploads/2020/05/data_compression.pdf
        (chapter 6.4.1)
"""

english_alphabet = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
]


class MoveToFront:
    """
    Core class doing encoding and also decoding.

    >>> mtf = MoveToFront()
    >>> list(mtf.encode_text("algorithm"))
    [0, 11, 7, 14, 17, 11, 19, 12, 15]
    >>> mtf.decode_text([0, 11, 7, 14, 17, 11, 19, 12, 15])
    'algorithm'
    """

    def __init__(self, source_alphabet: list[str] = english_alphabet) -> None:
        """
        If the source alphabet is not provided, it will be set to the english.
        The class does not distinguish between UPPER and lower case.
        """
        self.source_alphabet = list(source_alphabet)

    def encode_text(self, plain_text: str) -> list[int]:
        """
        Encodes given text. The output is list of char positions in the alphabet.

        >>> mtf = MoveToFront()
        >>> list(mtf.encode_text("algorithm"))
        [0, 11, 7, 14, 17, 11, 19, 12, 15]
        """

        if not isinstance(plain_text, str):
            raise TypeError("The parameter plain_text type must be str.")

        # making a copy so we do not rotate the original alphabet
        alphabet = list(self.source_alphabet)
        encoded_text = []

        for char in plain_text.lower():
            # find the position of the char in the alphabet and add it to the result
            char_position_in_alphabet = alphabet.index(char)
            encoded_text.append(char_position_in_alphabet)

            # move our char to the front of the alphabet
            alphabet.pop(char_position_in_alphabet)
            alphabet.insert(0, char)

        return encoded_text

    def decode_text(self, compressed_text: list[int]) -> str:
        """
        Decodes given text. The input is list of char positions in the alphabet.

        >>> mtf = MoveToFront()
        >>> mtf.decode_text([0, 11, 7, 14, 17, 11, 19, 12, 15])
        'algorithm'
        """

        alphabet = list(self.source_alphabet)
        decoded_text = []

        for idx in compressed_text:
            # find corresponding chart to given index
            char = alphabet[idx]
            decoded_text.append(char)

            # move found char to the front of the alphabet
            alphabet.pop(idx)
            alphabet.insert(0, char)

        return "".join(decoded_text)


if __name__ == "__main__":
    mtf = MoveToFront()
    print(mtf.encode_text("algorithm"))
    print(mtf.decode_text([0, 11, 7, 14, 17, 11, 19, 12, 15]))
