'''
Implementation of m^n where m and n are big numbers
'''

def largePower(a: int, b: int) -> int:
  '''
  calculate large powers
  >>> largePower(16,9)
  68719476736
  '''
	res = 1
	while (b > 0):
		if (b & 1):
			res = res * a 
		a = a * a
		b >>= 1
	return res

if __name__ == "__main__":
    print(largePower(16, 24))
