# python program to find modular inverse of a under modulo m.
from math import pow

def MMI(a, p, m):
	"""
	According to fermat's little theorem, if m is prime. than,
	(a^p)%m = a%m

	thus we can calculate,
	(a^p-2)%m = (a^-1)%m 
	which is modular multiplicative inverse of a mod m.
	"""
	if not p :
		return 1
	tmp =  MMI(a, p//2, m) % m;
	tmp = (tmp*tmp) % m
	return tmp if p%2==0 else (tmp*a % m)

# Driver Program
if __name__ == '__main__':
	a, m = map(int, input().split())
	print(MMI(a, m-2, m))
