'''
This algorithm is used to hash a string using the MD5 algorithm.
To run this script, you must have Python 3 installed.
To run this script, type the following command:
python hashing.py
'''
import hashlib

# Define the string to be hashed
string_to_hash = input("Enter the string to be hashed: ")

# Create an instance of the MD5 hashing algorithm
hash_object = hashlib.md5()

# Update the hash object with the string to be hashed
hash_object.update(string_to_hash.encode())

# Get the hexadecimal representation of the hash
hex_dig = hash_object.hexdigest()

# Print the hash
print(hex_dig)
