from random import *
import os

u_pwd = input("enter a password")
pwd = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "1",
    "2",
    "3",
    "4",
    "5",
    "6",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "w",
    "v",
    "x",
    "y",
    "z",
]
pw = ""
while pw != u_pwd:
    pw = ""
    for letter in range(len(u_pwd)):
        guess_pwd = pwd[randint(0, 17)]
        pw = str(guess_pwd) + str(pw)
        print(pw)
        print("cracking password...")
        os.system("cls")
print("your password is-", pw)
