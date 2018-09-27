import sys
def main():
    print("Calculate primary number from 0 to your number:")
    while True:
        num = eval(input("To what number?"))
        print('resualt:' , pr(num))

def pr(num):
    #we know 2 is a primary number then next number if undivisibie with 2, it is primary
    #Any number that not divisible by numbers smaller than itself is primary
    p = [2]
    i = num
    for i in range(3,i+1,2):
        isPrime=True
        for x in p:
            if i % x == 0:
                isPrime = False
                break
        if isPrime:
            p.append(i)
    return p
    
main()
