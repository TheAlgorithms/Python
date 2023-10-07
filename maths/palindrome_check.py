#A palindromic number (also known as a numeral palindrome or a numeric palindrome) is a number (such as 16461) that remains the same when its digits are reversed

def is_palindrome_number(number):
    # Convert the number to a string
    number_str = str(number)
    
    # Check if the string is equal to its reverse
    return number_str == number_str[::-1]

# Test the function
number = 121
if is_palindrome_number(number):
    print(f"{number} is a palindrome!")
else:
    print(f"{number} is not a palindrome.")

if __name__ == "__main__":
    import doctest

    doctest.testmod()
    main()

