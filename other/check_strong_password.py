# This Will Check Whether A Given Password Is Strong Or Not
# It Follows The Rule that Length Of Password Should Be At Least 8 Characters
# And At Least 1 Lower, 1 Upper, 1 Number And 1 Special Character

from string import ascii_lowercase, ascii_uppercase, digits, punctuation


def strong_password_detector(password: str, min_length: int = 8) -> str:
    """
    >>> strong_password_detector('Hwea7$2!')
    'This is a strong Password'

    >>> strong_password_detector('Sh0r1')
    'Your Password must be at least 8 characters long'

    >>> strong_password_detector('Hello123')
    'Password should contain UPPERCASE, lowercase, numbers, special characters'

    >>> strong_password_detector('Hello1238udfhiaf038fajdvjjf!jaiuFhkqi1')
    'This is a strong Password'

    >>> strong_password_detector(0)
    'Your Password must be at least 8 characters long'
    """

    if len(str(password)) < 8:
        return "Your Password must be at least 8 characters long"

    upper = any(char in ascii_uppercase for char in password)
    lower = any(char in ascii_lowercase for char in password)
    num = any(char in digits for char in password)
    spec_char = any(char in punctuation for char in password)

    if upper and lower and num and spec_char:
        return "This is a strong Password"

    else:
        return (
            "Password should contain UPPERCASE, lowercase, "
            "numbers, special characters"
        )


if __name__ == "__main__":
    import doctest

    doctest.testmod()
