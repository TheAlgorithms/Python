# Created by sarathkaul on 17/11/19
from collections import defaultdict


def word_occurence(sentence: str) -> dict:
    """
    >>> from collections import Counter
    >>> SENTENCE = "a b A b c b d b d e f e g e h e i e j e 0"
    >>> occurence_dict = word_occurence(SENTENCE)
    >>> all(occurence_dict[word] == count for word, count
    ...     in Counter(SENTENCE.split()).items())
    True
    """
    occurence = defaultdict(int)
    # Creating a dictionary containing count of each word
    for word in sentence.split(" "):
        occurence[word] += 1
    return occurence


if __name__ == "__main__":
    for word, count in word_occurence("INPUT STRING").items():
        print(f"{word}: {count}")
