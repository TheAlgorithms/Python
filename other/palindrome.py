# Program to find whether given string is palindrome or not
def is_palindrome(str):
    """
    This function return True is given string is Palindrom other wise return False.

    >>> is_palindrome('MALAYALAM')
    True
    >>> is_palindrome('String')
    False
    >>> is_palindrome('rotor')
    True
    >>> is_palindrome('level')
    True
    >>> is_palindrome('A')
    True
    >>> is_palindrome('BB')
    True
    >>> is_palindrome('ABC')
    False
    """
    
    
    start_i = 0
    end_i = len(str) - 1
    while start_i < end_i:
        if str[start_i] == str[end_i]:
            start_i += 1
            end_i -= 1
        else:
            return False
    return True


# Recursive method
def recursive_palindrome(str):
    if len(str) <= 1:
        return True
    if str[0] == str[len(str) - 1]:
        return recursive_palindrome(str[1:-1])
    else:
        return False


def main():
    str = "ama"
    print(recursive_palindrome(str.lower()))
    print(is_palindrome(str.lower()))


if __name__ == "__main__":
    main()
