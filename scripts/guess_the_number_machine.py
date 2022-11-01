"""
get the random number guessed by the computer by passing the lower,higher
and the number to guess

this solution works on divide and getting the half of number of previous and current
    this depends on the number is low or high 

if the number is more than last lower and less than to the number to guess then the number 
is assigned to it, and same but opposite for higher number

suppose lower is 0, higher is 1000 and the number to guess is 355
then:
    num = int((lower+higher)/2)
    for above statement the function already declared as the d(a,b)

        [1]
    d(0,1000)  : 500
    answer(500) : high
        Now this value is passed to the answer function and that returns the passed number is lower than
        the guess number or higher than the guess number and also for equality
    
        [2]
    d(0,500) : 250
    answer(250) : low

        [3]
    d(250,500) : 375
    answer(375) : high

        [4]
    d(375,250) : 312
    answer(312) : low

        [5]
    d(312,375) : 343
    answer(343) : low

        [6]
    d(343,375) : 359
    answer(359) : high

        [7]
    d(343,359) : 351
    answer(351) : low

        [8]
    d(351,359) : 355
    answer(355) : same

The number is found : 355
"""

import sys
import time

def d(a,b):
    return int((a+b)/2)

lower = int(input("Enter lower number : "))
higher = int(input("Enter higher number : "))

to_guess = int(input("Enter number to guess : "))

if to_guess > higher or to_guess < lower:
    print("Please enter the number in range of lower and higher")
    sys.exit(1)

start_time = time.time()

def answer(number):
    if number > to_guess:
        return "high"
    elif number < to_guess:
        return "low"
    else:
        return "same"

print("started...")

last_lowest = lower
last_highest = higher

last_numbers = []

while True:
    number = d(last_lowest, last_highest)
    last_numbers.append(number)

    if answer(number) == "low":
        print("low",end="\r")
        last_lowest = number
    elif answer(number) == "high":
        print("high",end="\r")
        last_highest = number
    else:
        print("Got that"," "*10)
        break
    
end_time = time.time()

print(last_numbers)
print("successfully gueesed the number :",last_numbers[-1])
print(f"time elapsed : {end_time-start_time}")
