# Created by sarathkaul on 14/11/19

from ordered_set import OrderedSet


def remove_duplicates(sentence: str) -> str:
    """
    Reomove duplicates from sentence
    >>> remove_duplicates("Python is great and Java is also great")
    'Python is great and Java also'
    """
    sen_list = sentence.split(" ")
    check = OrderedSet()

    for a_word in sen_list:
        check.add(a_word)

    return " ".join(check)


if __name__ == "__main__":
    print(remove_duplicates("INPUT_SENTENCE"))
