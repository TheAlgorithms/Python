#from Python.Math import prime_generator
import math 
from itertools import takewhile 

def primeCheck(number):
    if number % 2 == 0 and number > 2:
        return False
    return all(number % i for i in range(3, int(math.sqrt(number)) + 1, 2))
    
def prime_generator():
    num = 2
    while True:
        if primeCheck(num):
            yield num
        num+=1
        
def main():
    n = int(input('Enter The upper limit of prime numbers: '))  
    print(sum(takewhile(lambda x: x < n,prime_generator())))
    
if __name__ == '__main__':
    main() 
