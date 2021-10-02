x = input("Enter the number to find with whats it divisible in 2-10: ")
flag = 0
if int(x) % 2 == 0:
    print("The number is divisible by :",2)
    flag = 1
if x % 3 == 0:
    print("The number is divisible by :",3)
    flag = 1
if x % 4 == 0:
    flag = 1
    print("The number is divisible by :",4)
if x % 5 == 0:
    flag = 1
    print("The number is divisible by :",5)
if x % 6 == 0:
    flag = 1
    print("The number is divisible by :",6)
if x % 7 == 0:
    flag = 1
    print("The number is divisible by :",7)
if x % 8 == 0:
    flag = 1
    print("The number is divisible by :",8)
if x % 9 == 0:
    flag = 1
    print("The number is divisible by :",9)
if x % 10 == 0:
    flag = 1
    print("The number is divisible by :",10)

if flag == 0:
    print("Divisible by none in the range 2 - 10\n")
