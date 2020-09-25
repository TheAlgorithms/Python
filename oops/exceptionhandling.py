#Errors can also occur at runtime and these are called exceptions
#Code enters the else block only if the try block doesnt raises an exception
#LEARN how to raise USER DEFINED EXCEPTIONS.
#They occur, for example, when a file we try to open does not exist(FileNotFoundError),
# dividing a number by zero(ZeroDivisionError), module we try to import is not found(ImportError)
#The try statement can have optional "final" statement
#This final clause is executed no matter what, and is generally used to release external resources like closing a file etc.
import sys
a = [1, 2, 3, 4]
try:
    print("{} is the first element".format(a[0]))
    print("{} is the last element".format(a[len(a)]))
except IndexError:
    print("Index out of bounds error")


try:
    a = 3
    if(a < 4):
        b = a/(a-3)
    print("value of b is {}".format(b))
except(NameError, ZeroDivisionError):
    print("Exception Occured and Handled")


def abfun(a, b):
    try:
        c = int((a+b)/(a-b))
    except ZeroDivisionError:
        print("Division of a/b results in zero")
    else:
        print("value of c {}".format(c))
    finally:
        print("Done")


abfun(2, 3)
abfun(2, 2)


randomList = ['a', 0, 2]

for entry in randomList:
    try:
        print("The entry is", entry)
        r = 1/int(entry)
        break
    except:
        print("Oops!", sys.exc_info()[1], "occured.")
        print("Next entry.")
        print()
print("The reciprocal of", entry, "is", r)
