import random


def generate_magic_number(user_input):
    # Check if the user input is a valid integer
    try:
        input_number = int(user_input)
    except ValueError:
        return "Invalid input. Please enter a valid integer."

    # Generate a random 4-digit number
    random_num = random.randint(1000, 9999)

    # Combine the user input and the random number to create a magic number
    magic_number = f"{input_number}{random_num}"

    return magic_number


# Get user input
user_input = input("Enter an integer: ")

# Generate and print the magic number
magic_number = generate_magic_number(user_input)
print(f"Magic Number: {magic_number}")
