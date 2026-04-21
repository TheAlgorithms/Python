"""
Sources:
https://en.wikipedia.org/wiki/LZ77_and_LZ78#LZ78
"""

from dataclasses import dataclass

__version__ = "1.0"
__author__ = "Ahmed Tamer"


@dataclass
class Token:
    """
    Dataclass representing pair called token consisting of the dictionary index
    and a single character that follows the phrase in the dictionary.
    """

    index: int
    char: str

    def __repr__(self) -> str:
        """
        >>> token = Token(1, "c")
        >>> repr(token)
        '(1, c)'
        >>> str(token)
        '(1, c)'
        """
        return f"({self.index}, {self.char})"


class LZ78Compressor:
    """
    Class containing compress and decompress methods using LZ78 compression algorithm.
    """

    def compress(self, text: str) -> list[Token]:
        """
        Compress the given string text using LZ78 compression algorithm.

        Args:
          text: string to be compressed

        Returns:
          output: the compressed text as a list of Tokens

        Tests:
          >>> lz78_compressor = LZ78Compressor()
          >>> str(lz78_compressor.compress("ababcbababaa"))
          '[(0, a), (0, b), (1, b), (0, c), (2, a), (5, b), (1, a)]'
          >>> str(lz78_compressor.compress("aacaacabcabaaac"))
          '[(0, a), (1, c), (1, a), (0, c), (1, b), (4, a), (0, b), (3, a)]'
          >>> str(lz78_compressor.compress(""))
          '[]'
          >>> lz78_compressor.compress([])
          Traceback (most recent call last):
          TypeError: Expected string.
          >>> lz78_compressor.compress({})
          Traceback (most recent call last):
          TypeError: Expected string.
          >>> all(len(s) >= len(lz78_compressor.compress(s)) for s in (
          ...     "", "AA", "AB", "AAA", "ABC", "ABCDEFGH"))
          True
        """

        if not isinstance(text, str):
            raise TypeError("Expected string.")

        phrase_dict = {}
        tokens = []
        code = 1
        phrase = ""
        for char in text:
            phrase += char
            if phrase not in phrase_dict:
                phrase_dict[phrase] = str(code)
                if len(phrase) == 1:
                    tokens.append(Token(0, phrase))
                else:
                    tokens.append(Token(int(phrase_dict[phrase[:-1]]), phrase[-1]))
                code += 1
                phrase = ""
        return tokens

    def decompress(self, tokens: list[Token]) -> str:
        """
        Convert the list of tokens into an output string.

        Args:
          tokens: list containing pairs (index, char)

        Returns:
          output: decompressed text

        Tests:
          >>> lz78_compressor = LZ78Compressor()
          >>> lz78_compressor.decompress([Token(0, 'c'), Token(0, 'a'), Token(0, 'b'),
          ... Token(0, 'r'), Token(2, 'c'), Token(2, 'd'), Token(2, 'b'), Token(4, 'a'),
          ... Token(4, 'r'), Token(2, 'r'), Token(8, 'd')])
          'cabracadabrarrarrad'
          >>> lz78_compressor.decompress([Token(0, 'a'), Token(0, 'b'), Token(1, 'b'),
          ... Token(0, 'c'), Token(2, 'a'), Token(5, 'b'), Token(1, 'a')])
          'ababcbababaa'
          >>> lz78_compressor.decompress([Token(0, 'a'), Token(1, 'c'), Token(1, 'a'),
          ... Token(0, 'c'), Token(1, 'b'), Token(4, 'a'),
          ... Token(0, 'b'), Token(3, 'a')])
          'aacaacabcabaaa'
        """

        text = ""
        phrase_dict = {"0": ""}
        code = 1
        for token in tokens:
            phrase = phrase_dict[str(token.index)] + token.char
            phrase_dict[str(code)] = phrase
            code += 1
            text += phrase
        return text


if __name__ == "__main__":
    from doctest import testmod

    testmod()

    lz78_compressor = LZ78Compressor()

    # Example
    text = "aacaacabcabaaa"
    tokens = lz78_compressor.compress(text)
    decompressed_text = lz78_compressor.decompress(tokens)
    assert decompressed_text == text, "Invalid result."
