# WAP to reverse a number

n=int(input("enter the value of n: "))
rev=0
print("Before:",n)
while (n>0):
    a=n%10
    rev=rev*10+a
    n=n//10
print("After reverse:",rev)

