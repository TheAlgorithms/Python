"""
The nth term of the sequence of triangle numbers is given by, tn = ½n(n+1); so
the first ten triangle numbers are:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

By converting each letter in a word to a number corresponding to its
alphabetical position and adding these values we form a word value. For example,
the word value for SKY is 19 + 11 + 25 = 55 = t10. If the word value is a
triangle number then we shall call the word a triangle word.

Using words.txt (right click and 'Save Link/Target As...'), a 16K text file
containing nearly two-thousand common English words, how many are triangle
words?
"""
import os

# Precomputes a list of the 100 first triangular numbers
TRIANGULAR_NUMBERS = [int(0.5 * n * (n + 1)) for n in range(1, 101)]


def solution():
    """
    Finds the amount of triangular words in the words file.

    >>> solution()
    162
    """
    script_dir = os.path.dirname(os.path.realpath(__file__))
    words_file_path = os.path.join(script_dir, "words.txt")

    words = ""
    with open(words_file_path) as f:
        words = f.readline()

    words = [word.strip('"') for word in words.strip("\r\n").split(",")]
    words = list(
        filter(
            lambda word: word in TRIANGULAR_NUMBERS,
            (sum(ord(x) - 64 for x in word) for word in words),
        )
    )
    return len(words)


if __name__ == "__main__":
    print(solution())
