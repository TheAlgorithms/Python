def is_palindrome(s):
    """
    Determine whether the string is palindrome
    :param s:
    :return: Boolean
    """
    if s == s[::-1]:
        return True
    return False


s = input("Enter string to determine whether its palindrome or not: ")
if is_palindrome(s):
    print("Given string is palindrome")
else:
    print("Given string is not palindrome")
