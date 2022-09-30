#Python Algorithm to check of two numbers are Twin Prime
'''
A twin prime is a prime number that is either 2 less or 
2 more than another prime number—for example, either member
of the twin prime pair (41, 43). In other words, a twin prime
is a prime that has a prime gap of two. Sometimes the term
twin prime is used for a pair of twin primes; an alternative
name for this is prime twin or prime pair.
'''
import math
import unittest

#Simple Function to check if a number is prime or not
def isPrime(n: int) -> bool:
	
	if n <= 1:
		return False
	if n <= 3:
		return True
	
	if n%2 == 0 or n%3 == 0:
		return False
	
	for i in range(5, int(math.sqrt(n)+1), 6):
		if n%i == 0 or n%(i + 2) == 0:
			return False
	
	return True

#Function to check if two numbers are twinPrime or Not
def twinPrime(n1: int , n2: int) -> bool:
    '''
    >>> twinPrime(0,2)
    False
    >>> twinPrime(1,3)
    False
    >>> twinPrime(3,5)
    True
    >>> twinPrime(5,7)
    True
    >>> twinPrime(2,7)
    False
    >>> twinPrime(8,7)
    False
    >>> twinPrime(41,43)
    True
    >>> twinPrime(29,31)
    True
    >>> twinPrime(6,8)
    False
    '''
    assert isinstance(n1, int) and isinstance(n2, int) and (n1 >= 0), "both 'numbers' must been an int and positive"

    return (isPrime(n1) and isPrime(n2) and abs(n1 - n2) == 2)


class Test(unittest.TestCase):
    def test_twin_primes(self):
        self.assertTrue(twinPrime(3,5))
        self.assertTrue(twinPrime(5,7))
        self.assertTrue(twinPrime(11,13))
        self.assertTrue(twinPrime(17,19))
        self.assertTrue(twinPrime(29,31))
        self.assertTrue(twinPrime(41,43))
        self.assertTrue(twinPrime(59,61))

    def test_not_twin_primes(self):
        with self.assertRaises(AssertionError):
            twinPrime(-19,-17)
        self.assertFalse(
            twinPrime(0,2),
            "Zero doesn't have any positive factors, primes must have exactly two.",
        )
        self.assertFalse(
            twinPrime(1,3),
            "One only has 1 positive factor, primes must have exactly two.",
        )
        self.assertFalse(twinPrime(2,4))
        self.assertFalse(twinPrime(6,8))
        self.assertFalse(twinPrime(4,8))
        self.assertFalse(twinPrime(12,30))
        self.assertFalse(twinPrime(16,24))

#driver code
if __name__ == "__main__":
    unittest.main()