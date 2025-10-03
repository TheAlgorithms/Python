"""
Snake-Water-Gun Game

A simple game where the user plays against the computer.
Choices: 's' for Snake, 'w' for Water, 'g' for Gun.

Reference: https://en.wikipedia.org/wiki/Rock_paper_scissors
"""

import random
from typing import Literal


<<<<<<< HEAD
def snake_water_gun(
    user_choice: Literal["s", "w", "g"], computer_choice: Literal["s", "w", "g"]
) -> str:
=======
def get_computer_choice() -> Literal["s", "w", "g"]:
>>>>>>> b5d62810 (Refactored snake_game.py with doctests and type hints for automated testing)
    """
    Randomly returns the computer's choice.

    Returns
    -------
    str
        's' for snake, 'w' for water, or 'g' for gun
    """
    return random.choice(["s", "w", "g"])


def get_user_choice() -> Literal["s", "w", "g"]:
    """
    Prompts the user to enter their choice and validates it.

    Returns
    -------
    str
        's' for snake, 'w' for water, or 'g' for gun
    """
    while True:
        choice = input("Enter your choice: s for snake, w for water, g for gun: ").strip().lower()
        if choice in ("s", "w", "g"):
            return choice
        print("Invalid input! Please enter 's', 'w', or 'g'.")


def determine_winner(user_choice: str, computer_choice: str) -> str:
    """
    Determines the winner of the Snake-Water-Gun game.

    Parameters
    ----------
    user_choice : str
        The user's choice
    computer_choice : str
        The computer's choice

    Returns
    -------
    str
        "draw", "user", or "computer" indicating the winner

    Examples
    --------
    >>> determine_winner("s", "w")
    'user'
    >>> determine_winner("w", "s")
    'computer'
    >>> determine_winner("g", "g")
    'draw'
    """
    if user_choice == computer_choice:
<<<<<<< HEAD
        return "Draw"
    if (user_choice, computer_choice) in [("s", "w"), ("w", "g"), ("g", "s")]:
        return "You win!"
    return "Computer wins!"


def main() -> None:
=======
        return "draw"

    wins = {
        "s": "w",  # snake drinks water
        "w": "g",  # water damages gun
        "g": "s",  # gun kills snake
    }

    if wins[user_choice] == computer_choice:
        return "user"
    return "computer"


def play_game() -> None:
>>>>>>> b5d62810 (Refactored snake_game.py with doctests and type hints for automated testing)
    """
    Runs the Snake-Water-Gun game.
    """
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()

<<<<<<< HEAD
    while True:
        try:
            rounds = int(
                input("Enter the number of rounds you want to play (1-10): ").strip()
            )
            if 1 <= rounds <= 10:
                break
            else:
                print("Please enter a number between 1 and 10.")
        except ValueError:
            print("Invalid input. Please enter an integer.")

    score_user = 0
    score_computer = 0
    choices = ["s", "w", "g"]

    for round_number in range(1, rounds + 1):
        print(f"\nRound {round_number}:")
        while True:
            user_input = (
                input("Enter your choice: s for Snake, w for Water, g for Gun: ")
                .strip()
                .lower()
            )
            if user_input in choices:
                break
            else:
                print("Invalid choice. Please enter 's', 'w', or 'g'.")

        computer_input = random.choice(choices)
        print(f"You chose {user_input}, computer chose {computer_input}.")

        result = snake_water_gun(user_input, computer_input)
        print(result)

        if result == "You win!":
            score_user += 1
        elif result == "Computer wins!":
            score_computer += 1

    print("\nGame Over!")
    print(f"Your score: {score_user}")
    print(f"Computer score: {score_computer}")

    if score_user > score_computer:
        print("Congratulations! You won the game!")
    elif score_user < score_computer:
        print("Computer won the game! Better luck next time!")
=======
    print(f"You chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")

    winner = determine_winner(user_choice, computer_choice)
    if winner == "draw":
        print("It's a draw!")
    elif winner == "user":
        print("You win!")
>>>>>>> b5d62810 (Refactored snake_game.py with doctests and type hints for automated testing)
    else:
        print("Computer wins!")



if __name__ == "__main__":
    play_game()
