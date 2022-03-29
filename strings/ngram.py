def create_ngram(sentence: str, ngram_size: int) -> list:
    """
    Create ngrams from a sentence
    :param sentence: str
    :param ngram_size: int
    :return: list
    """

    ngrams = []
    for i in range(len(sentence) - ngram_size + 1):
        ngrams.append(sentence[i : i + ngram_size])
    return ngrams


ngram_size = 2
create_ngram("I am an NLPer", ngram_size)
