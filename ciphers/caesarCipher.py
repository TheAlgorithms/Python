# Define the alphabet as a string
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# Define the shift as an integer
shift = 3

# Define the message as a string
message = "CAESAR CIPHER"

# Initialize an empty string for the encrypted message
encrypted = ""

# Loop through each character in the message
for char in message:
    # If the character is a letter, encrypt it
    if char in alphabet:
        # Find the index of the letter in the alphabet
        index = alphabet.index(char)
        # Add the shift to the index and wrap around if necessary
        new_index = (index + shift) % len(alphabet)
        # Find the new letter in the alphabet
        new_char = alphabet[new_index]
        # Append the new letter to the encrypted message
        encrypted += new_char
    # If the character is not a letter, keep it as it is
    else:
        encrypted += char

# Print the encrypted message
print(encrypted)
