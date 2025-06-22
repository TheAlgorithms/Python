from __future__ import annotations

import random
import string


class ShuffledShiftCipher:
         """
     This algorithm uses the Caesar Cipher algorithm but removes the option to
     use brute force to decrypt the message.

     The passcode is a random password from the selection buffer of
     1. uppercase letters of the English alphabet
     2. lowercase letters of the English alphabet
     3. digits from 0 to 9

     Using unique characters from the passcode, the normal list of characters,
     that can be allowed in the plaintext, is pivoted and shuffled. Refer to docstring
     of __make_key_list() to learn more about the shuffling.

     Then, using the passcode, a number is calculated which is used to encrypt the
     plaintext message with the normal shift cipher method, only in this case, the
     reference, to look back at while decrypting, is shuffled.

     Each cipher object can possess an optional argument as passcode, without which a
     new passcode is generated for that object automatically.
     cip1 = ShuffledShiftCipher('d4usr9TWxw9wMD')
     cip2 = ShuffledShiftCipher()

    Enhanced Caesar Cipher with shuffled character set for stronger encryption.
    Uses a passcode to generate a unique shuffled key list and shift key.
    """

    def __init__(self, passcode: str | None = None) -> None:
        """
        Initialize cipher with optional passcode.
        Generates random passcode if none provided.
        """
        self.__passcode = passcode or self.__passcode_creator()
        self.__key_list = self.__make_key_list()
        self.__shift_key = self.__make_shift_key()

    def __str__(self) -> str:
        """Return passcode as string representation."""
        return "".join(self.__passcode)

    def __neg_pos(self, iter_list: list[int]) -> list[int]:
        """Alternate sign of elements in list."""
        for i in range(1, len(iter_list), 2):
            iter_list[i] *= -1
        return iter_list

    def __passcode_creator(self) -> list[str]:
        """Generate random passcode."""
        choices = string.ascii_letters + string.digits
        pass_len = random.randint(10, 20)
        return [random.choice(choices) for _ in range(pass_len)]

    def __make_key_list(self) -> list[str]:
        """Create shuffled character set using passcode breakpoints."""
        # Get printable characters except rare whitespace
        key_options = string.printable.strip("\r\x0b\x0c")
        breakpoints = sorted(set(self.__passcode))
        shuffled: list[str] = []  # Explicit type annotation
        temp: list[str] = []  # Explicit type annotation

        for char in key_options:
            temp.append(char)
            if char in breakpoints or char == key_options[-1]:
                shuffled.extend(reversed(temp))
                temp.clear()

        return shuffled

    def __make_shift_key(self) -> int:
        """Calculate shift key from passcode ASCII values."""
        ascii_vals = [ord(x) for x in self.__passcode]
        num = sum(self.__neg_pos(ascii_vals))
        return num if num > 0 else len(self.__passcode)

    def encrypt(self, plaintext: str) -> str:
        """Encrypt plaintext using shuffled shift cipher."""
        encoded: list[str] = []  # Explicit type annotation
        key_len = len(self.__key_list)

        for char in plaintext:
            pos = self.__key_list.index(char)
            new_pos = (pos + self.__shift_key) % key_len
            encoded.append(self.__key_list[new_pos])

        return "".join(encoded)

    def decrypt(self, encoded_message: str) -> str:
        """Decrypt message using shuffled shift cipher."""
        decoded: list[str] = []  # Explicit type annotation
        key_len = len(self.__key_list)

        for char in encoded_message:
            pos = self.__key_list.index(char)
            new_pos = (pos - self.__shift_key) % key_len
            decoded.append(self.__key_list[new_pos])

        return "".join(decoded)


def test_end_to_end() -> str:
    """Test full encryption-decryption cycle."""
    msg = "Hello, this is a modified Caesar cipher"
    cipher = ShuffledShiftCipher()
    return cipher.decrypt(cipher.encrypt(msg))


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    # Example usage
    cipher = ShuffledShiftCipher("SecurePass123")
    original = "Encryption test!"
    encrypted = cipher.encrypt(original)
    decrypted = cipher.decrypt(encrypted)

    print(f"Original: {original}")
    print(f"Encrypted: {encrypted}")
    print(f"Decrypted: {decrypted}")
    print(f"Test passed: {decrypted == original}")
