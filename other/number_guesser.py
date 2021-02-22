"""
Number Guessing algorithm

This algorithm guesses a number between the maximum and minimum parameters by asking yes/no questions in the most efficient way.
It is a mathematical solution which changes the smallest and largest possible values according to answers until there is only one
possible value. Only works with whole numbers.

For example,

>>> guessnumber(0,10)
Is your number larger than or equal to  5.0 ?
y
Is your number larger than or equal to  7.5 ?
n
Is your number larger than or equal to  6.5 ?
n
Is your number  6 ?
y
6


By Viridescence
"""

# maximum is the largest possible number, minimum is the smallest possible number a guess could be.
def guessnumber(maximum,minimum):
    # smallestnumber refers to the smallest possible number given the information, largestnumber refers to the largest possible number.
    # These are changed to exclude certain ranges as the algorithm learns new information.
    smallestnumber = minimum
    biggestnumber = maximum
    while True:
        #This if statement handles the final decision, when biggest and smallest number are only 1 apart
        if (biggestnumber - smallestnumber <= 1 and biggestnumber - smallestnumber > 0) or (smallestnumber - biggestnumber <= 1 and smallestnumber - biggestnumber > 0):
           print("Is your number ", smallestnumber, "?")
           userinput = input("").strip()
           if userinput == "y":
                return smallestnumber
           elif userinput == "n":
                return biggestnumber
        #This statement handles narrowing down the selection by constantly calculating the middle of possible answers.
        elif not ((biggestnumber - smallestnumber <= 1 and biggestnumber - smallestnumber > 0) or (smallestnumber - biggestnumber <= 1 and smallestnumber - biggestnumber > 0)):
            print("Is your number larger than or equal to ",(smallestnumber+biggestnumber)/2,"?")
            userinput = input("").strip()
            if userinput == "n":
                smallestnumber = round((smallestnumber+biggestnumber)/2)
            elif userinput == "y":
                    biggestnumber = round((smallestnumber+biggestnumber)/2)
            else:
                print("Use y or n")
        else:
            print("Use y or n")
