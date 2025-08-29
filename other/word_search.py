"""
Creates a random wordsearch with eight different directions
that are best described as compass locations.

@ https://en.wikipedia.org/wiki/Word_search
"""

from random import choice, randint, shuffle

# The words to display on the word search -
# can be made dynamic by randonly selecting a certain number of
# words from a predefined word file, while ensuring the character
# count fits within the matrix size (n x m)
WORDS = ["cat", "dog", "snake", "fish"]

WIDTH = 10
HEIGHT = 10


class WordSearch:
    """
    >>> ws = WordSearch(WORDS, WIDTH, HEIGHT)
    >>> ws.board  # doctest: +ELLIPSIS
    [[None, ..., None], ..., [None, ..., None]]
    >>> ws.generate_board()
    """

    def __init__(self, words: list[str], width: int, height: int) -> None:
        self.words = words
        self.width = width
        self.height = height

        # Board matrix holding each letter
        self.board: list[list[str | None]] = [[None] * width for _ in range(height)]

    def insert_north(self, word: str, rows: list[int], cols: list[int]) -> None:
        """
        >>> ws = WordSearch(WORDS, 3, 3)
        >>> ws.insert_north("cat", [2], [2])
        >>> ws.board  # doctest: +NORMALIZE_WHITESPACE
        [[None, None, 't'],
        [None, None, 'a'],
        [None, None, 'c']]
        >>> ws.insert_north("at", [0, 1, 2], [2, 1])
        >>> ws.board  # doctest: +NORMALIZE_WHITESPACE
        [[None, 't', 't'],
        [None, 'a', 'a'],
        [None, None, 'c']]
        """
        word_length = len(word)
        # Attempt to insert the word into each row and when successful, exit
        for row in rows:
            # Check if there is space above the row to fit in the word
            if word_length > row + 1:
                continue

            # Attempt to insert the word into each column
            for col in cols:
                # Only check to be made here is if there are existing letters
                # above the column that will be overwritten
                letters_above = [self.board[row - i][col] for i in range(word_length)]
                if all(letter is None for letter in letters_above):
                    # Successful, insert the word north
                    for i in range(word_length):
                        self.board[row - i][col] = word[i]
                    return

    def insert_northeast(self, word: str, rows: list[int], cols: list[int]) -> None:
        """
        >>> ws = WordSearch(WORDS, 3, 3)
        >>> ws.insert_northeast("cat", [2], [0])
        >>> ws.board  # doctest: +NORMALIZE_WHITESPACE
        [[None, None, 't'],
        [None, 'a', None],
        ['c', None, None]]
        >>> ws.insert_northeast("at", [0, 1], [2, 1, 0])
        >>> ws.board  # doctest: +NORMALIZE_WHITESPACE
        [[None, 't', 't'],
        ['a', 'a', None],
        ['c', None, None]]
        """
        word_length = len(word)
        # Attempt to insert the word into each row and when successful, exit
        for row in rows:
            # Check if there is space for the word above the row
            if word_length > row + 1:
                continue

            # Attempt to insert the word into each column
            for col in cols:
                # Check if there is space to the right of the word as well as above
                if word_length + col > self.width:
                    continue

                # Check if there are existing letters
                # to the right of the column that will be overwritten
                letters_diagonal_left = [
                    self.board[row - i][col + i] for i in range(word_length)
                ]
                if all(letter is None for letter in letters_diagonal_left):
                    # Successful, insert the word northeast
                    for i in range(word_length):
                        self.board[row - i][col + i] = word[i]
                    return

    def insert_east(self, word: str, rows: list[int], cols: list[int]) -> None:
        """
        >>> ws = WordSearch(WORDS, 3, 3)
        >>> ws.insert_east("cat", [1], [0])
        >>> ws.board  # doctest: +NORMALIZE_WHITESPACE
        [[None, None, None],
        ['c', 'a', 't'],
        [None, None, None]]
        >>> ws.insert_east("at", [1, 0], [2, 1, 0])
        >>> ws.board  # doctest: +NORMALIZE_WHITESPACE
        [[None, 'a', 't'],
        ['c', 'a', 't'],
        [None, None, None]]
        """
        word_length = len(word)
        # Attempt to insert the word into each row and when successful, exit
        for row in rows:
            # Attempt to insert the word into each column
            for col in cols:
                # Check if there is space to the right of the word
                if word_length + col > self.width:
                    continue

                # Check if there are existing letters
                # to the right of the column that will be overwritten
                letters_left = [self.board[row][col + i] for i in range(word_length)]
                if all(letter is None for letter in letters_left):
                    # Successful, insert the word east
                    for i in range(word_length):
                        self.board[row][col + i] = word[i]
                    return

    def insert_southeast(self, word: str, rows: list[int], cols: list[int]) -> None:
        """
        >>> ws = WordSearch(WORDS, 3, 3)
        >>> ws.insert_southeast("cat", [0], [0])
        >>> ws.board  # doctest: +NORMALIZE_WHITESPACE
        [['c', None, None],
        [None, 'a', None],
        [None, None, 't']]
        >>> ws.insert_southeast("at", [1, 0], [2, 1, 0])
        >>> ws.board  # doctest: +NORMALIZE_WHITESPACE
        [['c', None, None],
        ['a', 'a', None],
        [None, 't', 't']]
        """
        word_length = len(word)
        # Attempt to insert the word into each row and when successful, exit
        for row in rows:
            # Check if there is space for the word below the row
            if word_length + row > self.height:
                continue

            # Attempt to insert the word into each column
            for col in cols:
                # Check if there is space to the right of the word as well as below
                if word_length + col > self.width:
                    continue

                # Check if there are existing letters
                # to the right of the column that will be overwritten
                letters_diagonal_left = [
                    self.board[row + i][col + i] for i in range(word_length)
                ]
                if all(letter is None for letter in letters_diagonal_left):
                    # Successful, insert the word southeast
                    for i in range(word_length):
                        self.board[row + i][col + i] = word[i]
                    return

    def insert_south(self, word: str, rows: list[int], cols: list[int]) -> None:
        """
        >>> ws = WordSearch(WORDS, 3, 3)
        >>> ws.insert_south("cat", [0], [0])
        >>> ws.board  # doctest: +NORMALIZE_WHITESPACE
        [['c', None, None],
        ['a', None, None],
        ['t', None, None]]
        >>> ws.insert_south("at", [2, 1, 0], [0, 1, 2])
        >>> ws.board  # doctest: +NORMALIZE_WHITESPACE
        [['c', None, None],
        ['a', 'a', None],
        ['t', 't', None]]
        """
        word_length = len(word)
        # Attempt to insert the word into each row and when successful, exit
        for row in rows:
            # Check if there is space below the row to fit in the word
            if word_length + row > self.height:
                continue

            # Attempt to insert the word into each column
            for col in cols:
                # Only check to be made here is if there are existing letters
                # below the column that will be overwritten
                letters_below = [self.board[row + i][col] for i in range(word_length)]
                if all(letter is None for letter in letters_below):
                    # Successful, insert the word south
                    for i in range(word_length):
                        self.board[row + i][col] = word[i]
                    return

    def insert_southwest(self, word: str, rows: list[int], cols: list[int]) -> None:
        """
        >>> ws = WordSearch(WORDS, 3, 3)
        >>> ws.insert_southwest("cat", [0], [2])
        >>> ws.board  # doctest: +NORMALIZE_WHITESPACE
        [[None, None, 'c'],
        [None, 'a', None],
        ['t', None, None]]
        >>> ws.insert_southwest("at", [1, 2], [2, 1, 0])
        >>> ws.board  # doctest: +NORMALIZE_WHITESPACE
        [[None, None, 'c'],
        [None, 'a', 'a'],
        ['t', 't', None]]
        """
        word_length = len(word)
        # Attempt to insert the word into each row and when successful, exit
        for row in rows:
            # Check if there is space for the word below the row
            if word_length + row > self.height:
                continue

            # Attempt to insert the word into each column
            for col in cols:
                # Check if there is space to the left of the word as well as below
                if word_length > col + 1:
                    continue

                # Check if there are existing letters
                # to the right of the column that will be overwritten
                letters_diagonal_left = [
                    self.board[row + i][col - i] for i in range(word_length)
                ]
                if all(letter is None for letter in letters_diagonal_left):
                    # Successful, insert the word southwest
                    for i in range(word_length):
                        self.board[row + i][col - i] = word[i]
                    return

    def insert_west(self, word: str, rows: list[int], cols: list[int]) -> None:
        """
        >>> ws = WordSearch(WORDS, 3, 3)
        >>> ws.insert_west("cat", [1], [2])
        >>> ws.board  # doctest: +NORMALIZE_WHITESPACE
        [[None, None, None],
        ['t', 'a', 'c'],
        [None, None, None]]
        >>> ws.insert_west("at", [1, 0], [1, 2, 0])
        >>> ws.board  # doctest: +NORMALIZE_WHITESPACE
        [['t', 'a', None],
        ['t', 'a', 'c'],
        [None, None, None]]
        """
        word_length = len(word)
        # Attempt to insert the word into each row and when successful, exit
        for row in rows:
            # Attempt to insert the word into each column
            for col in cols:
                # Check if there is space to the left of the word
                if word_length > col + 1:
                    continue

                # Check if there are existing letters
                # to the left of the column that will be overwritten
                letters_left = [self.board[row][col - i] for i in range(word_length)]
                if all(letter is None for letter in letters_left):
                    # Successful, insert the word west
                    for i in range(word_length):
                        self.board[row][col - i] = word[i]
                    return

    def insert_northwest(self, word: str, rows: list[int], cols: list[int]) -> None:
        """
        >>> ws = WordSearch(WORDS, 3, 3)
        >>> ws.insert_northwest("cat", [2], [2])
        >>> ws.board  # doctest: +NORMALIZE_WHITESPACE
        [['t', None, None],
        [None, 'a', None],
        [None, None, 'c']]
        >>> ws.insert_northwest("at", [1, 2], [0, 1])
        >>> ws.board  # doctest: +NORMALIZE_WHITESPACE
        [['t', None, None],
        ['t', 'a', None],
        [None, 'a', 'c']]
        """
        word_length = len(word)
        # Attempt to insert the word into each row and when successful, exit
        for row in rows:
            # Check if there is space for the word above the row
            if word_length > row + 1:
                continue

            # Attempt to insert the word into each column
            for col in cols:
                # Check if there is space to the left of the word as well as above
                if word_length > col + 1:
                    continue

                # Check if there are existing letters
                # to the right of the column that will be overwritten
                letters_diagonal_left = [
                    self.board[row - i][col - i] for i in range(word_length)
                ]
                if all(letter is None for letter in letters_diagonal_left):
                    # Successful, insert the word northwest
                    for i in range(word_length):
                        self.board[row - i][col - i] = word[i]
                    return

    def generate_board(self) -> None:
        """
        Generates a board with a random direction for each word.

        >>> wt = WordSearch(WORDS, WIDTH, HEIGHT)
        >>> wt.generate_board()
        >>> len(list(filter(lambda word: word is not None, sum(wt.board, start=[])))
        ... ) == sum(map(lambda word: len(word), WORDS))
        True
        """
        directions = (
            self.insert_north,
            self.insert_northeast,
            self.insert_east,
            self.insert_southeast,
            self.insert_south,
            self.insert_southwest,
            self.insert_west,
            self.insert_northwest,
        )
        for word in self.words:
            # Shuffle the row order and column order that is used when brute forcing
            # the insertion of the word
            rows, cols = list(range(self.height)), list(range(self.width))
            shuffle(rows)
            shuffle(cols)

            # Insert the word via the direction
            choice(directions)(word, rows, cols)


def visualise_word_search(
    board: list[list[str | None]] | None = None, *, add_fake_chars: bool = True
) -> None:
    """
    Graphically displays the word search in the terminal.

    >>> ws = WordSearch(WORDS, 5, 5)
    >>> ws.insert_north("cat", [4], [4])
    >>> visualise_word_search(
    ...     ws.board, add_fake_chars=False)  # doctest: +NORMALIZE_WHITESPACE
    # # # # #
    # # # # #
    # # # # t
    # # # # a
    # # # # c
    >>> ws.insert_northeast("snake", [4], [4, 3, 2, 1, 0])
    >>> visualise_word_search(
    ...     ws.board, add_fake_chars=False)  # doctest: +NORMALIZE_WHITESPACE
    # # # # e
    # # # k #
    # # a # t
    # n # # a
    s # # # c
    """
    if board is None:
        word_search = WordSearch(WORDS, WIDTH, HEIGHT)
        word_search.generate_board()
        board = word_search.board

    result = ""
    for row in range(len(board)):
        for col in range(len(board[0])):
            character = "#"
            if (letter := board[row][col]) is not None:
                character = letter
            # Empty char, so add a fake char
            elif add_fake_chars:
                character = chr(randint(97, 122))
            result += f"{character} "
        result += "\n"
    print(result, end="")


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    visualise_word_search()
