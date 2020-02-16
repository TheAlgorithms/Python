def is_palindrome(s):
    """
    Determine whether the string is palindrome
    :param s:
    :return: Boolean
    """
    return s == s[::-1]



s = str(input("Enter string to determine whether its palindrome or not: ").strip())
if is_palindrome(s):
    print("Given string is palindrome")
else:
    print("Given string is not palindrome")
