import random


def generate_magic_number(user_input):

    try:
        input_number = int(user_input)
    except ValueError:
        return "Invalid input. Please enter a valid integer."


    random_num = random.randint(1000, 9999)


    magic_number = f"{input_number}{random_num}"

    return magic_number



user_input = input("Enter an integer: ")


magic_number = generate_magic_number(user_input)
print(f"Magic Number: {magic_number}")
