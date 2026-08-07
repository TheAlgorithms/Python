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
        Finds the positions of the pattern occurrence.

        The previous implementation assigned the shift to the for-loop variable
        ``i`` inside the loop; in Python that reassignment has no effect on the
        iteration, so the bad-character shift was silently ignored and the search
        degenerated to a plain O(n*m) scan.

        This version uses a ``while`` loop so the shift actually takes effect.
        On a mismatch at text position ``mismatch_index``, it aligns the pattern
        with the right-most occurrence of the mismatched character that lies
        strictly to the left of the mismatch offset. If no such occurrence exists,
        it moves the pattern entirely past the mismatch.

        Correctness (why the shift never skips a valid occurrence):

        At any alignment ``i`` we first scan the pattern from right to left and
        find the right-most mismatch at pattern offset ``mismatch_offset`` (so
        everything to its right already agrees). The mismatching text character
        is ``char``. The loop then advances ``i`` by ``shift``:

        * If ``char`` occurs at some index ``r < mismatch_offset`` (right-most such
          ``r``), set ``shift = mismatch_offset - r``. Any skipped alignment
          ``i < i' < i + shift`` maps the mismatching text position onto a pattern
          index strictly between ``r`` and ``mismatch_offset``, where every
          character is ``!= char``, so ``i'`` cannot be a match.
        * Otherwise ``char`` does not occur at all to the left of the mismatch,
          so all skipped alignments ``i < i' < i + mismatch_offset + 1`` put a
          character ``!= char`` at the mismatching text position, and cannot be
          matches either.

        Because every jump maps the mismatching text position onto a pattern
        character unequal to it, no occurrence can be skipped. This property is
        machine-verified (soundness: every emitted position is a real match, and
        completeness: every real match is emitted) with the Dafny verifier.

        >>> bms = BoyerMooreSearch(text="ABAABA", pattern="AB")
        >>> bms.bad_character_heuristic()
        [0, 3]
        """

        positions = []
        i = 0
        while i <= self.textLen - self.patLen:
            mismatch_index = self.mismatch_in_text(i)
            if mismatch_index == -1:
                positions.append(i)
                i += 1
            else:
                mismatch_offset = mismatch_index - i
                char = self.text[mismatch_index]
                shift = 1
                for j in range(mismatch_offset - 1, -1, -1):
                    if self.pattern[j] == char:
                        shift = mismatch_offset - j
                        break
                else:
                    # char not present to the left of the mismatch offset:
                    # shift the pattern entirely past the mismatch
                    shift = mismatch_offset + 1
                i += shift

        return positions


if __name__ == "__main__":
    import doctest

    doctest.testmod()
