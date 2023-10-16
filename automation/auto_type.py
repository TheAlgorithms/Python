import time

import keyboard
from pynput.keyboard import Controller, Key

# assign controller to auto
auto = Controller()


# main function for auto typing
def auto_type(n):
    for i in n.split("\n"):
        auto.type(i)
        auto.press(Key.enter)
        time.sleep(0.1)  # adjust the speed according to your need


# code or text to be autotyped
# please comment the code after inserting your code (refer the demo code below)
n = """
# def pattern(num):
#     x=''
#     for i in range(1,num+1):
#         x+=str(i)+' '
#         print(x)
# pattern(5)
"""


# A function that will be executed when the hotkey is pressed
def hotkey_pressed():
    auto_type(n)


# A loop to check for keyboard events
while True:
    if keyboard.is_pressed("shift"):
        hotkey_pressed()
    # Check for an exit condition, such as the 'esc' key
    if keyboard.is_pressed("esc"):
        print("Exiting the program.")
        break