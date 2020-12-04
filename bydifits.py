import sys

zero = ["***","*","**","****"]
one = ["*   *","* *","*  *","*"]
two = ["*   *"," *","*","*"]
third = ["***","*****","*****","****"]

Digits = ["zero","one","two","third"]

try:
    Digits = sys.argv[1]
    row = 0
    while row < 7:
        while column < len(Digits):
            number = int(Digits[column])
            digit = Digits[number]
            line += digit[row] + "  "
            column += 1
            print(line)
            row += 1
except IndexError:
    print("usage: bidigits.py <number>")
except ValueError as err:
    print(err, "in", digits)
