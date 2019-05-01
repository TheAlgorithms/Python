import sys


def encrypt(string, key):
    encrypted = ''
    for x in string:
        index = (ord(x) + key) % 256
        if index > 126:
            index = index - 95
        encrypted = encrypted + chr(index)
    return encrypted


def decrypt(string, key):
    decrypted = ''
    for x in string:
        index = (ord(x) - key) % 256
        if index < 32:
            index = index + 95
        decrypted = decrypted + chr(index)
    return decrypted


def brute_force(string):
    key = 1
    decrypted = ''
    while key <= 94:
        for x in string:
            index = (ord(x) - key) % 256
            if index < 32:
                index = index + 95
            decrypted = decrypted + chr(index)
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
            print("Invalid choice, please enter a valid choice")
        elif choice == '1':
            string = input("Please enter t  he string to be encrypted: ")
            key = int(input("Please enter off-set between 1-94: "))
            if key in range(1, 95):
                print(encrypt(string.lower(), key))
        elif choice == '2':
            string = input("Please enter the string to be decrypted: ")
            key = int(input("Please enter off-set between 1-94: "))
            if key in range(1, 95):
                print(decrypt(string, key))
        elif choice == '3':
            string = input("Please enter the string to be decrypted: ")
            brute_force(string)
            main()
        elif choice == '4':
            print("Goodbye.")
            break


main()
