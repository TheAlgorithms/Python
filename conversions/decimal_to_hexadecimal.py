""" Convert Base 10 (Decimal) Values to Hexadecimal Representations """

# set decimal value for each hexadecimal digit
values = {
    0:'0',
    1:'1',
    2:'2',
    3:'3',
    4:'4',
    5:'5',
    6:'6',
    7:'7',
    8:'8',
    9:'9',
    10:'a',
    11:'b',
    12:'c',
    13:'d',
    14:'e',
    15:'f'
}

def decimal_to_hexadecimal(decimal):
    """
        take integer decimal value, return hexadecimal representation as str 
        >>> decimal_to_hexadecimal(5)
        '5'
        >>> decimal_to_hexadecimal(15)
        'f'
        >>> decimal_to_hexadecimal(37)
        '25'
        >>> decimal_to_hexadecimal(255)
        'ff'
        >>> decimal_to_hexadecimal(4096)
        '1000'
        >>> decimal_to_hexadecimal(999098)
        'f3eba'
    """
    hexadecimal = ''
    while decimal > 0:
        remainder = decimal % 16
        decimal -= remainder
        hexadecimal = values[remainder] + hexadecimal
        decimal /= 16
    return hexadecimal

if __name__ == '__main__':
    import doctest
    doctest.testmod()
