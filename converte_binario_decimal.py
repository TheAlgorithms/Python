def converterb_d(n):
    decimal = 0
    n = str(n)
    n = n[::-1]
    tam = len(n)
    for i in range(tam):
        if n[i] == "1":
            decimal = decimal + 2**i
    return decimal

def main():
    
    binar = input('Digite o número binário: ')
    b_d = converterb_d(binar)
    print ('O número binário {} corresponde a {} em decimal'.format(binar,b_d ))
    
main()
