"""
hangman.py
A simple command-line Hangman game implemented in Python.

This program randomly selects a word from a given list and allows the user
to guess it letter by letter. The game ends when the user either correctly
guesses all the letters or exceeds the maximum allowed wrong attempts.

Usage:
    python hangman.py

Example:
    $ python hangman.py
    Welcome to Hangman!
    _ _ _ _ _
    Enter a letter: a
    Correct!
    a _ _ _ _
    ...
"""

import random


# ----------------------------- #
# HANGMAN STAGES (ASCII ART)
# ----------------------------- #

words = (
    # Fruits
    "apple",
    "orange",
    "banana",
    "coconut",
    "pineapple",
    "mango",
    "papaya",
    "strawberry",
    "blueberry",
    "raspberry",
    "grape",
    "watermelon",
    "peach",
    "pear",
    "cherry",
    "plum",
    "kiwi",
    "apricot",
    "lemon",
    "lime",
    # Animals
    "elephant",
    "tiger",
    "lion",
    "giraffe",
    "zebra",
    "monkey",
    "kangaroo",
    "dolphin",
    "rabbit",
    "panda",
    "koala",
    "wolf",
    "bear",
    "fox",
    "camel",
    "penguin",
    "snake",
    "turtle",
    "deer",
    "leopard",
    # Countries
    "pakistan",
    "india",
    "china",
    "japan",
    "brazil",
    "canada",
    "france",
    "germany",
    "australia",
    "italy",
    "spain",
    "egypt",
    "turkey",
    "russia",
    "mexico",
    "norway",
    "sweden",
    "argentina",
    "indonesia",
    "nigeria",
    # Colors
    "red",
    "blue",
    "green",
    "yellow",
    "purple",
    "orange",
    "black",
    "white",
    "pink",
    "brown",
    "gray",
    "violet",
    "indigo",
    "silver",
    "gold",
    # Computer / Tech
    "python",
    "javascript",
    "variable",
    "function",
    "developer",
    "keyboard",
    "internet",
    "website",
    "database",
    "algorithm",
    "software",
    "hardware",
    "network",
    "browser",
    "program",
    "compiler",
    "laptop",
    "machine",
    "coding",
    # Random everyday words
    "school",
    "teacher",
    "window",
    "garden",
    "flower",
    "butterfly",
    "dream",
    "sunshine",
    "moonlight",
    "family",
    "holiday",
    "mountain",
    "river",
    "forest",
    "island",
    "cloud",
    "ocean",
    "rainbow",
    "friend",
    "love",
)


hangman_art: dict[int, tuple[str, str, str]] = {
    0: ("    ", "    ", "    "),
    1: (" o  ", "    ", "    "),
    2: (" o  ", " |  ", "    "),
    3: (" o  ", "/|  ", "    "),
    4: (" o  ", "/|\\ ", "    "),
    5: (" o  ", "/|\\ ", "/   "),
    6: (" o  ", "/|\\ ", "/ \\ "),
}


def display_man(wrong_guesses: int) -> None:
    """
    Display the current hangman stage according to the number of wrong guesses.

    Args:
        wrong_guesses (int): Number of incorrect guesses made so far.
    """
    print("*****************")
    for line in hangman_art[wrong_guesses]:
        print(line)
    print("*****************")


def display_hint(hint: list[str]) -> None:
    """
    Display the current state of the guessed word as underscores and letters.

    Args:
        hint (list[str]): List containing correctly guessed letters or underscores.
    """
    print(" ".join(hint))


def display_answer(answer: str) -> None:
    """
    Display the correct word at the end of the game.

    Args:
        answer (str): The correct word that was to be guessed.
    """
    print(f"The correct word was: {answer}")


def main() -> None:
    """
    Main function to run the Hangman game.

    The player has up to 6 incorrect guesses to complete the word.
    The game ends when the player wins or loses.
    """
    answer: str = random.choice(words)
    hint: list[str] = ["_"] * len(answer)
    wrong_guesses: int = 0
    guessed_letters: set[str] = set()
    is_running: bool = True

    print("\n Welcome to Hangman!")
    print("Guess the word, one letter at a time.\n")

    while is_running:
        display_man(wrong_guesses)
        display_hint(hint)
        guess = input("Enter a letter: ").lower().strip()

        # Input validation
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single alphabetic character.\n")
            continue

        if guess in guessed_letters:
            print(f"'{guess}' has already been guessed.\n")
            continue

        guessed_letters.add(guess)

        # Check if the guessed letter is in the word
        if guess in answer:
            for i, letter in enumerate(answer):
                if letter == guess:
                    hint[i] = guess
            print("Correct!\n")
        else:
            wrong_guesses += 1
            print("Wrong guess!\n")

        # Win condition
        if "_" not in hint:
            display_man(wrong_guesses)
            display_answer(answer)
            print("YOU WIN!\n")
            is_running = False

        # Lose condition
        elif wrong_guesses >= len(hangman_art) - 1:
            display_man(wrong_guesses)
            display_answer(answer)
            print("YOU LOSE!\n")
            is_running = False


if __name__ == "__main__":
    main()
