#Author-Slayking1965
#email-kingslayer8509@gmail.com
import random
import pyautogui
import string


chars = "abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

chars = string.printable
chars_list = list(chars)


password = pyautogui.password("Enter a password : ")

guess_password = ""

while(guess_password != password):
    guess_password = random.choices(chars_list, k=len(password))

    print("<=================="+ str(guess_password)+ "==================>")

    if(guess_password == list(password)):
        print("Your password is : "+ "".join(guess_password))
        break
        #please accept my pull request sir/ma'am
