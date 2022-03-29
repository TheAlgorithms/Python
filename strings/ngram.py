"""
https://en.wikipedia.org/wiki/N-gram


"""


def create_ngram(sentence: str, ngram_size: int) -> list:
    """
    Create ngrams from a sentence
    :param sentence: str
    :param ngram_size: int
    :return: list

    >>> create_ngram("I am a sentence", 2)
    ['I ', 'am', ' a', 'm ', 'a ', 'sentence']
    >>> create_ngram("I am an NLPer", 2)
    ['I ', ' a', 'am', 'm ', ' a', 'an', 'n ', ' N', 'NL', 'LP', 'Pe', 'er']

    """

    ngrams = []
    for i in range(len(sentence) - ngram_size + 1):
        ngrams.append(sentence[i : i + ngram_size])
    return ngrams


if __name__ == "__main__":
    ngram_size = 2
    print(create_ngram("I am a sentence", ngram_size))
