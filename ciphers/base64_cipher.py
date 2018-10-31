import base64

def main():
    inp = input('->')
    encoded = inp.encode('utf-8') #encoded the input (we need a bytes like object)
    b64encoded = base64.b64encode(encoded) #b64encoded the encoded string
    print(b64encoded)
    print(base64.b64decode(b64encoded).decode('utf-8'))#decoded it

if __name__ == '__main__':
    main()
