import random

computer_choice = random.choice(["rock", "paper", "scissors"])
player_choice = input(
    "What would you like to choose: Rock, Paper or Scissors: ").lower()
w = "You Won!"
l = "Computer Won!"


def determine_winner():
    if computer_choice == player_choice:
        return "It's a tie!"

    if player_choice == "rock" and computer_choice == "scissors":
        return w

    elif player_choice == "rock" and computer_choice == "paper":
        return l

    if player_choice == "paper" and computer_choice == "rock":
        return w

    elif player_choice == "paper" and computer_choice == "scissors":
        return l

    if player_choice == "scissors" and computer_choice == "paper":
        return w

    elif player_choice == "scissors" and computer_choice == "rock":
        return l

    if player_choice != "rock" and player_choice != "scissors" and player_choice != "paper":
        return 'Throw a valid string!'


def play_game():
    print(f"You threw: {player_choice}.")
    print(f"Computer threw: {computer_choice}.")


play_game()
print(determine_winner())
