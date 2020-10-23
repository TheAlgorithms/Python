"""
Problem 206 : https://projecteuler.net/problem=206

Find the unique positive integer whose square has the form 1_2_3_4_5_6_7_8_9_0,
where each “_” is a single digit.

Solution: Finding a square number can found by adding consecutive odd numbers 
starting from 1. The minimum number possible for perfect square is 1020304050607080900
in this situation, so started checking digits are in correct places after 
total is above it. 

"""

import math  

def solution():
    """
    >>> solution()
    1389019170
    """


    total = 1
    add = 1
    while True:
        add += 2
        total += add
        if total > 1020304050607080900 and \
            int(str(total)[-1]) == 0 and \
            int(str(total)[-3]) == 9 and \
            int(str(total)[-5]) == 8 and \
            int(str(total)[-7]) == 7 and \
            int(str(total)[-9]) == 6 and \
            int(str(total)[-11]) == 5 and \
            int(str(total)[-13]) == 4 and \
            int(str(total)[-15]) == 3 and \
            int(str(total)[-17]) == 2 and \
            int(str(total)[-19]) == 1:

            break
    return int(math.sqrt(total))
    
if __name__ == "__main__":
    print(f"{solution() = }")
