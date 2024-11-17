def is_palindrome(input_value):
    # Convert the input to a string and remove spaces and special characters (for phrases)
    sanitized_value = "".join(filter(str.isalnum, str(input_value))).lower()

    # Check if the sanitized string is equal to its reverse
    return sanitized_value == sanitized_value[::-1]


input_value = input("Enter a phrase, word, or number to check if it's a palindrome: ")
if is_palindrome(input_value):
    print("The input is a palindrome.")
else:
    print("The input is not a palindrome.")
