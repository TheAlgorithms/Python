#!/usr/bin/env python3
import re


def split_words(input_text: str) -> list[str]:
    # The following regex will consider as delimiter whitespaces and punctuation
    words = re.split(r'\s+|[,;.!?"\'-]+', input_text)
    """
    Splitting every word considering whitespaces and also punctuation as delimiters

    >>> input_text = "This is a sample text, with some punctuation!"
    >>> split_words()
    >>> words
    ['This', 'is', 'a', 'sample', 'text', 'with', 'some', 'punctuation']
    """
    # Selecting only non empty elements
    words = [word for word in words if word.strip()]

    return words


def word_frequency(words: list[str]) -> dict[str, int]:
    frequency: dict[str, int] = {}
    """
    Calculate the frequency of words in the input text.

    >>> words = ['this', 'is', 'a', 'sample', 'text', 'with', 'some', 'punctuation']
    >>> word_frequency()
    >>> frequency
    {
        'this': 1,
        'is': 1,
        'a': 1,
        'sample': 1,
        'text': 1,
        'with': 1,
        'some': 1,
        'punctuation': 1
    }
    """
    for word in words:
        # Lower-casing each word to avoid possible repetition due to sensitive case
        word = word.lower()

        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1
    return frequency


def sort_frequency(f: dict[str, int], desc: bool = True) -> dict[str, int]:
    """
    Sort the frequency dictionary by frequency.

    :param f: Frequency dictionary.
    :param desc: True to sort in descending order (default), False for ascending.

    >>> frequency = {'apple': 3, 'banana': 1, 'cherry': 2}
    >>> sort_frequency(frequency)
    {'apple': 3, 'cherry': 2, 'banana': 1}
    >>> sort_frequency(frequency, desc=False)
    {'banana': 1, 'cherry': 2, 'apple': 3}
    """
    sorted_frequency = dict(sorted(f.items(), key=lambda item: item[1], reverse=desc))

    return sorted_frequency


def print_output() -> None:
    input_text = ""
    """
    Calculate word count and word frequency, and print the results.

    >>> input_text = "Riders of Gondor! Of Rohan! My brothers!
    I see in your eyes the same fear that would take the heart of me.
    The day may come when the courage of men fails, but it is not this day.
    An hour of wolves and shattered shields when the age of men comes crashing down,
    but it is not this day! This day, we fight! By all that you hold dear,
    I bid you stand, Men of the West!"
    >>> print_output()
    Provided text includes 79 words.
    Here there is the words' frequency:
    {
        'of': 5,
        'the': 5,
        'is': 4,
        'day': 3,
        'men': 3,
        'this': 3,
        'Riders': 1,
        'Gondor': 1,
        'Of': 1,
        'Rohan': 1,
        'My': 1,
        'brothers': 1,
        'I': 1,
        'see': 1,
        'in': 1,
        'your': 1,
        'eyes': 1,
        'same': 1,
        'fear': 1,
        'that': 1,
        'would': 1,
        'take': 1,
        'heart': 1,
        'me': 1,
        'The': 1,
        'may': 1,
        'come': 1,
        'when': 1,
        'courage': 1,
        'fails': 1,
        'but': 1,
        'it': 1,
        'not': 1,
        'hour': 1,
        'wolves': 1,
        'shattered': 1,
        'shields': 1,
        'age': 1,
        'comes': 1,
        'crashing': 1,
        'down': 1,
        'fight': 1,
        'By': 1,
        'all': 1,
        'you': 1,
        'hold': 1,
        'dear': 1,
        'bid': 1,
        'stand': 1,
        'Men': 1,
        'West': 1
    }
    """
    words = split_words(input_text)
    print(input_text)
    m = f"Provided text includes {len(words)} words.\n"
    m += "Here there is the words' frequency:\n{sort_frequency(word_frequency(words))}"
    print(m)


def main():
    import doctest

    doctest.testmod()


if __name__ == "__main__":
    main()
