def encrypt(key,val):
    le = len(key)
    enc = ''
    for i in range(len(val)):
        enc += chr((ord(val[i]) ^ ord(key[i % le])) % 0xff)
    return enc.encode('hex')

def main():
    key = raw_input("enter your key: ")
    plain = raw_input("enter your msg: ")

    print("encrypted msg, encoded with hex: " + encrypt(key,plain))

if __name__ == "__main__":
    main()