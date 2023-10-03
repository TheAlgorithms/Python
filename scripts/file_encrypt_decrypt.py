#!/usr/bin/env python3

import os
from cryptography.fernet import Fernet

def generate_key():
    key = Fernet.generate_key()
    with open("encryption_key.key", "wb") as key_file:
        key_file.write(key)

def encrypt_directory(input_directory, key):
    cipher_suite = Fernet(key)

    for filename in os.listdir(input_directory):
        input_file_path = os.path.join(input_directory, filename)

        if os.path.isfile(input_file_path):
            with open(input_file_path, "rb") as file:
                file_data = file.read()

            encrypted_data = cipher_suite.encrypt(file_data)

            with open(input_file_path, "wb") as file:
                file.write(encrypted_data)

            print(f"Encrypted '{input_file_path}'")

def decrypt_directory(input_directory, key):
    cipher_suite = Fernet(key)

    for filename in os.listdir(input_directory):
        input_file_path = os.path.join(input_directory, filename)

        if os.path.isfile(input_file_path):
            with open(input_file_path, "rb") as file:
                encrypted_data = file.read()

            try:
                decrypted_data = cipher_suite.decrypt(encrypted_data)

                with open(input_file_path, "wb") as file:
                    file.write(decrypted_data)

                print(f"Decrypted '{input_file_path}'")
            except cryptography.fernet.InvalidToken:
                print(f"Failed to decrypt '{input_file_path}'")

if __name__ == "__main__":
    action = input("Enter 'e' for encrypt' or 'd' decrypt: ")
    input_directory = input(f"Enter path: ")

    if action == "e":
        generate_key()
        with open("encryption_key.key", "rb") as key_file:
            key = key_file.read()
        encrypt_directory(input_directory, key)
        print("Encryption complete.")
    elif action == "d":
        with open("encryption_key.key", "rb") as key_file:
            key = key_file.read()
        decrypt_directory(input_directory, key)
        print("Decryption complete.")
    else:
        print("Invalid action. Use 'e' or 'd'.")
