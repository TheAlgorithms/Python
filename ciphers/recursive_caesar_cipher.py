# Recursive Caesar cipher function
def caesar_cipher(text, key):
    # Base case: the text is empty
    if not text:
        return ""
    # Convert the first character to ASCII code
    code = ord(text[0])
    # Check if the character is an uppercase letter
    if 65 <= code <= 90:
        # Shift the character by the key and wrap around if needed
        code = (code - 65 + key) % 26 + 65
    # Check if the character is a lowercase letter
    elif 97 <= code <= 122:
        # Shift the character by the key and wrap around if needed
        code = (code - 97 + key) % 26 + 97
    # Convert the shifted character back to string
    char = chr(code)
    # Recursively cipher the remaining text and concatenate with the first character
    return char + caesar_cipher(text[1:], key)


# Example text to cipher
text = "The Algorithms!"
# Example key to shift by
key = 6
# Call the recursive Caesar cipher function
ciphered_text = caesar_cipher(text, key)
# Print the ciphered text
print(ciphered_text)
