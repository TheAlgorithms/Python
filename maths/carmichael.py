"""
In number theory, a Carmichael number is a composite number n which satisfies the modular 
arithmetic congruence relation:

									n | b^(n-1) - 1

for all integers b which are relatively prime to n.[1] They are named for Robert Carmichael.
The Carmichael numbers are the subset K1 of the Knödel numbers.

Equivalently, a Carmichael number is a composite number n for which

									n | b^n - b

for all integers b.

Examples of Carmichael numbers: 561, 1105, 1729, 2465, 2821, 6601, 8911 ....

https://en.wikipedia.org/wiki/Carmichael_number
"""
PASSING = (561, 1105, 1729, 2465, 2821, 6601, 8911)
FAILING: tuple = ("A", [], {}, None)

import numpy as np

def check_carmichael(number: int) -> bool:
    """
    Return True if number is a Carmichael number or False if it is not.
    >>> all(check_carmichael(n) for n in PASSING)
    True
    >>> any(check_carmichael(n) for n in FAILING)
    False
    """
	n = number
	count1=0
	count2=0
	count3=0

	for i in range(3,n):
		if n%(i*i)==0:
			count3 = count3 + 1
		else:
			if i < 2:
				flag = 1
			elif i == 2:
				flag = 0
			else:
				j = 2
				while True:
					if i % j == 0:
						flag = 1
					if j * j > i:
						flag = 0
					j = j + 1
			if n%i==0 and flag==0:
				if (n-1)%(i-1)==0:
					count2 = count2 + 1
				else:
					count1 = count1 + 1

	if count1==0 and count2>2 and count3==0:
		return True
	else:
		return False

if __name__ == "__main__":
   num = int(input("Enter the number: "))
   if check_carmichael(num):
      print(f"{num} is a Carmichael number")
   else:
      print(f"{num} is not a Carmichael number")
