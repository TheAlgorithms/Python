#guessing the number
def example():
    try:
        pNumber = int(input("enter positive number : "))
        if(pNumber < 0):
            raise ValueError("Thats not a positive number!")
    except ValueError as me:
        print(me)
    else:
        print()
        print(pNumber)


class error(Exception):
    pass


class valuetoosmallError(error):
    pass


class valuetoolargeError(error):
    pass


number = 10
while(True):
    try:
        n = int(input("Guess the number"+"\n"))
        if(n < number):
            raise valuetoosmallError
        elif(n > number):
            raise valuetoolargeError
        break
    except valuetoosmallError:
        print("value is too small..try one more time")
    except valuetoolargeError:
        print("value too large..have a try again")
print("Congrats bud!U nailed it")
