import time
import os
from win10toast import ToastNotifier
toaster = ToastNotifier()
  
birthdayFile = 'reminder.data'
  
def checkTodaysBirthdays():
    fileName = open(birthdayFile, 'r')
    today = time.strftime('%m%d')
    flag = 0
    for line in fileName:
        if today in line:
            line = line.split(' ')
            flag =1            
            toaster.show_toast("Today's Birthday", line[1]+ ' ' + line[2] + '"')
    if flag == 0:
            toaster.show_toast("No Birthdays Today!")
  
if __name__ == '__main__':
    checkTodaysBirthdays()

time.sleep(2)
quit