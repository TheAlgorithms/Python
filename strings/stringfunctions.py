def is_upper(string: str) -> bool:
    """
    Check if all characters in the string are uppercase letters.
    
    Args:
        string (str): The input string.
        
    Returns:
        bool: True if all characters in the string are uppercase letters, False otherwise.
    """
    return all(ord(char) >= 65 and ord(char) <= 90 for char in string)

def is_lower(string: str) -> bool:
    """
    Check if all characters in the string are lowercase letters.
    
    Args:
        string (str): The input string.
        
    Returns:
        bool: True if all characters in the string are lowercase letters, False otherwise.
    """
    return all(ord(char) >= 97 and ord(char) <= 122 for char in string)

def is_alpha(string: str) -> bool:
    """
    Check if all characters in the string are alphabetical (letters).
    
    Args:
        string (str): The input string.
        
    Returns:
        bool: True if all characters in the string are letters, False otherwise.
    """
    return all(char.isalpha() for char in string)

def is_alnum(string: str) -> bool:
    """
    Check if all characters in the string are alphanumeric (letters or digits).
    
    Args:
        string (str): The input string.
        
    Returns:
        bool: True if all characters in the string are letters or digits, False otherwise.
    """
    return all(char.isalnum() for char in string)

def is_decimal(string: str) -> bool:
    """
    Check if all characters in the string are decimal digits.
    
    Args:
        string (str): The input string.
        
    Returns:
        bool: True if all characters in the string are decimal digits, False otherwise.
    """
    return all(char.isdigit() for char in string)

def is_space(string: str) -> bool:
    """
    Check if all characters in the string are whitespace characters.
    
    Args:
        string (str): The input string.
        
    Returns:
        bool: True if all characters in the string are whitespace characters, False otherwise.
    """
    return all(char.isspace() for char in string)

def is_title(string: str) -> bool:
    """
    Check if the string is in title case (first letter of each word is capital).
    
    Args:
        string (str): The input string.
        
    Returns:
        bool: True if the string is in title case, False otherwise.
    """
    return string.istitle()

# Tests
assert is_upper("HELLO")
assert not is_upper("Hello")
assert is_lower("hello")
assert not is_lower("Hello")
assert is_alpha("Hello")
assert not is_alpha("Hello123")
assert is_alnum("Hello123")
assert not is_alnum("Hello 123")
assert is_decimal("12345")
assert not is_decimal("12.345")
assert is_space("    \t\n")
assert not is_space("Hello")
assert is_title("This Is A Title Case String")
assert not is_title("This is Not a Title Case String")

print("All tests passed!")