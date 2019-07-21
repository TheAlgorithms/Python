"""
Refrences:
https://en.wikipedia.org/wiki/Bag-of-words_model
@author QuantumNovice

flake8: passed
black: true
mypy: passed
"""
from typing import List, Dict
from collections import Counter


def bagOfwords(data: List[str]) -> Dict[str, int]:
    """
    Counts the repitition of words in data.
    >>> data = ['John likes to watch movies. Mary likes movies too']
    >>> bagOfwords(data) # doctest: +NORMALIZE_WHITESPACE +ELLIPSIS
    {'John': 1, 'likes': 2, 'to': 1, ... 'movies': 1, 'too': 1}
    >>> data = ['John also likes to watch football games.']
    >>> bagOfwords(data) # doctest: +NORMALIZE_WHITESPACE +ELLIPSIS
    {'John': 1, 'also': 1, ... 'football': 1, 'games.': 1}
    """
    counter: Dict[str, int] = {}
    for line in data:
        counter = dict(Counter(line.split(" ")))
    return counter


if __name__ == "__main__":
    import doctest

    doctest.testmod()
