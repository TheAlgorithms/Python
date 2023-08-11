octal_number = input("Enter an octal number: ")
decimal_number = int(octal_number, 8)  # Convert octal to decimal
binary_number = bin(decimal_number)     # Convert decimal to binary

print(f"The binary representation of {octal_number} is {binary_number}")
