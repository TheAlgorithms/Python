print("""
*********************
This program finds the number is a prime number or not.

If you want to exit press 'q'.

*********************""")

def prime_number(number):
    for i in range(2,number):
        if (number % i == 0):
            return False

    return True


while True:
    number =(input("Please enter number: "))

    if (number == "q"):
        print("Program is terminating..")
        break
    number = int(number)

    if (number == 1):
        print("This is not a prime number.")
    elif (number == 2):
        print("This is a prime number.")
    else:
        if (prime_number(number)):
            print("{} is a prime number".format(number))
        else:
            print("{} is not a prime number".format(number))
