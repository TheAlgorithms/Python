"""
The algorithm finds the pattern in given text using following rule.

The bad-character rule considers the mismatched character in Text.
The next occurrence of that character to the left in Pattern is found,

If the mismatched character occurs to the left in Pattern,
a shift is proposed that aligns text block and pattern.

If the mismatched character does not occur to the left in Pattern,
a shift is proposed that moves the entirety of Pattern past
the point of mismatch in the text.

If there is no mismatch then the pattern matches with text block.

Time Complexity : O(n/m)
    n=length of main string
    m=length of pattern string
"""


class BoyerMooreSearch:
    """
    Example usage:

        bms = BoyerMooreSearch(text="ABAABA", pattern="AB")
        positions = bms.bad_character_heuristic()

    where 'positions' contain the locations where the pattern was matched.
    """

    def __init__(self, text: str, pattern: str):
        self.text, self.pattern = text, pattern
        self.textLen, self.patLen = len(text), len(pattern)

    def match_in_pattern(self, char: str) -> int:
        """
        Finds the index of char in pattern in reverse order.

        Parameters :
            char (chr): character to be searched

        Returns :
            i (int): index of char from last in pattern
            -1 (int): if char is not found in pattern

        >>> bms = BoyerMooreSearch(text="ABAABA", pattern="AB")
        >>> bms.match_in_pattern("B")
        1
        """

        for i in range(self.patLen - 1, -1, -1):
            if char == self.pattern[i]:
                return i
        return -1

    def mismatch_in_text(self, current_pos: int) -> int:
        """
        Find the index of mis-matched character in text when compared with pattern
        from last.

        Parameters :
            current_pos (int): current index position of text

        Returns :
            i (int): index of mismatched char from last in text
            -1 (int): if there is no mismatch between pattern and text block

        >>> bms = BoyerMooreSearch(text="ABAABA", pattern="AB")
        >>> bms.mismatch_in_text(2)
        3
        """

        for i in range(self.patLen - 1, -1, -1):
            if self.pattern[i] != self.text[current_pos + i]:
                return current_pos + i
        return -1

    def bad_character_heuristic(self) -> list[int]:
        """
        Finds the positions of the pattern location.

        >>> bms = BoyerMooreSearch(text="ABAABA", pattern="AB")
        >>> bms.bad_character_heuristic()
        [0, 3]
        """

        positions = []
        for i in range(self.textLen - self.patLen + 1):
            mismatch_index = self.mismatch_in_text(i)
            if mismatch_index == -1:
                positions.append(i)
            else:
                match_index = self.match_in_pattern(self.text[mismatch_index])
                i = (
                    mismatch_index - match_index
                )  # shifting index lgtm [py/multiple-definition]
        return positions


if __name__ == "__main__":
    import doctest

    doctest.testmod()
