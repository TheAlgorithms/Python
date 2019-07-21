"""
Refrences:
https://en.wikipedia.org/wiki/Bag-of-words_model
@author QuantumNovice

flake8: ignore
bag_of_words.py:21:80: E501 line too long (96 > 79 characters)
bag_of_words.py:24:80: E501 line too long (87 > 79 characters)

black: true
mypy: passed
"""
from typing import List, Dict


def bagOfwords(data: List[str]) -> Dict[str, int]:
    """
    Counts the repitition of words in data.
    >>> data = ['John likes to watch movies. Mary likes movies too']
    >>> bagOfwords(data)
    {'John': 1, 'likes': 2, 'to': 1, 'watch': 1, 'movies.': 1, 'Mary': 1, 'movies': 1, 'too': 1}
    >>> data = ['John also likes to watch football games.']
    >>> bagOfwords(data)
    {'John': 1, 'also': 1, 'likes': 1, 'to': 1, 'watch': 1, 'football': 1, 'games.': 1}
    """
    counter: Dict[str, int] = {}
    for line in data:
        for word in line.split(" "):
            if word in counter:
                counter[word] += 1
            if word not in counter:
                counter[word] = 1
    return counter


if __name__ == "__main__":
    import doctest

    doctest.testmod()
