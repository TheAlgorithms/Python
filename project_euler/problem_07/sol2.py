# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13. What is the Nth prime number?
def isprime(number):
	for i in range(2,int(number**0.5)+1):
		if number%i==0:
			return False
	return True
n = int(input('Enter The N\'th Prime Number You Want To Get: ')) # Ask For The N'th Prime Number Wanted
primes = []
num = 2
while len(primes) < n:
	if isprime(num):
		primes.append(num)
		num += 1
	else:
		num += 1
print(primes[len(primes) - 1])
