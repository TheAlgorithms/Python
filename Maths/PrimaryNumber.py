import sys
def main():
    print("Calculate primary number from 0 to your number:")
    while True:
        num = eval(input("To what number?"))
        print('resualt:' , pr(num))

def pr(num):
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