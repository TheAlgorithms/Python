"""
This is a bot could be used to create on a text field such as whatsapp or youtube chats
It includes following packages in place :-
-pyautogui
To install required packages, use command 
for windows -
    pip install pyautogui
    pip install pillow
for linux
    apt-get install python-tk
    pip3 install pyautogui
    pip3 install pillow
"""

import pyautogui as pp

def spambot():
    while(True):
        try:
            spam_times = pp.prompt(text="Enter the number of messages you wanted to spam !!!", title = 'ChatBot', default = '0')
            spam_times = int(spam_times)
            break
        except Exception as e:
            if(spam_times is None): 
                exit()
            pp.alert(text='Please enter numric value')
            continue

    spam_message = pp.prompt(text="Enter the message you wanted to send !!!", title = 'ChatBot', default = 'This is spam!!')
    
    while(True):
        try:
            spam_rate = float(pp.prompt(text="Enter the rate at which you wanted to spam !!! default is 0.005 (in seconds)", title = 'ChatBot', default = '0.005'))
            spam_rate = float(spam_rate)
            break
        except Exception as e:
            if(spam_rate is None): 
                exit()
            pp.alert(text='Please enter numric or decimal value')
            continue
        
    while(True):
        try:
            waiting_time = float(pp.prompt(text="Enter the time you need to take to reach desired text field !!! default is 10 (in seconds)", title = 'ChatBot', default = '10'))
            waiting_time = float(waiting_time)
            break
        except Exception as e:
            if(spam_rate is None): 
                exit()
            pp.alert(text='Please enter numric or decimal value')
            continue

    for _ in range(spam_times):
        pp.write(spam_message, 0, 'enter')
        pp.sleep(spam_rate)

if __name__ == "__main__":
    spambot()    