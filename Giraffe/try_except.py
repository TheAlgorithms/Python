
try:
    ans = 10/0
    number = int(input("Enter a number: "))
    print("Number is",number)
except ZeroDivisionError as err:
    print(err)
except ValueError:
    print("Invalid Input")