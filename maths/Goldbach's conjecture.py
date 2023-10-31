'''
This program will search every even number less than the inputted number and then show which numbers passed the test and which didn't.
'''

def isprime(num):
    value = False

    if num == 1:
        #print(num, "is not a prime number")
        pass
    elif num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                value = True
                break
        if value:
            return False
        else:
            return True
def istrue(x):
    t=0
    while t<= x/2:
        if isprime(t) == 1 and isprime(x-t) == 1:
            return True
        t=t+1

final_num=int(input("-->"))
x=4
A=[]
B=[]
while x <= final_num:
    if istrue(x)== 1:
        #print(x,"follows Goldbach's conjecture")
        A.append(x)
    else:
        print(x,"does not follow the Goldbach's conjecture")
        B.append(x)
    x=x+2
print(A, "follow the Goldbach's conjecture")
print(B, " does not follow the Goldbach's conjecture")
