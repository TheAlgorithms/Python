"""
Snake Water Gun Game

This is a simple implementation of the Snake Water Gun game (similar to Rock Paper Scissors).
The rules are:
- Snake drinks Water (Snake wins)
- Water rusts Gun (Water wins)
- Gun shoots Snake (Gun wins)

Author: TheAlgorithms/Python
"""

import random


def get_computer_choice() -> str:
    """
    Generate a random choice for the computer.
    
    Returns:
        str: Computer's choice ('s' for snake, 'w' for water, 'g' for gun)
        
    Examples:
        >>> choice = get_computer_choice()
        >>> choice in ['s', 'w', 'g']
        True
    """
    choices = ['s', 'w', 'g']
    return random.choice(choices)


def get_choice_name(choice: str) -> str:
    """
    Convert choice letter to full name.
    
    Args:
        choice (str): Choice letter ('s', 'w', or 'g')
        
    Returns:
        str: Full name of the choice
        
    Examples:
        >>> get_choice_name('s')
        'snake'
        >>> get_choice_name('w')
        'water'
        >>> get_choice_name('g')
        'gun'
        >>> get_choice_name('x')
        'unknown'
    """
    choice_names = {
        's': 'snake',
        'w': 'water',
        'g': 'gun'
    }
    return choice_names.get(choice, 'unknown')


def determine_winner(player_choice: str, computer_choice: str) -> str:
    """
    Determine the winner based on game rules.
    Rules: Snake drinks Water, Water rusts Gun, Gun shoots Snake
    
    Args:
        player_choice (str): Player's choice ('s', 'w', or 'g')
        computer_choice (str): Computer's choice ('s', 'w', or 'g')
        
    Returns:
        str: Result of the game ('win', 'lose', or 'draw')
        
    Examples:
        >>> determine_winner('s', 's')
        'draw'
        >>> determine_winner('s', 'w')  # Snake drinks Water
        'win'
        >>> determine_winner('w', 'g')  # Water rusts Gun
        'win'
        >>> determine_winner('g', 's')  # Gun shoots Snake
        'win'
        >>> determine_winner('w', 's')  # Snake drinks Water
        'lose'
        >>> determine_winner('g', 'w')  # Water rusts Gun
        'lose'
        >>> determine_winner('s', 'g')  # Gun shoots Snake
        'lose'
    """
    if player_choice == computer_choice:
        return 'draw'
    
    # Define winning conditions for player
    winning_conditions = {
        's': 'w',  # Snake drinks Water
        'w': 'g',  # Water rusts Gun
        'g': 's'   # Gun shoots Snake
    }
    
    if winning_conditions[player_choice] == computer_choice:
        return 'win'
    else:
        return 'lose'


def play_single_game() -> None:
    """
    Play a single round of Snake Water Gun game.
    """
    print("\n=== Snake Water Gun Game ===")
    print("Rules:")
    print("- Snake drinks Water (Snake wins)")
    print("- Water rusts Gun (Water wins)")
    print("- Gun shoots Snake (Gun wins)")
    print()
    
    # Get player input
    while True:
        player_choice = input("Enter your choice: s for snake, w for water, g for gun: ").lower().strip()
        if player_choice in ['s', 'w', 'g']:
            break
        print("Invalid choice! Please enter 's', 'w', or 'g'.")
    
    # Get computer choice
    computer_choice = get_computer_choice()
    
    # Display choices
    print(f"You chose {get_choice_name(player_choice)}")
    print(f"Computer chose {get_choice_name(computer_choice)}")
    
    # Determine and display result
    result = determine_winner(player_choice, computer_choice)
    
    if result == 'draw':
        print("It's a draw!")
    elif result == 'win':
        print("You win!")
    else:
        print("You lose!")


def play_multiple_games() -> None:
    """
    Play multiple rounds and keep score.
    """
    player_score = 0
    computer_score = 0
    draws = 0
    
    print("\n=== Snake Water Gun - Multiple Rounds ===")
    
    while True:
        try:
            rounds = int(input("How many rounds would you like to play? "))
            if rounds > 0:
                break
            print("Please enter a positive number.")
        except ValueError:
            print("Please enter a valid number.")
    
    for round_num in range(1, rounds + 1):
        print(f"\n--- Round {round_num} ---")
        
        # Get player input
        while True:
            player_choice = input("Enter your choice: s for snake, w for water, g for gun: ").lower().strip()
            if player_choice in ['s', 'w', 'g']:
                break
            print("Invalid choice! Please enter 's', 'w', or 'g'.")
        
        # Get computer choice
        computer_choice = get_computer_choice()
        
        # Display choices
        print(f"You chose {get_choice_name(player_choice)}")
        print(f"Computer chose {get_choice_name(computer_choice)}")
        
        # Determine result
        result = determine_winner(player_choice, computer_choice)
        
        if result == 'draw':
            print("It's a draw!")
            draws += 1
        elif result == 'win':
            print("You win this round!")
            player_score += 1
        else:
            print("Computer wins this round!")
            computer_score += 1
        
        # Display current score
        print(f"Score - You: {player_score}, Computer: {computer_score}, Draws: {draws}")
    
    # Final results
    print(f"\n=== Final Results ===")
    print(f"Your score: {player_score}")
    print(f"Computer score: {computer_score}")
    print(f"Draws: {draws}")
    
    if player_score > computer_score:
        print("🎉 Congratulations! You won overall!")
    elif computer_score > player_score:
        print("💻 Computer wins overall! Better luck next time!")
    else:
        print("🤝 It's a tie overall! Great game!")


def main() -> None:
    """
    Main function to run the Snake Water Gun game.
    """
    print("Welcome to Snake Water Gun Game!")
    
    while True:
        print("\nChoose game mode:")
        print("1. Single game")
        print("2. Multiple rounds")
        print("3. Exit")
        
        choice = input("Enter your choice (1/2/3): ").strip()
        
        if choice == '1':
            play_single_game()
        elif choice == '2':
            play_multiple_games()
        elif choice == '3':
            print("Thanks for playing! Goodbye!")
            break
        else:
            print("Invalid choice! Please enter 1, 2, or 3.")
        
        # Ask if player wants to continue
        if choice in ['1', '2']:
            play_again = input("\nWould you like to play again? (y/n): ").lower().strip()
            if play_again != 'y':
                print("Thanks for playing! Goodbye!")
                break


if __name__ == "__main__":
    main()
