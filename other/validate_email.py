"""
The code below features a function that can tell
whether a given string argument is a valid email
address or not.
"""
import re


def validate_email(email: str) -> bool:
    """
    validate_email uses regular expressions to check if the input is
    a valid email address.
    -------
    :param email: a string that represents the email to be validated.

    Examples:
    >>> validate_email('joker01@gmail.com')
    True
    >>> validate_email('joker01@gmail-com')
    False
    """

    regex_ = re.compile(
        r"""
        # email prefix
        ([a-zA-Z0-9_\-+%]+|[a-zA-Z0-9\-_%+]+(.\.))
        # @ symbol
        [@]
        # email domain
        [a-zA-Z0-9.-]+
        # email suffix
        [\.]
        ([a-zA-Z]{2,4})
        """,
        re.VERBOSE,
    )
    return bool(regex_.search(email))

if __name__ == "__main__":
    import doctest

    doctest.testmod()
