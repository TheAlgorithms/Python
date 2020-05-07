from itertools import chain


def encrypt(input_string: str, key: int, alphabet=None) -> str:
    # Set default alphabet to lower and upper case english chars
    alpha = alphabet or [chr(i) for i in chain(range(65, 91), range(97, 123))]

    # The final result string
    result = ""

    for character in input_string:
        if character not in alpha:
            # Append without encryption if character is not in the alphabet
            result += character
        else:
            # Get the index of the new key and make sure it isn't too large
            new_key = (alpha.index(character) + key) % len(alpha)

            # Append the encoded character to the alphabet
            result += alpha[new_key]

    return result


def decrypt(input_string: str, key: int, alphabet=None) -> str:
    # Turn on decode mode by making the key negative
    key *= -1

    return encrypt(input_string, key, alphabet)


def brute_force(input_string: str, alphabet=None) -> dict:
    # Set default alphabet to lower and upper case english chars
    alpha = alphabet or [chr(i) for i in chain(range(65, 91), range(97, 123))]

    # The key during testing (will increase)
    key = 1

    # The encoded result
    result = ""

    # To store data on all the combinations
    brute_force_data = {}

    # Cycle through each combination
    while key <= len(alpha):
        # Encrypt the message
        result = encrypt(input_string, key, alpha)

        # Update the data
        brute_force_data[key] = result

        # Reset result and increase the key
        result = ""
        key += 1

    return brute_force_data


def main():
    while True:
        print(f'\n{"-" * 10}\n Menu\n{"-" * 10}')
        print(*["1.Encrpyt", "2.Decrypt", "3.BruteForce", "4.Quit"], sep="\n")

        # get user input
        choice = input("\nWhat would you like to do?: ").strip()

        # run functions based on what the user chose
        if choice not in ["1", "2", "3", "4"]:
            print("Invalid choice, please enter a valid choice")
        elif choice == "1":
            input_string = input("Please enter the string to be encrypted: ")
            key = int(input("Please enter off-set between 0-25: ").strip())

            print(encrypt(input_string, key))
        elif choice == "2":
            input_string = input("Please enter the string to be decrypted: ")
            key = int(input("Please enter off-set between 1-94: ").strip())

            print(decrypt(input_string, key))
        elif choice == "3":
            input_string = input("Please enter the string to be decrypted: ")
            brute_force_data = brute_force(input_string)

            for key, value in brute_force_data.items():
                print(f"Key: {key} | Message: {value}")

        elif choice == "4":
            print("Goodbye.")
            break


if __name__ == "__main__":
    main()
