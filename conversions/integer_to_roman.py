def integer_to_roman(num: int) -> str:
    """
    LeetCode No. 12. Integer to Roman
    Given a integer numeral, convert it to an roman.
    https://en.wikipedia.org/wiki/Roman_numerals
    >>> tests = {3: "III", 154: "CLIV", 3999: "MMMCMXCIX"}
    >>> all(integer_to_roman(key) == value for key, value in tests.items())
    True
    """

    roman_dict = { 
            1000:'M',
            900:'CM',
            500:'D',
            400:'CD',
            100:'C',
            90:'XC',
            50:'L',
            40:'XL',
            10:'X',
            9:'IX',
            5:'V',
            4:'IV',
            1:'I'}
    ret=''
    for k in roman_dict:
        while(num-k>=0):
            num-=k
            ret+=roman_dict[k]
    return ret

if __name__ == "__main__":
    import doctest

    doctest.testmod()
