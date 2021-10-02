import random
def encrypter():
    file_crypt = open("crypt", "r")
    file_crypted = open("encrypted", "w+")
    for i in file_crypt.readlines():
        for y in range(len(i)):
                file_crypted.write(chr(ord(i[y])+2))
    file_crypted.close()
    file_crypt.close()
def decrypter():
    file_crypted = open("encrypted","r")
    file_copy = open("Decrypted", "w")
    for a in file_crypted.readlines():
        for t in range(len(a)):
                file_copy.write(chr(ord(a[t])-2))
    file_crypted.close()
    file_copy.close()
reply = "Y"
while(reply == "Y" or reply == "y"):
    x = input("ENTER E: IF YOU WANT TO ENCRYPT A MESSAGE OR D: TO DECRYPT THE MESSAGE: ")
    if x == "e" or x == "E":
        encrypter()
        print("Successfully Encrypted your message")
    elif x == "D" or x == "d":
        decrypter()
        print("Successfully Decrypted your message")
    reply = input("Press Y to Continue OR N to Exit: ")
    if reply != "N" and reply != "n" and reply != "Y" and reply != "y":
        print("Invalid answer")
