"""
A simple implementation of the Snake, Water, Gun game.
"""

import doctest
import random


def snake_water_gun(player_choice: str, computer_choice: str) -> str:
    """
    Determines the winner of a Snake, Water, Gun game round.

    Args:
        player_choice: The player's choice ('s' for snake, 'w' for water, 'g' for gun).
        computer_choice: The computer's choice.

    Returns:
        Result: "Player wins!", "Computer wins!", or "It's a draw!".

    Doctests:
        >>> snake_water_gun('s', 'w')
        'Player wins!'
        >>> snake_water_gun('w', 'g')
        'Player wins!'
        >>> snake_water_gun('g', 's')
        'Player wins!'
        >>> snake_water_gun('w', 's')
        'Computer wins!'
        >>> snake_water_gun('s', 's')
        "It's a draw!"
    """
    if player_choice == computer_choice:
        return "It's a draw!"

    if (
        (player_choice == "s" and computer_choice == "w")
        or (player_choice == "w" and computer_choice == "g")
        or (player_choice == "g" and computer_choice == "s")
    ):
        return "Player wins!"
    else:
        return "Computer wins!"


def main():
    """
    Main function to run the Snake, Water, Gun game.
    """
    print("--- Snake, Water, Gun Game ---")
    player_input = (
        input("Enter your choice (s for snake, w for water, g for gun): ")
        .lower()
        .strip()
    )

    if player_input not in ["s", "w", "g"]:
        print("Invalid choice. Please choose 's', 'w', or 'g'.")
        return

    choices = ["s", "w", "g"]
    computer_input = random.choice(choices)

    print(f"\nYou chose: {player_input}")
    print(f"Computer chose: {computer_input}\n")

    result = snake_water_gun(player_input, computer_input)
    print(result)


if __name__ == "__main__":
    doctest.testmod()  # Run the doctests
    main()
