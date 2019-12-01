# Created by sarathkaul on 18/11/19


def reverse_words(input_str: str) -> str:
    """
    Reverses words in a given string
    >>> sentence = "I love Python"
    >>> reverse_words(sentence) == " ".join(sentence.split()[::-1])
    True
    >>> reverse_words(sentence)
    'Python love I'
    """
    input_str = input_str.split(" ")
    new_str = list()

    for a_word in input_str:
        new_str.insert(0, a_word)

    return " ".join(new_str)


if __name__ == "__main__":
    print(reverse_words("INPUT STRING"))
