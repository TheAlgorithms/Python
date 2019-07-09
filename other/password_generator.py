"""Password generator allows you to generate a random password of length N."""
from __future__ import print_function
from random import choice
from string import ascii_letters, digits, punctuation


def password_generator(length=8):
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
    chars = tuple(ascii_letters) + tuple(digits) + tuple(punctuation)
    return ''.join(choice(chars) for x in range(length))


# ALTERNATIVE METHODS
# ctbi= characters that must be in password
# i= how many letters or characters the password length will be
def alternative_password_generator(ctbi, i):
    # Password generator = full boot with random_number, random_letters, and
    # random_character FUNCTIONS
    pass  # Put your code here...


def random_number(ctbi, i):
    pass  # Put your code here...


def random_letters(ctbi, i):
    pass  # Put your code here...


def random_characters(ctbi, i):
    pass  # Put your code here...


def main():
    length = int(
        input('Please indicate the max length of your password: ').strip())
    print('Password generated:', password_generator(length))
    print('[If you are thinking of using this passsword, You better save it.]')


if __name__ == '__main__':
    main()
