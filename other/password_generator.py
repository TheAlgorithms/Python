from __future__ import print_function
import string
import random


def password_generator(max_length):
    letters = [letter for letter in string.ascii_letters]
    digits = [digit for digit in string.digits]
    symbols = [symbol for symbol in string.punctuation]
    chars = letters + digits + symbols
    random.shuffle(chars)
    password = ''.join(random.choice(chars)
                       for x in range(max_length))
    return password


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
    max_length = int(
        input('Please indicate the max length of your password: '))
    print ('Password generated:', password_generator(max_length))
    print('[If you are thinking of using this passsword, You better save it.]')


if __name__ == '__main__':
    main()
