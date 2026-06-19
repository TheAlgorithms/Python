"""
A simple number guessing game.
The program generates a random number and the user has to guess it.
"""

import random


def guessing_game(low: int, high: int) -> None:
    """
    Starts an interactive number guessing game.
    This function is interactive and does not have a return value for doctests.
    """
    secret_number = random.randint(low, high)
    attempts = 0
    print(f"I'm thinking of a number between {low} and {high}. Can you guess it?")

    while True:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1
            if guess < secret_number:
                print("Too low! Try again.")
            elif guess > secret_number:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You guessed it in {attempts} attempts.")
                break
        except ValueError:
            print("Invalid input. Please enter an integer.")


if __name__ == "__main__":
    guessing_game(1, 100)
