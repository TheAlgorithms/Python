import random as ra
import string as str


def options():
    while True:
        print("========== Welcome To Message Encryption ==========")
        print("\t'1' For Encryption")
        print("\t'2' For Decode")
        try:
            opt = int(input("Enter: "))
            if opt not in ("1", "2", 1, 2):
                print("Choose Number Between '1','2'")
            if opt == 1:
                encrypt()
            elif opt == 2:
                decode()
        except ValueError:
            print("Enter Numbers Only")


def encrypt():
    x = input("Enter Your Message :")

    if len(x) <= 3:
        encrypt_key = input("Enter Your Key '1','4','7' :")

        with open("User_Key.txt", "a+") as f:
            f.write(f"{encrypt_key},{x}\n")
        print(f"Successfully Encrypted: {x[::-1]}")

    encrypt_key = input("Enter Your Key '1','4','7' :")

    with open("User_Key.txt", "a") as f:
        f.write(f"{encrypt_key},{x}\n")
    shift = x[1:] + x[0]
    prefix = "".join(ra.choice(str.ascii_letters) for _ in range(3))
    suffix = "".join(ra.choice(str.ascii_letters) for _ in range(3))
    message = prefix + shift + suffix
    message = message.strip()
    print(f"Successfully Encrypted: {message}")
    return encrypt_key


def decode():
    with open("User_Key.txt", "r") as f:
        user_message = input("Enter Message To Decode : ")
        decode_key = input("Enter Your Key : ")
        found = False

        for line in f:
            encrypt_key, x = line.strip().split(",")

            if encrypt_key == decode_key:
                if len(user_message) <= 3:
                    print(user_message[::-1])
                else:
                    x = user_message[3:-3]
                    x = x[-1] + x[:-1]
                    print(f"Message Decoded : {x}")

                found = True
                break

        if not found:
            print("Didn't Match :/")


options()
