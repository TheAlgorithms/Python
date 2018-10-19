'''
Problem:
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 x 99.
Find the largest palindrome made from the product of two 3-digit numbers which is less than N.
'''
from __future__ import print_function
limit = int(raw_input("limit? "))

# fetchs the next number
for number in range(limit-1,10000,-1):

    # converts number into string.
    strNumber = str(number)

    # checks whether 'strNumber' is a palindrome.
    if(strNumber == strNumber[::-1]):

        divisor = 999

        # if 'number' is a product of two 3-digit numbers
        # then number is the answer otherwise fetch next number.
        while(divisor != 99): 
            
            if((number % divisor == 0) and (len(str(number / divisor)) == 3)):

                print(number)
                exit(0)

            divisor -=1