""" Problem Statement (Digit Fifth Power ): 
Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:

1634 = 14 + 64 + 34 + 44
8208 = 84 + 24 + 04 + 84
9474 = 94 + 44 + 74 + 44
As 1 = 14 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.
 
"""
"""
(9^5)=59,049‬
59049*7=4,13,343 (which is only 6 digit number )
So, number greater than 9,99,999 are rejected
and also 59049*3=1,77,147 (which exceeds the criteria of number being 3 digit)
So, n>999
and hence a bound between (1000,1000000)
"""


def digitsum(s):
    c=0
    for j in range(len(s)):
        c+=pow(int(s[j]),5)
    if c==int(s):
        return c
    else:
        return 0

count=0
for i in range(1000,1000000):
    count+=digitsum(str(i))
print(count)

#ans = 443839
