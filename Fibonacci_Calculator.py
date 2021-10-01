from tkinter import *
from tkinter import ttk



class Calculator:
    calVal = 0.0

    divTrigger = False
    multTrigger = False
    addTrigger = False
    subtractTrigger = False
    factorialTrigger = False
    fibTrigger = False

    # The function where the user clicks on number button
    # We need to add the digit until we get a number
    def button_press(self, value):

        # Get the current value in the entry
        entryVal = self.number_entry.get()
        entryVal += value
        # Clear the entry box
        self.number_entry.delete(0, "end")
        # Insert the new value going from left to right
        self.number_entry.insert(0, entryVal)

    def isFloat(self,strVal):
        try:
            float(strVal)
            return True
        except ValueError:
            return False

    # The function where the user clicks on an operation
    def math_button_press(self, value):
        if self.isFloat(str(self.number_entry.get())):
            self.divTrigger = False
            self.multTrigger = False
            self.addTrigger = False
            self.subtractTrigger = False

            self.calcVal = float(self.entryVal.get())

            if(value == "/"):
                print("/ was pressed")
                self.divTrigger = True
            elif( value == "*"):
                print("* was pressed")
                self.multTrigger = True
            elif( value == "+"):
                print("+ was pressed")
                self.addTrigger = True
            else:
                print("- was pressed")
                self.subtractTrigger = True

            self.number_entry.delete(0, "end")






    def special_button_press(self,value):
        if(value == "Factorial" or value == "Nth Fibonacci"):
            if(value == "Factorial"):
                print("! was pressed")
                solution = getFact(int(self.entryVal.get()))
            else:
                print("Nth Fibonacci was pressed")
                solution = getFib(int(self.entryVal.get()))

        self.number_entry.delete(0, "end")
        self.number_entry.insert(0, solution)





    # Clear everything
    def clear_button_press(self):
        print("Clearing everything")
        self.divTrigger = False
        self.multTrigger = False
        self.addTrigger = False
        self.subtractTrigger = False
        self.calVal = 0.0
        self.number_entry.delete(0, "end")


    def equal_button_press(self):
        if (self.addTrigger or self.subtractTrigger or self.divTrigger or self.multTrigger):
            if self.addTrigger:
                solution = self.calcVal + float(self.entryVal.get())
            elif self.subtractTrigger:
                solution = self.calcVal - float(self.entryVal.get())
            elif self.multTrigger:
                solution = self.calcVal * float(self.entryVal.get())
            else:
                if (self.entryVal.get()) == '0':
                    solution = "UNDEFINED"
                else:
                    solution = self.calcVal / float(self.entryVal.get())

        print(self.calcVal,"   ", float(self.entryVal.get()),"  ",solution)
        self.number_entry.delete(0, "end")
        self.number_entry.insert(0, solution)

    def __init__(self, root):
        self.entryVal = StringVar(root, value="")
        root.title("Calculator")
        root.geometry("597x344")
        root.resizable(width=False, height=False)

        style = ttk.Style()
        style.configure("TButton", font="Serif 15", padding=10)
        style.configure("TEntry", font="Serif 35", padding=10)

        self.number_entry = ttk.Entry(root,
                                      textvariable=self.entryVal, width=95,justify='center')
        self.number_entry.grid(row=0, columnspan=4)

        self.button7 = ttk.Button(root, text = "7",
                                  command = lambda:self.button_press('7')).grid(row = 1, column = 0)

        self.button8 = ttk.Button(root, text = "8",
                                  command = lambda:self.button_press('8')).grid(row = 1, column = 1)

        self.button9 = ttk.Button(root, text = "9",
                                  command = lambda:self.button_press('9')).grid(row = 1, column = 2)

        self.buttonDiv = ttk.Button(root, text="/",
                                    command=lambda: self.math_button_press('/')).grid(row = 1, column = 3)

        # Start of the second row

        self.button4 = ttk.Button(root, text = "4",
                                  command = lambda:self.button_press('4')).grid(row = 2, column = 0)

        self.button5 = ttk.Button(root, text = "5",
                                  command = lambda:self.button_press('5')).grid(row = 2, column = 1)

        self.button6 = ttk.Button(root, text = "6",
                                  command = lambda:self.button_press('6')).grid(row = 2, column = 2)

        self.buttonMult = ttk.Button(root, text = "*",
                                    command = lambda:self.math_button_press('*')).grid(row = 2, column = 3)

        # Start of the third row

        self.button1 = ttk.Button(root, text = "1",
                                  command = lambda:self.button_press('1')).grid(row = 3, column = 0)

        self.button2 = ttk.Button(root, text = "2",
                                  command = lambda:self.button_press('2')).grid(row = 3, column = 1)

        self.button3 = ttk.Button(root, text = "3",
                                  command = lambda:self.button_press('3')).grid(row = 3, column = 2)

        self.buttonAdd = ttk.Button(root, text = "+",
                                    command = lambda:self.math_button_press('+')).grid(row = 3, column = 3)

        # Start of the fourth row

        self.buttonAC = ttk.Button(root, text = "AC",
                                    command = lambda:self.clear_button_press()).grid(row = 4, column = 0)

        self.button0 = ttk.Button(root, text = "0",
                                    command = lambda:self.button_press('0')).grid(row = 4, column = 1)

        self.buttonEqual = ttk.Button(root, text = "=",
                                    command = lambda:self.equal_button_press()).grid(row = 4, column = 2)

        self.buttonSub = ttk.Button(root, text = "-",
                                    command = lambda:self.math_button_press('-')).grid(row = 4, column = 3)

        # Start of the fifth row
        self.specialLabel = ttk.Label(root, text="\n\n\t\t\t\t\tSpecial Functions", width=95)
        self.specialLabel.grid(row=5, columnspan=4)

        # Start of the sixth row

        self.buttonFactorial = ttk.Button(root, text = "Factorial",
                                  command = lambda:self.special_button_press('Factorial')).grid(row = 6, column = 1)

        self.buttonFib = ttk.Button(root, text = "Nth Fibonacci",
                                      command = lambda:self.special_button_press('Nth Fibonacci')).grid(row = 6, column = 2)






def getFact(n):
    if(n < 0):
        return "Error"
    elif(n == 0):
        return 1
    else:
        return n * getFact(n-1)


def getFib(n):
    if(n<=0):
        return 0

    arr = [0]*(n+1)

    arr[0] = 0
    arr[1] = 1

    for i in range(2, n+1):
        arr[i] = arr[i-1] + arr[i-2]

    return arr[n]



root = Tk()
calc = Calculator(root)

root.mainloop()
