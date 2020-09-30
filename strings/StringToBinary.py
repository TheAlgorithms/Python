text = input('Enter Text : ')

for chr in text:
    bin = ''
    asciiVal = int(ord(chr))
    while asciiVal > 0:
        if asciiVal % 2 == 0:
            bin = bin + '0'
        else:
            bin = bin + '1'
        asciiVal = int(asciiVal/2)
    print(bin + " : " + bin[::-1]
