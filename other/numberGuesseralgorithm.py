
# Only works with whole numbers

def guessnumber(maximum,minimum):
    # smallestnumber refers to the smallest possible number given the information, largestnumber refers to the largest possible number.
    smallestnumber = minimum
    biggestnumber = maximum
    while True:
        #This if statement handles the final decision, when biggest and smallest number are only 1 apart
        if (biggestnumber - smallestnumber <= 1 and biggestnumber - smallestnumber > 0) or (smallestnumber - biggestnumber <= 1 and smallestnumber - biggestnumber > 0):
           print("Is your number ", smallestnumber, "?")
           userinput = input("")
           if userinput == "y":
                print("Your number is... ",smallestnumber,"!")
                return smallestnumber
           elif userinput == "n":
                print("Your number is... ",biggestnumber,"!")
                return biggestnumber
        #This statement handles narrowing down the selection by constantly calculating the middle
        elif not ((biggestnumber - smallestnumber <= 1 and biggestnumber - smallestnumber > 0) or (smallestnumber - biggestnumber <= 1 and smallestnumber - biggestnumber > 0)):
            print("Is your number larger than or equal to ",(smallestnumber+biggestnumber)/2,"?")
            userinput = input("")
            if userinput == "n":
                smallestnumber = round((smallestnumber+biggestnumber)/2)
            elif userinput == "y":
                    biggestnumber = round((smallestnumber+biggestnumber)/2)
            else:
                print("Use y or n")
        else:
            print("Use y or n")

