# Created by sarathkaul on 12/11/19


def check_pangram(
    input_str: str = "The quick brown fox jumps over the lazy dog",
) -> bool:
    """
    A Pangram String contains all the alphabets at least once.
    >>> check_pangram("The quick brown fox jumps over the lazy dog")
    True
    >>> check_pangram("My name is Unknown")
    False
    >>> check_pangram("The quick brown fox jumps over the la_y dog")
    False
    """
    frequency = set()
    input_str = input_str.replace(
        " ", ""
    )  # Replacing all the Whitespaces in our sentence
    for alpha in input_str:
        if "a" <= alpha.lower() <= "z":
            frequency.add(alpha.lower())

    return True if len(frequency) == 26 else False


if __name__ == "main":
    check_str = "INPUT STRING"
    status = check_pangram(check_str)
    print(f"{check_str} is {'not ' if status else ''}a pangram string")
