import secrets
from random import shuffle
from string import ascii_letters, ascii_lowercase, ascii_uppercase, digits, punctuation


def password_generator(length: int = 8) -> str:
    """
    Password Generator allows you to generate a random password of length N.

    >>> len(password_generator())
    8
    >>> len(password_generator(length=16))
    16
    >>> len(password_generator(257))
    257
    >>> len(password_generator(length=0))
    0
    >>> len(password_generator(-1))
    0
    """
    chars = ascii_letters + digits + punctuation
    return "".join(secrets.choice(chars) for _ in range(length))


# ALTERNATIVE METHODS
# chars_incl= characters that must be in password
# i= how many letters or characters the password length will be
def alternative_password_generator(chars_incl: str, i: int) -> str:
    """
    Generate a password of length i that includes all characters in chars_incl.

    >>> len(alternative_password_generator("aA1!", 10))
    10
    >>> all(c in alternative_password_generator("test", 12) for c in "test")
    True
    >>> len(alternative_password_generator("abcd", 4))
    4
    >>> alternative_password_generator("abcdefgh", 5)
    Traceback (most recent call last):
        ...
    ValueError: Requested length (5) cannot be less than required characters (8)
    """
    if i < len(chars_incl):
        msg = (
            f"Requested length ({i}) cannot be less than "
            f"required characters ({len(chars_incl)})"
        )
        raise ValueError(msg)

    i -= len(chars_incl)
    quotient = i // 3
    remainder = i % 3
    chars = (
        chars_incl
        + random(ascii_letters, quotient + remainder)
        + random(digits, quotient)
        + random(punctuation, quotient)
    )
    list_of_chars = list(chars)
    shuffle(list_of_chars)
    return "".join(list_of_chars)


def random(chars_incl: str, i: int) -> str:
    """
    Generate a random string of length i from characters in chars_incl.

    >>> len(random("abc", 5))
    5
    >>> all(c in "abc" for c in random("abc", 10))
    True
    >>> random("xyz", 0)
    ''
    """
    return "".join(secrets.choice(chars_incl) for _ in range(i))


def is_strong_password(password: str, min_length: int = 8) -> bool:
    """
    This will check whether a given password is strong or not. The password must be at
    least as long as the provided minimum length, and it must contain at least 1
    lowercase letter, 1 uppercase letter, 1 number and 1 special character.

    >>> is_strong_password('Hwea7$2!')
    True
    >>> is_strong_password('Sh0r1')
    False
    >>> is_strong_password('Hello123')
    False
    >>> is_strong_password('Hello1238udfhiaf038fajdvjjf!jaiuFhkqi1')
    True
    >>> is_strong_password('0')
    False
    """
    if len(password) < min_length:
        return False

    upper = any(char in ascii_uppercase for char in password)
    lower = any(char in ascii_lowercase for char in password)
    num = any(char in digits for char in password)
    spec_char = any(char in punctuation for char in password)

    return upper and lower and num and spec_char


def main() -> None:
    length = int(input("Please indicate the max length of your password: ").strip())
    chars_incl = input(
        "Please indicate the characters that must be in your password: "
    ).strip()
    print("Password generated:", password_generator(length))
    print(
        "Alternative Password generated:",
        alternative_password_generator(chars_incl, length),
    )
    print("[If you are thinking of using this password, You better save it.]")


if __name__ == "__main__":
    main()
