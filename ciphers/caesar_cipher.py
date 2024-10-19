from __future__ import annotations
from string import ascii_letters
from typing import Optional, Dict


def encrypt(input_string: str, key: int, alphabet: Optional[str] = None) -> str:
    """
    Encodes a given string using the Caesar cipher and returns the encoded message.

    Parameters:
    -----------
    input_string : str
        The plain text that needs to be encoded.
    key : int
        The number of letters to shift the message by.
    alphabet : Optional[str]
        The alphabet used to encode the cipher. If not specified, the standard English
        alphabet with upper and lowercase letters is used.

    Returns:
    --------
    str
        A string containing the encoded cipher text.
    """
    alpha = alphabet or ascii_letters
    result = []

    for character in input_string:
        if character in alpha:
            index = alpha.index(character)
            new_index = (index + key) % len(alpha)
            result.append(alpha[new_index])
        else:
            result.append(character)

    return ''.join(result)


def decrypt(input_string: str, key: int, alphabet: Optional[str] = None) -> str:
    """
    Decodes a given cipher text using the Caesar cipher and returns the decoded plain text.

    Parameters:
    -----------
    input_string : str
        The cipher text that needs to be decoded.
    key : int
        The number of letters to shift the message backwards to decode.
    alphabet : Optional[str]
        The alphabet used to decode the cipher. If not specified, the standard English
        alphabet with upper and lowercase letters is used.

    Returns:
    --------
    str
        A string containing the decoded plain text.
    """
    return encrypt(input_string, -key, alphabet)


def brute_force(input_string: str, alphabet: Optional[str] = None) -> Dict[int, str]:
    """
    Returns all possible combinations of keys and the decoded strings as a dictionary.

    Parameters:
    -----------
    input_string : str
        The cipher text that needs to be used during brute-force.
    alphabet : Optional[str]
        The alphabet used to decode the cipher. If not specified, the standard English
        alphabet with upper and lowercase letters is used.

    Returns:
    --------
    Dict[int, str]
        A dictionary where keys are the shift values and values are the decoded messages.
    """
    alpha = alphabet or ascii_letters
    brute_force_data = {}

    for key in range(1, len(alpha) + 1):
        decoded_message = decrypt(input_string, key, alpha)
        brute_force_data[key] = decoded_message

    return brute_force_data


def get_valid_integer(prompt: str) -> int:
    """
    Prompts the user for a valid integer input.

    Parameters:
    -----------
    prompt : str
        The message displayed to the user.

    Returns:
    --------
    int
        The validated integer input from the user.
    """
    while True:
        user_input = input(prompt).strip()
        try:
            return int(user_input)
        except ValueError:
            print("Invalid input. Please enter a valid integer.")


def main():
    """
    Main function to run the Caesar cipher program with a user-interactive menu.
    """
    menu_options = {
        "1": "Encrypt",
        "2": "Decrypt",
        "3": "Brute Force",
        "4": "Quit"
    }

    while True:
        print(f'\n{"-" * 10}\n Menu\n{"-" * 10}')
        for option, description in menu_options.items():
            print(f"{option}. {description}")

        choice = input("\nWhat would you like to do?: ").strip()

        if choice == "1":
            input_string = input("Please enter the string to be encrypted: ")
            key = get_valid_integer("Please enter the offset: ")
            alphabet = input("Enter the alphabet to use (leave blank for default): ") or None

            encrypted_message = encrypt(input_string, key, alphabet)
            print(f"Encrypted message: {encrypted_message}")

        elif choice == "2":
            input_string = input("Please enter the string to be decrypted: ")
            key = get_valid_integer("Please enter the offset: ")
            alphabet = input("Enter the alphabet to use (leave blank for default): ") or None

            decrypted_message = decrypt(input_string, key, alphabet)
            print(f"Decrypted message: {decrypted_message}")

        elif choice == "3":
            input_string = input("Please enter the string to be brute-forced: ")
            alphabet = input("Enter the alphabet to use (leave blank for default): ") or None

            brute_force_data = brute_force(input_string, alphabet)
            for key, message in brute_force_data.items():
                print(f"Key: {key} | Decoded Message: {message}")

        elif choice == "4":
            print("Goodbye.")
            break

        else:
            print("Invalid choice, please enter a valid option.")


if __name__ == "__main__":
    main()
