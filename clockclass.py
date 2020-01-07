
from time import sleep
from colorama import Fore
class Clock:
    def __init__(self,hours=0,minutes=0,seconds=0):
        '''
        I created instances for hours,minutes,seconds
        
        '''
        self.hours=hours
        self.minutes=minutes
        self.seconds=seconds

        '''
        run method starts the clock.

        '''

    def run(self):
        self.seconds+=1
        if self.seconds==60:
            self.seconds=0
            self.minutes+=1
            if self.minutes==60:
                self.minutes=0
                self.hours+=1
                if self.hours==24:
                    self.hours=0

        '''
        Show method shows the time
        I added extra space infront of time because cursor shows at the starting.

        '''
    def show(self):
        return ' %02d:%02d:%02d'%(self.hours,self.minutes,self.seconds)

'''
main function actually runs the program.
I used colorama to show the clock in yellow colour

'''

def main(hours,minutes,seconds=0):
    time=Clock(hours,minutes,seconds)
    while True:
        print(Fore.YELLOW+time.show(),end='\r')#end='\r' this represents flusing out the output and printing the new output in same position
        sleep(1)
        time.run()
'''
This is the main program

'''

if __name__ == "__main__":
    try:
        hours=int(input('Enter what hours'))
        minutes=int(input('Enter minutes'))
        main(hours,minutes)
    except:
        main(0,0,0)
