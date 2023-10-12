# description: This program is a simple encryption and decryption program that uses the current time as the key.
# whatever you encrypt with the program can only be decrypted with the program and the exact time it was encypted.
# This program is not meant to be used for any serious encryption or decryption. It is just a fun project.
# Example: If you encrypt a text at 12:00 PM, you can only decrypt it at 12:00 PM. If you try to decrypt it at 12:01 PM, it will not work.
# or if you set key to day or month then you can only decrypt it on that day or month.

# This program is written in Python 3.8.2
# This program uses ceaser cipher encryption technique.

# Author: Aayush Kewat


import string
import time
import doctest

# defualt character list
char = " " + string.punctuation + string.ascii_letters + string.digits
char_list = list(char)


# function to shuffle the character list according to the time
def change_key()->None:
    global char_list
    global char
    global current_time
    var = int(1)
    var = var + int(current_time)
    while var > 24:
        var = var - 24
    if var == 1:
        char = " " + string.punctuation + string.ascii_letters + string.digits
    elif var == 2:
        char = " " + string.ascii_letters + string.punctuation + string.digits
    elif var == 3:
        char = " " + string.ascii_letters + string.digits + string.punctuation
    elif var == 4:
        char = " " + string.digits + string.ascii_letters + string.punctuation
    elif var == 5:
        char = " " + string.digits + string.punctuation + string.ascii_letters
    elif var == 6:
        char = " " + string.punctuation + string.digits + string.ascii_letters
    elif var == 7:
        char = string.punctuation + " " + string.ascii_letters + string.digits
    elif var == 8:
        char = string.ascii_letters + " " + string.punctuation + string.digits
    elif var == 9:
        char = string.ascii_letters + " " + string.digits + string.punctuation
    elif var == 10:
        char = string.digits + " " + string.ascii_letters + string.punctuation
    elif var == 11:
        char = string.digits + " " + string.punctuation + string.ascii_letters
    elif var == 12:
        char = string.punctuation + " " + string.digits + string.ascii_letters
    elif var == 13:
        char = string.ascii_letters + string.punctuation + " " + string.digits
    elif var == 14:
        char = string.ascii_letters + string.digits + " " + string.punctuation
    elif var == 15:
        char = string.digits + string.ascii_letters + " " + string.punctuation
    elif var == 16:
        char = string.digits + string.punctuation + " " + string.ascii_letters
    elif var == 17:
        char = string.punctuation + string.digits + " " + string.ascii_letters
    elif var == 18:
        char = string.ascii_letters + string.punctuation + string.digits + " "
    elif var == 19:
        char = string.ascii_letters + string.digits + string.punctuation + " "
    elif var == 20:
        char = string.digits + string.ascii_letters + string.punctuation + " "
    elif var == 21:
        char = string.digits + string.punctuation + string.ascii_letters + " "
    elif var == 22:
        char = string.punctuation + string.digits + string.ascii_letters + " "
    elif var == 23:
        char = string.ascii_letters + string.punctuation + string.digits + " "
    elif var == 24:
        char = string.ascii_letters + string.digits + string.punctuation + " "
    char_list = list(char)


# deault time
t = time.localtime()
current_time = time.strftime("%H", t)


# function to encrypt the text
def encryption()->None:
    password = input("Enter the text to be encrypted: ")
    passlist = list(password)
    change_key()
    for i in range(len(passlist)):
        passlist[i] = char_list.index(passlist[i])
        enctrpt = passlist[i] + int(current_time)
        if enctrpt > 94:
            enctrpt = enctrpt - 94
        passlist[i] = char_list[enctrpt]
    print("".join(passlist))


#  function to decrypt the text
def decryption()->None:
    password = input("Enter the text to be decrypted: ")
    passlist = list(password)
    change_key()
    for i in range(len(passlist)):
        passlist[i] = char_list.index(passlist[i])
        enctrpt = passlist[i] - int(current_time)
        if enctrpt < 0:
            enctrpt = enctrpt + 94
        passlist[i] = char_list[enctrpt]
    print("".join(passlist))


#  main program
doctest.testmod()
print("Welcome to the Encryption and Decryption Program")

print("Select the Encryption Key")
print("1. Month")
print("2. Day")
print("3. Hour")

option = input("Enter the option: ")
option = int(option)

if option == 1:
    current_time = time.strftime("%m", t)
elif option == 2:
    current_time = time.strftime("%d", t)
elif option == 3:
    current_time = time.strftime("%H", t)
else:
    print("Invalid Choice")


print("wants to encrypt or decrypt?")
print("1. Encrypt")
print("2. Decrypt")


choice = input("Enter the choice: ")
choice = int(choice)

if choice == 1:
    encryption()
elif choice == 2:
    decryption()
else:
    print("Invalid Choice")
