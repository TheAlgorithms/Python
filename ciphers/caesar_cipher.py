import sys
def encrypt(strng, key):
    encrypted = ''
    for x in strng:
        indx = (ord(x) + key) % 256
        if indx > 126:
            indx = indx - 95
        encrypted = encrypted + chr(indx)
    return encrypted


def decrypt(strng, key):
    decrypted = ''
    for x in strng:
        indx = (ord(x) - key) % 256
        if indx < 32:
            indx = indx + 95
        decrypted = decrypted + chr(indx)
    return decrypted

def brute_force(strng):
    key = 1
    decrypted = ''
    while key <= 94:
        for x in strng:
            indx = (ord(x) - key) % 256
            if indx < 32:
                indx = indx + 95
            decrypted = decrypted + chr(indx)
        print("Key: {}\t| Message: {}".format(key, decrypted))
        decrypted = ''
        key += 1
    return None


def main():
    print('-' * 10 + "\n**Menu**\n" + '-' * 10)
    print("1.Encrpyt")
    print("2.Decrypt")
    print("3.BruteForce")
    print("4.Quit")
    while True:
        choice = raw_input("What would you like to do?: ")
        if choice not in ['1', '2', '3', '4']:
            print ("Invalid choice")
        elif choice == '1':
            strng = raw_input("Please enter the string to be ecrypted: ")
            while True:
                key = int(input("Please enter off-set between 1-94: "))
                if key in range(1, 95):
                    print (encrypt(strng, key))
                    main()
        elif choice == '2':
            strng = raw_input("Please enter the string to be decrypted: ")
            while True:
                key = raw_int(input("Please enter off-set between 1-94: "))
                if key > 0 and key <= 94:
                    print(decrypt(strng, key))
                    main()
        elif choice == '3':
            strng = raw_input("Please enter the string to be decrypted: ")
            brute_force(strng)
            main()
        elif choice == '4':
            print ("Goodbye.")
            sys.exit()

main()
