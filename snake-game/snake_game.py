"""
Snake-Water-Gun Game

This program allows a user to play the classic Snake-Water-Gun game against the computer.
The user can play multiple rounds, and scores are displayed at the end.

Fixes Issue: #12987
"""

import random
from typing import Literal


def snake_water_gun(
    user_choice: Literal["s", "w", "g"], computer_choice: Literal["s", "w", "g"]
) -> str:
    """
    Determines the winner between user and computer.

    Parameters:
    user_choice (str): 's' for Snake, 'w' for Water, 'g' for Gun
    computer_choice (str): 's' for Snake, 'w' for Water, 'g' for Gun

    Returns:
    str: Result message - 'Draw', 'You win!', or 'Computer wins!'

    >>> snake_water_gun('s', 'w')
    'You win!'
    >>> snake_water_gun('g', 's')
    'You win!'
    >>> snake_water_gun('w', 'w')
    'Draw'
    """
    if user_choice == computer_choice:
        return "Draw"
    if (user_choice, computer_choice) in [("s", "w"), ("w", "g"), ("g", "s")]:
        return "You win!"
    return "Computer wins!"


def main() -> None:
    """
    Main function to run the Snake-Water-Gun game with multiple rounds.
    """
    print("Welcome to Snake-Water-Gun Game!")
    rounds = 0

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
    else:
        print("It's a tie!")


if __name__ == "__main__":
    main()
