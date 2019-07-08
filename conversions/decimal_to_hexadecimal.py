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
    """ take decimal value, return hexadecimal representation as str """
    hexadecimal = ''
    while decimal > 0:
        remainder = decimal % 16
        decimal -= remainder
        hexadecimal = values[remainder] + hexadecimal
        decimal /= 16
    return hexadecimal

def main():
    """ print test cases """
    print("5 in hexadecimal is", decimal_to_hexadecimal(5))
    print("15 in hexadecimal is", decimal_to_hexadecimal(15))
    print("37 in hexadecimal is", decimal_to_hexadecimal(37))
    print("255 in hexadecimal is", decimal_to_hexadecimal(255))
    print("4096 in hexadecimal is", decimal_to_hexadecimal(4096))
    print("999098 in hexadecimal is", decimal_to_hexadecimal(999098))

if __name__ == '__main__':
    main()