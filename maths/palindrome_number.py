def is_palindrome(number: int) -> bool:
    """
    Check whether a given integer is a palindrome.

    A palindrome number reads the same forwards and backwards.

    Examples:
    >>> is_palindrome(121)
    True
    >>> is_palindrome(123)
    False
    """
    number_str = str(number)
    return number_str == number_str[::-1]


if __name__ == "__main__":
    user_input = input("Enter a number: ").strip()

    if user_input.isdigit():
        number = int(user_input)
        if is_palindrome(number):
            print("The number is a palindrome.")
        else:
            print("The number is not a palindrome.")
    else:
        print("Please enter a valid non-negative integer.")
