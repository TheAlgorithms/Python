def is_upper(string):
    """
    Check if all characters in the string are uppercase letters.
    
    Args:
        string (str): The input string.
        
    Returns:
        bool: True if all characters in the string are uppercase letters, False otherwise.
    """
    return all(ord(char) >= 65 and ord(char) <= 90 for char in string)

def is_lower(string):
    """
    Check if all characters in the string are lowercase letters.
    
    Args:
        string (str): The input string.
        
    Returns:
        bool: True if all characters in the string are lowercase letters, False otherwise.
    """
    return all(ord(char) >= 97 and ord(char) <= 122 for char in string)

def is_alpha(string):
    """
    Check if all characters in the string are alphabetical (letters).
    
    Args:
        string (str): The input string.
        
    Returns:
        bool: True if all characters in the string are letters, False otherwise.
    """
    return all(char.isalpha() for char in string)

def is_alnum(string):
    """
    Check if all characters in the string are alphanumeric (letters or digits).
    
    Args:
        string (str): The input string.
        
    Returns:
        bool: True if all characters in the string are letters or digits, False otherwise.
    """
    return all(char.isalnum() for char in string)

def is_decimal(string):
    """
    Check if all characters in the string are decimal digits.
    
    Args:
        string (str): The input string.
        
    Returns:
        bool: True if all characters in the string are decimal digits, False otherwise.
    """
    return all(char.isdigit() for char in string)

def is_space(string):
    """
    Check if all characters in the string are whitespace characters.
    
    Args:
        string (str): The input string.
        
    Returns:
        bool: True if all characters in the string are whitespace characters, False otherwise.
    """
    return all(char.isspace() for char in string)

def is_title(string):
    """
    Check if the string is in title case (first letter of each word is capital).
    
    Args:
        string (str): The input string.
        
    Returns:
        bool: True if the string is in title case, False otherwise.
    """
    return string.istitle()

