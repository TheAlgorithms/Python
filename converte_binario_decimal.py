def convertb_d(n):
    decimal = 0
    n = str(n)
    n = n[::-1]
    lenght = len(n)
    for i in range(lenght):
        if n[i] == "1":
            decimal = decimal + 2**i
    return decimal

def main():
    
    binar = input('Enter the binary number: ')
    b_d = convertb_d(binar)
    print ('The binary number {} corresponds to {} in decimal'.format(binar,b_d ))
    
main()
