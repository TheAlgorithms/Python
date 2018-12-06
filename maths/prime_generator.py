from PrimeCheck import primeCheck

def prime_generator():
    num = 2
    while True:
        if primeCheck(num):
            yield num
        num+=1
