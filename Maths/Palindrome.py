def palindrome(n):
    # Saving n value for later
    original = n
    reverse = 0
    while n != 0:
        # Shift reversed number to 1 digit to the left
        reverse *= 10
        # Add the last digit of n to the end of reversed number
        reverse += n % 10
        # Shift n to 1 digit to the right
        n //= 10

    # check if n can be read backwards. Return True if n is a palindrome.
    if reverse == original:
        return True
    else:
        return False


# check the function above
print(101, palindrome(101))
print(1234, palindrome(1234))
print(123321, palindrome(123321))
print(12321, palindrome(12321))
print(12343210, palindrome(12343210))
