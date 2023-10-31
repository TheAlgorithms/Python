'''
This program will search every even number less than the inputted number
and then show which numbers passed the test and which didn't.
'''

def isprime(num):
    value = False

    if num == 1:
        # print(num, "is not a prime number")
        pass
    elif num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                value = True
                break
        if value==True:
            return False
        else:
            return True


def istrue(x):
    t = 0
    while t <= x / 2:
        if isprime(t) == 1 and isprime(x - t) == 1:
            return True
        t = t + 1


final_num=int(input("-->"))
test_num=4
A=[]
B=[]
while test_num <= final_num:
    if istrue(test_num)== 1:
        #print(test_num,"follows Goldbach's conjecture")
        A.append(test_num)
    else:
        print(test_num,"does not follow the Goldbach's conjecture")
        B.append(test_num)
    test_num=test_num+2
print(A, "follow the Goldbach's conjecture")
print(B, " does not follow the Goldbach's conjecture")
