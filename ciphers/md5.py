# Author: farazulhoda

# A Python program that calculates the MD5 (Message Digest 5) hash of a given string using the hashlib library.
# While MD5 is considered weak and not suitable for cryptographic purposes, it can still be used for non-security-related purposes
# like checksums or simple data integrity checks.


# By importing the hashlib library, which provides various hashing algorithms, including MD5.
import hashlib


# Function to calculate the MD5 hash of a given input string.
def calculate_md5_hash(input_string):
    # Create an MD5 hash object using hashlib.
    md5_hash = hashlib.md5()

    # Update the hash object with the input string, encoded as bytes.
    md5_hash.update(input_string.encode("utf-8"))

    # Get the hexadecimal representation of the MD5 hash.
    md5_hash_hex = md5_hash.hexdigest()

    # Return the MD5 hash as a hexadecimal string.
    return md5_hash_hex


# Input string provided by the user.
input_string = input("Enter a string: ")

# Calculate and print the MD5 hash.
md5_hash = calculate_md5_hash(input_string)
print(f"Input String: {input_string}")
print(f"MD5 Hash: {md5_hash}")
