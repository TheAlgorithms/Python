def encrypt(strng, key):
    encrypted = ''
    for x in strng:
        if x.isalpha():
            if x.isupper():
                x = ord(x) - 65
                x = (x + key) % 26 + 65
                encrypted += chr(x)
            else:
                x = ord(x) - 97
                x = (x + key) % 26 + 97
                encrypted += chr(x)
        else:
            encrypted += x
    return encrypted

def decrypt(strng, key):
    decrypted = ''
    for x in strng:
        if x.isalpha():
            if x.isupper():
                x = ord(x) - 65
                x = (x - key) % 26 + 65
                decrypted += chr(x)
            else:
                x = ord(x) - 97
                x = (x - key) % 26 + 97
                decrypted += chr(x)
        else:
            decrypted += x
    return decrypted

def brute_force(strng):
    key = 0
    decrypted = ''
    while key < 26:
        for x in strng:
            if x.isalpha():
                if x.isupper():
                    x = ord(x) - 65
                    x = (x - key) % 26 + 65
                    decrypted += chr(x)
                else:
                    x = ord(x) - 97
                    x = (x - key) % 26 + 97
                    decrypted += chr(x)
            else:
                decrypted += x
        print("Key: {}\t| Message: {}".format(key, decrypted))
        decrypted = ''
        key += 1
    return None

def main():
    while True:
        print('-' * 10 + "\n**Menu**\n" + '-' * 10)
        print("1.Encrypt")
        print("2.Decrypt")
        print("3.BruteForce")
        print("4.Quit")
        choice = input("What would you like to do?: ")
        if choice not in ['1', '2', '3', '4']:
            print ("Invalid choice")
        elif choice == '1':
            strng = input("Please enter the string to be encrypted: ")
            key = int(input("Please enter off-set between 0-25: "))
            if key in range(0, 26):
                print (encrypt(strng, key))
            else:
                print("Invalid off-set")
        elif choice == '2':
            strng = input("Please enter the string to be decrypted: ")
            key = int(input("Please enter off-set between 0-25: "))
            if key in range(0, 26):
                print(decrypt(strng, key))
            else:
                print("Invalid off-set")
        elif choice == '3':
            strng = input("Please enter the string to be decrypted: ")
            brute_force(strng)
        elif choice == '4':
            print("Goodbye.")
            break

if __name__ == '__main__':
    main()