from __future__ import annotations

from string import ascii_letters


def encrypt(input_string: str, key: int, alphabet: str | None = None) -> str:
    """
    encrypt
    =======
    Encodes a given string with the caesar cipher and returns the encoded
    message

    Parameters:
    -----------
    *   input_string: the plain-text that needs to be encoded
    *   key: the number of letters to shift the message by

    Optional:
    *   alphabet (None): the alphabet used to encode the cipher, if not
        specified, the standard english alphabet with upper and lowercase
        letters is used

    Returns:
    *   A string containing the encoded cipher-text

    More on the caesar cipher
    =========================
    The caesar cipher is named after Julius Caesar who used it when sending
    secret military messages to his troops. This is a simple substitution cipher
    where very character in the plain-text is shifted by a certain number known
    as the "key" or "shift".

    Example:
    Say we have the following message:
    "Hello, captain"

    And our alphabet is made up of lower and uppercase letters:
    "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

    And our shift is "2"

    We can then encode the message, one letter at a time. "H" would become "J",
    since "J" is two letters away, and so on. If the shift is ever two large, or
    our letter is at the end of the alphabet, we just start at the beginning
    ("Z" would shift to "a" then "b" and so on).

    Our final message would be "Jgnnq, ecrvckp"

    Further reading
    ===============
    *   https://en.m.wikipedia.org/wiki/Caesar_cipher

    Doctests
    ========
    >>> encrypt('The quick brown fox jumps over the lazy dog', 8)
    'bpm yCqks jzwEv nwF rCuxA wDmz Bpm tiHG lwo'

    >>> encrypt('A very large key', 8000)
    's nWjq dSjYW cWq'

    >>> encrypt('a lowercase alphabet', 5, 'abcdefghijklmnopqrstuvwxyz')
    'f qtbjwhfxj fqumfgjy'
    """
    # Set default alphabet to lower and upper case english chars
    alpha = alphabet or ascii_letters

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


def decrypt(input_string: str, key: int, alphabet: str | None = None) -> str:
    """
    decrypt
    =======
    Decodes a given string of cipher-text and returns the decoded plain-text

    Parameters:
    -----------
    *   input_string: the cipher-text that needs to be decoded
    *   key: the number of letters to shift the message backwards by to decode

    Optional:
    *   alphabet (None): the alphabet used to decode the cipher, if not
        specified, the standard english alphabet with upper and lowercase
        letters is used

    Returns:
    *   A string containing the decoded plain-text

    More on the caesar cipher
    =========================
    The caesar cipher is named after Julius Caesar who used it when sending
    secret military messages to his troops. This is a simple substitution cipher
    where very character in the plain-text is shifted by a certain number known
    as the "key" or "shift". Please keep in mind, here we will be focused on
    decryption.

    Example:
    Say we have the following cipher-text:
    "Jgnnq, ecrvckp"

    And our alphabet is made up of lower and uppercase letters:
    "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

    And our shift is "2"

    To decode the message, we would do the same thing as encoding, but in
    reverse. The first letter, "J" would become "H" (remember: we are decoding)
    because "H" is two letters in reverse (to the left) of "J". We would
    continue doing this. A letter like "a" would shift back to the end of
    the alphabet, and would become "Z" or "Y" and so on.

    Our final message would be "Hello, captain"

    Further reading
    ===============
    *   https://en.m.wikipedia.org/wiki/Caesar_cipher

    Doctests
    ========
    >>> decrypt('bpm yCqks jzwEv nwF rCuxA wDmz Bpm tiHG lwo', 8)
    'The quick brown fox jumps over the lazy dog'

    >>> decrypt('s nWjq dSjYW cWq', 8000)
    'A very large key'

    >>> decrypt('f qtbjwhfxj fqumfgjy', 5, 'abcdefghijklmnopqrstuvwxyz')
    'a lowercase alphabet'
    """
    # Turn on decode mode by making the key negative
    key *= -1

    return encrypt(input_string, key, alphabet)


def brute_force(input_string: str, alphabet: str | None = None) -> dict[int, str]:
    """
    brute_force
    ===========
    Returns all the possible combinations of keys and the decoded strings in the
    form of a dictionary

    Parameters:
    -----------
    *   input_string: the cipher-text that needs to be used during brute-force

    Optional:
    *   alphabet:  (None): the alphabet used to decode the cipher, if not
        specified, the standard english alphabet with upper and lowercase
        letters is used

    More about brute force
    ======================
    Brute force is when a person intercepts a message or password, not knowing
    the key and tries every single combination. This is easy with the caesar
    cipher since there are only all the letters in the alphabet. The more
    complex the cipher, the larger amount of time it will take to do brute force

    Ex:
    Say we have a 5 letter alphabet (abcde), for simplicity and we intercepted the
    following message:

    "dbc"

    we could then just write out every combination:
    ecd... and so on, until we reach a combination that makes sense:
    "cab"

    Further reading
    ===============
    *   https://en.wikipedia.org/wiki/Brute_force

    Doctests
    ========
    >>> brute_force("jFyuMy xIH'N vLONy zILwy Gy!")[20]
    "Please don't brute force me!"

    >>> brute_force(1)
    Traceback (most recent call last):
    TypeError: 'int' object is not iterable
    """
    # Set default alphabet to lower and upper case english chars
    alpha = alphabet or ascii_letters

    # To store data on all the combinations
    brute_force_data = {}

    # Cycle through each combination
    for key in range(1, len(alpha) + 1):
        # Decrypt the message and store the result in the data
        brute_force_data[key] = decrypt(input_string, key, alpha)

    return brute_force_data


if __name__ == "__main__":
    while True:
        print(f'\n{"-" * 10}\n Menu\n{"-" * 10}')
        print(*["1.Encrypt", "2.Decrypt", "3.BruteForce", "4.Quit"], sep="\n")

        # get user input
        choice = input("\nWhat would you like to do?: ").strip() or "4"

        # run functions based on what the user chose
        if choice not in ("1", "2", "3", "4"):
            print("Invalid choice, please enter a valid choice")
        elif choice == "1":
            input_string = input("Please enter the string to be encrypted: ")
            key = int(input("Please enter off-set: ").strip())

            print(encrypt(input_string, key))
        elif choice == "2":
            input_string = input("Please enter the string to be decrypted: ")
            key = int(input("Please enter off-set: ").strip())

            print(decrypt(input_string, key))
        elif choice == "3":
            input_string = input("Please enter the string to be decrypted: ")
            brute_force_data = brute_force(input_string)

            for key, value in brute_force_data.items():
                print(f"Key: {key} | Message: {value}")

        elif choice == "4":
            print("Goodbye.")
            break
