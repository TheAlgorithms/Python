"""
A classic word-guessing game: Hangman.
The computer picks a secret word, and the player tries to guess it letter by letter.
"""

import random


def play_hangman() -> None:
    """
    Starts an interactive session of Hangman.
    This function is interactive and does not have a testable return value.
    """
    words = ["python", "github", "algorithm", "developer", "computer"]
    secret_word = random.choice(words)
    guessed_letters = set()
    incorrect_guesses = 0
    max_attempts = 6

    print("Welcome to Hangman!")

    while incorrect_guesses < max_attempts:
        # Display the current state of the word
        display_word = "".join(
            letter if letter in guessed_letters else "_" for letter in secret_word
        )
        print(f"\nWord: {display_word}")
        print(f"Incorrect guesses left: {max_attempts - incorrect_guesses}")

        if display_word == secret_word:
            print(f"Congratulations! You guessed the word: {secret_word}")
            return

        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
        elif guess in secret_word:
            print("Good guess!")
            guessed_letters.add(guess)
        else:
            print("Sorry, that letter is not in the word.")
            incorrect_guesses += 1
            guessed_letters.add(guess)

    print(f"\nGame over! The word was: {secret_word}")


if __name__ == "__main__":
    play_hangman()
