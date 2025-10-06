"""
Caesar Cipher Algorithm
Description: Shift each letter in a string by a fixed number.
Time Complexity: O(n)
"""

def caesar_cipher(text, shift):
    result = ""
    for char in text:
        if char.isalpha():  # Encrypt letters only
            shift_base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            result += char  # Non-alphabetic characters remain unchanged
    return result

# Example usage
if __name__ == "__main__":
    message = "abc"
    shift_amount = 2
    encrypted = caesar_cipher(message, shift_amount)
    print(f"Original: {message}")
    print(f"Encrypted with shift {shift_amount}: {encrypted}")
