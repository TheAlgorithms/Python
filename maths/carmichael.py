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


import numpy as np

def check_prime(n: int) -> int:

	if n < 2:
		return 1
	elif n == 2:
		return 0
	else:
		i = 2
		while True:
			if n % i == 0:
				return 1
			if i * i > n:
				return 0
			i = i + 1

def check_carmichael(n: int) -> int:

	count1=0
	count2=0
	count3=0

	for i in range(3,n):
		if n%(i*i)==0:
			count3 = count3 + 1
		else:
			if n%i==0 and check_prime(i)==0:
				if (n-1)%(i-1)==0:
					count2 = count2 + 1
				else:
					count1 = count1 + 1

	if count1==0 and count2>2 and count3==0:
		return 0
	else:
		return 1

def main():
   num = int(input("Enter the number: "))
   if check_carmichael(num) == 0:
      print(f"{num} is a Carmichael number")
   else:
      print(f"{num} is not a Carmichael number")

if __name__ == "__main__":
    import doctest

    doctest.testmod()
    main()
