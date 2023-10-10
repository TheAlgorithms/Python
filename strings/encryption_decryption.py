# secret code generator :
def code(input_string: str) -> str:
    """
    Encrypts the input string using a specific encryption algorithm.
    
    Args:
        input_string (str): The input string to be encrypted.
        
    Returns:
        str: The encrypted string.
        
    Examples:
        >>> code("hello")
        'olleh'
        
        >>> code("world")
        'dlrow'
    """
    encrypted_string = input_string[::-1]  # Example encryption: reverse the input string
    return encrypted_string

def decode(input_string: str) -> str:
    """
    Decrypts the input string using a specific decryption algorithm.
    
    Args:
        input_string (str): The input string to be decrypted.
        
    Returns:
        str: The decrypted string.
        
    Examples:
        >>> decode('olleh')
        'hello'
        
        >>> decode('dlrow')
        'world'
    """
    decrypted_string = input_string[::-1]  # Example decryption: reverse the input string
    return decrypted_string

if __name__ == "__main__":
    import doctest
    doctest.testmod()
str1 = "axz"
str2 = "byz"


def code() -> None:
    print("\n***YOU CAME TO CODING SECTION***\n")
    code = input(" enter string to be encripted :  ")
    if len(code) >= 3:
        code = code.split()
        new_code = " ".join(code)
        new_code = new_code[1:] + new_code[0]
        new_code = str1 + new_code + str2
        print(f" \n generated code is  {new_code}\n")
    else:
        print(f"\n code is  : {code[::-1]} \n")


def decode() -> None:  # def function() -> None:
    print("\n***YOU CAME TO DeCODING SECTION***\n")
    code = input(" \nenter string to be decripted :  ")
    if len(code) >= 3:
        code = code[3:-3]
        code = code[-1] + code[:-1]
        print(f" \n generated code is :  {''.join(code)}\n")
    else:
        print(f"\n code is  : {code[::-1]} \n")

    pass


while True:
    print(" \n1.Coding \n2. Decoding \n 3.exit")
    choice = int(input(" Please enter Ur choice"))
    match choice:
        case 1:
            code()
        case 2:
            decode()
        case 3:
            exit(1)
