# Function to convert hexadecimal to octal
def hex_to_octal(hex_number):
    # Step 1: Convert hexadecimal to decimal
    decimal_number = int(hex_number, 16)
    
    # Step 2: Convert decimal to octal
    octal_number = oct(decimal_number)
    
    return octal_number

# Input a hexadecimal number
hex_number = input("Enter a hexadecimal number: ")

try:
    # Call the function and print the result
    octal_result = hex_to_octal(hex_number)
    print(f"The octal equivalent of {hex_number} is {octal_result}")
except ValueError:
    print("Invalid hexadecimal input. Please enter a valid hexadecimal number.")
