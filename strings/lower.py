

def lower(word):

    ''' 
    Will convert the entire string to lowecase letters 
    
    >>> lower("wow")
    'wow'
    >>> lower("HellZo")
    'hellzo'
    >>> lower("WHAT")
    'what'
    
    >>> lower("wh[]32")
    'wh[]32'
    >>> lower("whAT")
    'what'
    '''
    lower_string = ""

    for char in word:
        # converting to ascii value int value and checking to see if char is a capital letter
        # if it is a capital letter it is getting shift by 32 which makes it a lower case letter
        if ord(char) >= 65 and ord(char) <= 90:
            lower_string += chr(ord(char) + 32)
        else:
            lower_string += char

    return lower_string



if __name__ == "__main__":
    from doctest import testmod
    testmod()
    