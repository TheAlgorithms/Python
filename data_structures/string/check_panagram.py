# Created by sarathkaul on 12/11/19


def check_panagram(input_str: str) -> None:
    """
    A Panagram String contains all the alphabets at least once.
    >>> check_panagram("The quick brown fox jumps over the lazy dog")
    The quick brown fox jumps over the lazy dog is a Panagram String
    >>> check_panagram("My name is Unknown")
    My name is Unknown is not a Panagram String
    """
    frequency = set()

    for alpha in input_str:
        if alpha != " ":
            frequency.add(alpha.lower())
    if len(frequency) == 26:
        print(f"{input_str} is a Panagram String")
    else:
        print(f"{input_str} is not a Panagram String")

if __name__ == "main":
    check_panagram("INPUT STRING")