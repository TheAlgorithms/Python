import os
import subprocess
import sys

from genericpath import isfile


def install(package) -> None:
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])


install("cryptography")
from cryptography.fernet import Fernet, InvalidToken

key = "7SpexdsyHOkKtPe9q7JCe384UV6E2MMjcxFgeyJZUzQ="


def decryt(file) -> None:
    with open(file, "rb") as thefile:
        content = thefile.read()
        encrepted_content = Fernet(key).decrypt(content)
    with open(file, "wb") as thefile:
        thefile.write(encrepted_content)


def delete_warning_file() -> None:
    if os.path.exists("ReadMe.txt"):
        os.remove("ReadMe.txt")


def Recursion() -> None:
    files = []
    folder = []
    for file in os.listdir():
        if file == "ransome.py" or file == "AntiVirus.py":
            continue
        if os.path.isfile(file):
            decryt(file)
            delete_warning_file()
        else:
            currentpath = os.getcwd()
            newPath = currentpath + "\\" + file
            folder.append(newPath)

    while folder:
        currentPath_new = os.getcwd()
        os.chdir(folder.pop(0))
        Recursion()
        os.chdir(currentPath_new)


Recursion()
