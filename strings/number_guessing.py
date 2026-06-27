"""Number Guessing Game.

A simple game where the user guesses a randomly generated number
within a user-defined range.

Reference: https://en.wikipedia.org/wiki/Guessing_game
"""

import random


def get_top_of_range() -> int:
    """
    Get the upper bound of the guessing range from the user.

    >>> isinstance(get_top_of_range(), int)
    True
    """
    top_of_range = input("Enter the upper bound number: ")
    if top_of_range.isdigit():
        top_of_range = int(top_of_range)
        if top_of_range <= 0:
            print("Please enter a number larger than 0.")
            quit()
    else:
        print("Please enter a valid digit.")
        quit()
    return top_of_range


def get_guess() -> int:
    """
    Get a valid integer guess from the user.

    >>> isinstance(get_guess(), int)
    True
    """
    while True:
        guess = input("Please make a guess: ")
        if guess.isdigit():
            return int(guess)
        print("Please type a number next time.")


def play_game(top_of_range: int) -> int:
    """
    Play the number guessing game and return the number of guesses.

    >>> import random
    >>> random.seed(42)
    >>> play_game(1)
    Whoa! You got it.
    1
    """
    random_number = random.randint(0, top_of_range)
    guesses = 0

    while True:
        guesses += 1
        guess = get_guess()

        if guess == random_number:
            print("Whoa! You got it.")
            break
        elif guess < random_number:
            print("Too low! Try higher.")
        else:
            print("Too high! Try lower.")

    return guesses


if __name__ == "__main__":
    top = get_top_of_range()
    total_guesses = play_game(top)
    print(f"You got it in {total_guesses} guesses!")