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
    ['I ', ' a', 'am', 'm ', ' a', 'a ', ' s', 'se', 'en', 'nt', 'te', 'en', 'nc', 'ce']
    >>> create_ngram("I am an NLPer", 2)
    ['I ', ' a', 'am', 'm ', ' a', 'an', 'n ', ' N', 'NL', 'LP', 'Pe', 'er']
    """

    ngrams = []
    for i in range(len(sentence) - ngram_size + 1):
        ngrams.append(sentence[i : i + ngram_size])
    return ngrams


if __name__ == "__main__":
    from doctest import testmod

    testmod()
