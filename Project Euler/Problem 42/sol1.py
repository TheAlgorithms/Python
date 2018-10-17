# -*- coding: utf-8 -*-
from __future__ import print_function
import re

try:
    raw_input          # Python 2
    xrange
except NameError:
    raw_input = input  # Python 3
    xrange = range

'''
Coded triangle numbers
Problem 42

The nth term of the sequence of triangle numbers is given by, tn = ½n(n+1);
so the first ten triangle numbers are:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

By converting each letter in a word to a number corresponding to its
alphabetical position and adding these values we form a word value. For
example,the word value for SKY is 19 + 11 + 25 = 55 = t10. If the word value is
a triangle number then we shall call the word a triangle word.

Using words.txt (right click and 'Save Link/Target As...'), a 16K text file
containing nearly two-thousand common English words, how many are triangle
words?
'''

triangularNumbers = list(map(lambda n: int(0.5 * n * (n + 1)), xrange(1, 101)))
words = re.findall(r'\w+', open('words.txt').readline(), re.IGNORECASE)
words = list(
    map(
        lambda word: reduce(
            lambda x, y: x + y,
            map(lambda x: ord(x) % 64, word)
        ),
        words
    )
)

print(len(filter(lambda x: x in triangularNumbers, words)))
