"""Password Generator allows you to generate a random password of length N."""
import secrets
from random import shuffle
from string import ascii_letters, digits, punctuation


def password_generator(length: int = 8) -> str:
    """
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
    # Password Generator = full boot with random_number, random_letters, and
    # random_character FUNCTIONS
    # Put your code here...
    i -= len(chars_incl)
    quotient = i // 3
    remainder = i % 3
    # chars = chars_incl + random_letters(ascii_letters, i / 3 + remainder) +
    #     random_number(digits, i / 3) + random_characters(punctuation, i / 3)
    chars = (
        chars_incl
        + random(ascii_letters, quotient + remainder)
        + random(digits, quotient)
        + random(punctuation, quotient)
    )
    list_of_chars = list(chars)
    shuffle(list_of_chars)
    return "".join(list_of_chars)

    # random is a generalised function for letters, characters and numbers


def random(chars_incl: str, i: int) -> str:
    return "".join(secrets.choice(chars_incl) for _ in range(i))


def random_number(chars_incl, i):
    pass  # Put your code here...


def random_letters(chars_incl, i):
    pass  # Put your code here...


def random_characters(chars_incl, i):
    pass  # Put your code here...


def main():
    length = int(input("Please indicate the max length of your password: ").strip())
    chars_incl = input(
        "Please indicate the characters that must be in your password: "
    ).strip()
    print("Password generated:", password_generator(length))
    print(
        "Alternative Password generated:",
        alternative_password_generator(chars_incl, length),
    )
    print("[If you are thinking of using this passsword, You better save it.]")


if __name__ == "__main__":
    main()
