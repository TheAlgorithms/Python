# Function to convert Binary number to Gray code
def binary_to_gray(binary):
    # Convert binary (string) to integer
    binary = int(binary, 2)

    # Perform XOR between binary and binary right-shifted by 1 bit
    gray = binary ^ (binary >> 1)

    # Convert back to binary string and remove '0b' prefix
    gray_code = bin(gray)[2:]

    return gray_code


# --- Main Program ---

# Taking input from the user
binary_input = input("Enter a binary number: ")

# Input validation
if not all(bit in '01' for bit in binary_input):
    print("❌ Invalid input! Please enter a binary number (0s and 1s only).")
else:
    gray_result = binary_to_gray(binary_input)
    print(f"✅ The Gray code for binary {binary_input} is: {gray_result}")
