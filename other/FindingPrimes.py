'''
-The sieve of Eratosthenes is an algorithm used to find prime numbers, less than or equal to a given value.
-Illustration: https://upload.wikimedia.org/wikipedia/commons/b/b9/Sieve_of_Eratosthenes_animation.gif
'''
from math import sqrt
def SOE(n):
    check = round(sqrt(n)) #Need not check for multiples past the square root of n
    
    sieve = [False if i <2 else True for i in range(n+1)] #Set every index to False except for index 0 and 1
    
    for i in range(2, check):
        if(sieve[i] == True):                  #If i is a prime  
            for j in range(i+i, n+1, i):       #Step through the list in increments of i(the multiples of the prime)   
                sieve[j] = False               #Sets every multiple of i to False 
    
    for i in range(n+1):
        if(sieve[i] == True):
            print(i, end=" ")

n = int(input("Enter a positive number\n"))
SOE(n)