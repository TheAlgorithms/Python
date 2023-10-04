# make sure you have pycryptodomen to intsall run "pip install pycryptodome"
import hashlib
import hmac
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Protocol.KDF import PBKDF2


def pad(data):
    # Calculate the number of bytes to pad
    padding_length = 16 - (len(data) % 16)

    # Pad the data with bytes equal to the padding length
    padded_data = data + bytes([padding_length] * padding_length)

    return padded_data


def unpad(data):
    # Remove the padding bytes
    padding_length = data[-1]
    unpadded_data = data[:-padding_length]

    return unpadded_data


def encrypt(text, password):
    # Generate a random salt
    salt = get_random_bytes(16)

    # Derive a strong encryption key from the password and salt using PBKDF2
    key = PBKDF2(
        password,
        salt,
        dkLen=32,
        count=1000000,
        prf=lambda p, s: hmac.new(p, s, hashlib.sha256).digest(),
    )

    # Generate a random initialization vector (IV)
    iv = get_random_bytes(16)

    # Create an AES cipher object in CBC mode
    cipher = AES.new(key, AES.MODE_CBC, iv)

    # Pad the plaintext to be a multiple of 16 bytes (AES block size)
    plaintext = text.encode("utf-8")
    padded_text = pad(plaintext)

    # Encrypt the padded text
    ciphertext = cipher.encrypt(padded_text)

    # Return the salt, IV, and ciphertext as bytes
    return salt + iv + ciphertext


def decrypt(ciphertext, password):
    # Extract the salt and IV from the ciphertext
    salt = ciphertext[:16]
    iv = ciphertext[16:32]

    # Derive the encryption key from the password and salt using PBKDF2
    key = PBKDF2(
        password,
        salt,
        dkLen=32,
        count=1000000,
        prf=lambda p, s: hmac.new(p, s, hashlib.sha256).digest(),
    )

    # Create an AES cipher object in CBC mode
    cipher = AES.new(key, AES.MODE_CBC, iv)

    # Decrypt the ciphertext
    decrypted_text = cipher.decrypt(ciphertext[32:])

    # Remove padding and decode to obtain the original plaintext
    plaintext = unpad(decrypted_text).decode("utf-8")

    return plaintext


# Example usage
if __name__ == "__main__":
    password = "YourSecretPassword"
    plaintext = "This is a sample plaintext."

    encrypted_data = encrypt(plaintext, password)
    decrypted_data = decrypt(encrypted_data, password)

    print("Original Text:", plaintext)
    print("Encrypted Text:", encrypted_data)
    print("Decrypted Text:", decrypted_data)
