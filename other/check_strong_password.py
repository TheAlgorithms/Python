# This Will Check Whether A Given Password Is Strong Or Not
# It Follows The Rule that Length Of Password Should Be At Least 8 Characters
# And At Least 1 Lower, 1 Upper, 1 Number And 1 Special Character


import re


def strong_password_detector(password: str) -> str:
    """
    >>> strong_password_detector('Hwea7$2!')
    'This is a strong Password'

    >>> strong_password_detector('Sh0r1')
    'Your Password must be atleast 8 characters long'

    >>> strong_password_detector('Hello123')
    'Your Password should contain both UPPERCASE and lowercase letters with atleast 1 digit and 1 special character'
    """

    upper = re.compile(r"[A-Z]")
    lower = re.compile(r"[a-z]")
    num = re.compile(r"[0-9]")
    spec_char = re.compile(r"[!@#$\^&\*\(\):;\'\"<>,\.\?\/|]")

    if re.compile(r"\s").search(password) or len(password) < 8:
        return "Your Password must be atleast 8 characters long"

    elif (
        upper.search(password)
        and lower.search(password)
        and num.search(password)
        and spec_char.search(password)
    ):
        return "This is a strong Password"

    else:
        return "Your Password should contain both UPPERCASE and lowercase letters with atleast 1 digit and 1 special character"


if __name__ == "__main__":
    import doctest

    doctest.testmod()
