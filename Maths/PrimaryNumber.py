import sys
def main():
    print("Calculate primary number from 0 to your number:")
    while True:
        number = eval(input("To what number?"))
        print('resualt:' , primary(number))
def primary(num):
    #we know 2 is a prime number then next number if undivisibie with 2, it is primary
    #Any number that not divisible by prime numbers smaller than itself is primary
    prime_numbers = [2]
    for i in range(3,number+1,2):
        isPrime=True
        for x in prime_numbers:
            if i % x == 0:
                isPrime = False
                break
        if isPrime:
            prime_numbers.append(i)
    return prime_numbers 
main()
