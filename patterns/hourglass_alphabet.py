#define function 
def print_hourglass(rows):
    #print reverse pyramid
    for i in range(rows - 1):
        for j in range(i):
            print(' ', end='')
        for k in range(2 * (rows - i) - 1):
            print(chr(65 + k), end='')
        print()

    #print upright pyramid
    for i in range(rows):
        for j in range(rows - i - 1):
            print(' ', end='')
        for k in range(2 * i + 1):
            print(chr(65 + k), end='')
        print()

#rows to be spanned 
n = 7

#call the function 
print_hourglass(n)
