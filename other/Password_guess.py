import random
import os

# Define the list of possible characters
pwd = ['a', 'b', 'c', 'd', 'e', 'f', '1', '2', '3', '4', '5', '6', 
       'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 
       's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# Input from the user
u_pwd = input("Enter a password: ")

# Initialize an empty string to store the guessed password
pw = ""

while pw != u_pwd:
    # Reset the guessed password to an empty string
    pw = ""
    
    # Generate a guess by selecting random characters from the pwd list
    for _ in range(len(u_pwd)):
        guess_pwd = random.choice(pwd)
        pw += guess_pwd

    # Print progress information
    print(f"Attempting to crack password: {pw}")

    # Clear the console for the next attempt
    os.system("cls" if os.name == 'nt' else "clear")

# Output the result once the password is found
print(f"Your password is: {pw}")
