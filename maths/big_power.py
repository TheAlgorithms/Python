import math

def fpow(a,b):
  '''
  >>> fpow(16,24)
  79228162514264337593543950336
  '''
	res=1
	while (b>0):
		if b&1:
			res=res*a 
		a=a*a
		b>>=1
	return res

if __name__ == "__main__":
    import doctest

    doctest.testmod()
