def reverse(word: str) -> str:
    """
    Will reverse the entire string

    >>> reverse("Hello World")
    'dlroW olleH'
    >>> reverse("wh[]32")
    '23][hw'
    >>> reverse("WHAT are you Doing?")
    '?gnioD uoy era TAHW'
    >>> reverse("gnirts tupni eht sesrever noitcnuf sihT")
    'This function reverses the input string'
    >>> reverse("")
    ''
    """

    # creating a string slice that starts at the end of the string, and moves backwards.
    # the slice statement [::-1] means start at the end of the string and end at position 0,
    # move with the step negative one, which means one step backwards.
    return "".join(word[::-1])


if __name__ == "__main__":
    from doctest import testmod

    testmod()
