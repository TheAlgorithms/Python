# https://projecteuler.net/problem=63
"""
The reason i have choosen 25 is because any number which when is raised to the power of 25 gradually increases from
8 digits of 2^25 linearly(at first with a diffrence of 4(that is num_of_digit in 2^25 is 8 and 3^25 id 12) which starts 
halfening) ,hence all the sollution must lie for numbers below 25 only, since any number x^(any_num_greater_than_25) is
greater than x^25. 
"""

count=0
for i in range(1,25):
    for t in range(1,25):
        if len(str(t**i))==i:
            count+=1
print(count)
# 49 -- answer
