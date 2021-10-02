n = int(input("Enter the number to check: "))
j = n
rev = 0
while (j>0):
    digit = j%10
    rev = rev*10 + digit
    j = j//10
if(n == rev):
    print("The number is pallindrome")
else:
    print("Not a pallindrome")


