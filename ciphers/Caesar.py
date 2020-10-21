__author__ = '@ansanbinoy'
def encrypt(m, off): #encrypts by adding an offset to each character and outputs a new encrypted character

    m = m.upper()

    newM = ""

    for i in m:

        if ord(i)+off > 90: #error checking - verifies that the ascii value for the new letter is in an appropriate range

            i = chr(ord(i)-26)

        elif ord(i)+off < 65:

            i = chr(ord(i)+26)

        newM += chr(ord(i)+off)

    print(newM)

def decrypt(m, off): #bascially works in the same way but subtracts the offset

    m = m.upper()

    newM = ""

    for i in m:

        if ord(i)-off > 90:

            i = chr(ord(i)-26)

        elif ord(i)-off < 65:

            i = chr(ord(i)+26)

        newM += chr(ord(i)-off)

    print(newM)

message = input("Please enter a message")

offset = int(input("Please enter an offset between -25 and 25"))

while offset >25 or offset < -25:

    offset = int(input("Offset not in range - enter again"))

option = input("Would you like to encrypt or decrypt")

while not (option == "e" or option == "d" or option == "E" or option == "D"):

    option = input("Invalid option, enter again")

if option == "e" or option == "E":

    encrypt(message, offset)

else:

    decrypt(message, offset)
