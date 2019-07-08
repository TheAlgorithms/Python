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
    while True:
        print('-' * 10 + "\n**Menu**\n" + '-' * 10)
        print("1.Encrpyt")
        print("2.Decrypt")
        print("3.BruteForce")
        print("4.Quit")
        choice = input("What would you like to do?: ")
        if choice not in ['1', '2', '3', '4']:
            print ("Invalid choice, please enter a valid choice")
        elif choice == '1':
            strng = input("Please enter the string to be encrypted: ")
            key = int(input("Please enter off-set between 1-94: "))
            if key in range(1, 95):
                print (encrypt(strng.lower(), key))
        elif choice == '2':
            strng = input("Please enter the string to be decrypted: ")
            key = int(input("Please enter off-set between 1-94: "))
            if key in range(1,95):
                print(decrypt(strng, key))
        elif choice == '3':
            strng = input("Please enter the string to be decrypted: ")
            brute_force(strng)
            main()
        elif choice == '4':
            print ("Goodbye.")
            break


if __name__ == '__main__':
    main()
