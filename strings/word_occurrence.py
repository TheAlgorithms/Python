# Created by sarathkaul on 17/11/19
# Modified by Arkadip Bhattacharya(@darkmatter18) on 20/04/2020

def word_occurence(sentence: str) -> dict:
    """
    >>> word_occurence("Two  spaces")
    {'Two': 1, 'spaces': 1}
    """
    from collections import defaultdict
    occurrence = defaultdict(int)
    # Creating a dictionary containing count of each word
    for word in sentence.split():
        occurrence[word] += 1
    return occurrence


if __name__ == "__main__":
    from doctest import testmod

    testmod()
