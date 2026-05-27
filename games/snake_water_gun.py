"""
Snake Water Gun Game
=====================

A simple command-line game similar to Rock-Paper-Scissors.
Choices: Snake, Water, Gun.

Rules:
    - Snake drinks Water  → Snake wins.
    - Water damages Gun   → Water wins.
    - Gun kills Snake     → Gun wins.
    - Same choice         → Tie.

Functions:
    play(player_choice: str) -> str
        Play a single round against the computer.
    main() -> None
        Run an interactive game loop until the user quits.
"""

import random
import sys
from typing import NoReturn


VALID_CHOICES = ("Snake", "Water", "Gun")

WIN_CONDITIONS = {
    "Snake": "Water",  # Snake drinks Water
    "Water": "Gun",  # Water damages Gun
    "Gun": "Snake",  # Gun kills Snake
}


def play(player_choice: str) -> str:
    """
    Play one round of Snake Water Gun against the computer.

    The function normalises the player's input (case-insensitive) and
    validates it.  The computer picks a random choice.  It then
    determines the winner according to the rules and returns a
    descriptive string.

    Args:
        player_choice: The player's selection.  Any casing is accepted
            ("snake", "SNAKE", "Snake", etc.).

    Returns:
        A string in one of the following formats:
            - "You chose Snake, Computer chose Water. You win!"
            - "You chose Water, Computer chose Gun. You lose!"
            - "You chose Gun, Computer chose Gun. It's a tie!"
            - "Invalid choice: <input>. Please choose Snake, Water, or Gun."

    Examples:
        >>> play("Snake")
        'You chose Snake, Computer chose Water. You win!'   # if computer picks Water
    """
    # Normalise input: strip whitespace, capitalise first letter only
    normalised = player_choice.strip().lower().capitalize()

    if normalised not in VALID_CHOICES:
        return (
            f"Invalid choice: {player_choice}. "
            f"Please choose {', '.join(VALID_CHOICES)}."
        )

    computer_choice = random.choice(VALID_CHOICES)

    if normalised == computer_choice:
        result = "It's a tie!"
    elif WIN_CONDITIONS[normalised] == computer_choice:
        result = "You win!"
    else:
        result = "You lose!"

    return f"You chose {normalised}, Computer chose {computer_choice}. {result}"


def main() -> None:
    """
    Run the interactive Snake Water Gun game loop.

    The user is repeatedly prompted for a choice until they type
    ``quit`` (case-insensitive).  Each round's result is printed
    immediately.
    """
    print("Welcome to Snake Water Gun!")
    print(f"Choices: {', '.join(VALID_CHOICES)}")
    print("Enter 'quit' to exit.\n")

    while True:
        user_input = input("Your choice: ").strip()
        if user_input.lower() == "quit":
            print("Thanks for playing. Goodbye!")
            break
        result = play(user_input)
        print(result)
        print()


if __name__ == "__main__":
    main()
