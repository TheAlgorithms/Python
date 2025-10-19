"""
A simple, interactive Rock, Paper, Scissors game.
The user plays against the computer, which makes a random choice.
"""

import random


def play_rock_paper_scissors() -> None:
    """
    Starts an interactive session of Rock, Paper, Scissors.
    This function is interactive and does not have a testable return value.
    """
    options = ["rock", "paper", "scissors"]

    while True:
        user_choice = input(
            "Choose rock, paper, or scissors (or 'quit' to exit): "
        ).lower()

        if user_choice == "quit":
            print("Thanks for playing!")
            break

        if user_choice not in options:
            print("Invalid choice. Please try again.")
            continue

        computer_choice = random.choice(options)
        print(f"Computer chose: {computer_choice}")

        if user_choice == computer_choice:
            print("It's a tie!")
        elif (
            (user_choice == "rock" and computer_choice == "scissors")
            or (user_choice == "scissors" and computer_choice == "paper")
            or (user_choice == "paper" and computer_choice == "rock")
        ):
            print("You win!")
        else:
            print("You lose!")
        print("-" * 20)


if __name__ == "__main__":
    play_rock_paper_scissors()
