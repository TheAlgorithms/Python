def octal_to_binary(octal:str) -> str:
    """
   Convert an octal value to its binary equivalent
   >>> octal_to_binary("")
   Traceback (most recent call last):
       ...
   ValueError: Empty string was passed to the function
   >>> octal_to_binary("-")
   Traceback (most recent call last):
       ...
   ValueError: Non-octal value was passed to the function
   >>> octal_to_binary("e")
   Traceback (most recent call last):
       ...
   ValueError: Non-octal value was passed to the function
   >>> octal_to_binary(8)
   Traceback (most recent call last):
       ...
   ValueError: Non-octal value was passed to the function
   >>> octal_to_binary("-e")
   Traceback (most recent call last):
       ...
   ValueError: Non-octal value was passed to the function
   >>> octal_to_binary("-8")
   Traceback (most recent call last):
       ...
   ValueError: Non-octal value was passed to the function
   >>> octal_to_binary("1")
   '0b1'
   >>> octal_to_binary("-1")
   '-0b1'
   >>> octal_to_binary("12")
   '0b1010'
   >>> octal_to_binary(" 12   ")
   '0b1010'
   >>> octal_to_binary("-45")
   '-0b100101'
   >>> octal_to_binary("-")
   Traceback (most recent call last):
       ...
   ValueError: Non-octal value was passed to the function
   >>> octal_to_binary("0")
   '0b0'
   >>> octal_to_binary("-4055")
   '-0b100000101101'
   >>> octal_to_binary("2-0Fm")
   Traceback (most recent call last):
       ...
   ValueError: Non-octal value was passed to the function
   >>> octal_to_binary("")
   Traceback (most recent call last):
       ...
   ValueError: Empty string was passed to the function
   >>> octal_to_binary("19")
   Traceback (most recent call last):
       ...
   ValueError: Non-octal value was passed to the function
   """
    oct_string = str(octal).strip()
    if not oct_string:
        raise ValueError("Empty string was passed to the function")
    is_negative = oct_string.startswith('-')
    if is_negative:
        oct_string = oct_string[1:]
        binary_num = '-0b'
    else:
        binary_num = '0b'
    if not oct_string.isdigit() or not all(0 <= int(char) <= 7 for char in oct_string):
        raise ValueError("Non-octal value was passed to the function")
    binary_num += str(bin(int(oct_string, 8)))[2:]
    return binary_num
if __name__ == "__main__":
    from doctest import testmod
    testmod()
