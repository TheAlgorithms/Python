def upper(word):
    ''' 
    Will convert the entire string to uppercase letters 
    
    >>> upper("wow")
    'WOW'
    >>> upper("Hello")
    'HELLO'
    >>> upper("WHAT")
    'WHAT'
    
    >>> upper("wh[]32")
    'WH[]32'
    '''
    upper_string = ""
    
    for char in word:
        # converting to ascii value int value and checking to see if char is a lower letter
        # if it is a capital letter it is getting shift by 32 which makes it a capital case letter
        if ord(char) >= 97 and ord(char) <= 122:
            upper_string += chr(ord(char) -32)
        else:
            upper_string += char
    
    return upper_string



if __name__ == "__main__":
    from doctest import testmod
    testmod()
    