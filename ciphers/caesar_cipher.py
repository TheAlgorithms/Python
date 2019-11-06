def encrypt(input_string: str, key: int) -> str:
    result = ""
    for x in input_string:
        if not x.isalpha():
            result += x
        elif x.isupper():
            result += chr((ord(x) + key - 65) % 26 + 65)
        elif x.islower():
            result += chr((ord(x) + key - 97) % 26 + 97)
    return result


def decrypt(input_string: str, key: int) -> str:
    result = ""
    for x in input_string:
        if not x.isalpha():
            result += x
        elif x.isupper():
            result += chr((ord(x) - key - 65) % 26 + 65)
        elif x.islower():
            result += chr((ord(x) - key - 97) % 26 + 97)
    return result


def brute_force(input_string: str) -> None:
    key = 1
    result = ""
    while key <= 94:
        for x in input_string:
            indx = (ord(x) - key) % 256
            if indx < 32:
                indx = indx + 95
            result = result + chr(indx)
        print(f"Key: {key}\t| Message: {result}")
        result = ""
        key += 1
    return None


def main():
    while True:
        print(f'{"-" * 10}\n Menu\n{"-", * 10}')
        print(*["1.Encrpyt", "2.Decrypt", "3.BruteForce", "4.Quit"], sep="\n")
        choice = input("What would you like to do?: ")
        if choice not in ["1", "2", "3", "4"]:
            print("Invalid choice, please enter a valid choice")
        elif choice == "1":
            input_string = input("Please enter the string to be encrypted: ")
            key = int(input("Please enter off-set between 0-25: "))
            if key in range(1, 95):
                print(encrypt(input_string.lower(), key))
        elif choice == "2":
            input_string = input("Please enter the string to be decrypted: ")
            key = int(input("Please enter off-set between 1-94: "))
            if key in range(1, 95):
                print(decrypt(input_string, key))
        elif choice == "3":
            input_string = input("Please enter the string to be decrypted: ")
            brute_force(input_string)
            main()
        elif choice == "4":
            print("Goodbye.")
            break


if __name__ == "__main__":
    main()
