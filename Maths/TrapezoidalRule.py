'''
Numerical integration or quadrature for a smooth function f with known values at x_i

This method is the classical approch of suming 'Equally Spaced Abscissas' 

method 1: 
"extended trapezoidal rule"

'''

def method_1(boundary, steps):
# "extended trapezoidal rule"
# int(f) = dx/2 * (f1 + 2f2 + ... + fn)
	h = (boundary[1] - boundary[0]) / steps
	a = boundary[0]
	b = boundary[1]
	x_i = makePoints(a,b,h)
	y = 0.0	
	y += (h/2.0)*f(a)
	for i in x_i:
		#print(i)	
		y += h*f(i)
	y += (h/2.0)*f(b)	
	return y	

def makePoints(a,b,h):
	x = a + h	
	while x < (b-h):
		yield x
		x = x + h
		
def f(x):
	y = (x-0)*(x-0)
	return y

def main():
	a = 0.0 #Lower bound of integration
	b = 1.0	#Upper bound of integration
	steps = 10.0		#define number of steps or resolution	
	boundary = [a, b]	#define boundary of integration
	y = method_1(boundary, steps)
	print 'y = {0}'.format(y)

if __name__ == '__main__':
	main()
