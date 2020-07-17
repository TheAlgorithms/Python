"""
This is a pure Python implementation of the Arithmetico–Geometric Sequence algorithm
By using it you can get:
- Full Arithmetico-geometric Sequence
- Value of the last term of the series
- Sum of the series
- Infinite sum of the series
- Value of K-th term of the series
https://en.wikipedia.org/wiki/Arithmetico%E2%80%93geometric_sequence
For doctests run following command:
python -m doctest -v arithmetico_geometric_sequence.py
or
python3 -m doctest -v arithmetico_geometric_sequence.py
For manual testing run:
python3 arithmetico_geometric_sequence.py
"""

def full_series(a, d, b, r, n):
	"""
	Using this fuction, you can get the full series
	:params a: Initial Value For Arithmetic Progression
    		d: Difference For Arithmetic Progression
    		b: Initial Value For Geometric Progression
    		r: Common Ratio For Geometric Progression
    		n: Number Of Terms
    :return: Full series in list form
    Examples:
    >>>full_series(2, 3, 4, 0.5, 6)
    ['2.0 x 4.0', '(2.0 + 3.0) x 4.0x0.5^1', '(2.0 + 6.0) x 4.0x0.5^2', '(2.0 + 9.0) x 4.0x0.5^3', '(2.0 + 12.0) x 4.0x0.5^4', '(2.0 + 15.0) x 4.0x0.5^5']
	"""
	series = []
	for i in range(n):
		if i==0:
			series.append(str(a)+" x "+str(b))
		else:
			ap_part = str(a)+" + "+str(i*d)
			gp_part = str(b)+"x"+str(r)+"^"+str(i)
			series.append("("+ap_part+")"+" x "+gp_part)
	return series

def last_term_value(a, d, b, r, n):
	"""
	Using this fuction, you can get the value of the last term of the series
	:params a: Initial Value For Arithmetic Progression
    		d: Difference For Arithmetic Progression
    		b: Initial Value For Geometric Progression
    		r: Common Ratio For Geometric Progression
    		n: Number Of Terms
    :return: Value of the last term of the series
	Examples:
	>>>last_term_value(2, 3, 4, 0.5, 6)
	2.12
	"""
	return (a+(n-1)*d)*(b*pow(r, n-1))

def sum(a, d, b, r, n):
	"""
	Using this fuction, you can get the sum of the series
	:params a: Initial Value For Arithmetic Progression
    		d: Difference For Arithmetic Progression
    		b: Initial Value For Geometric Progression
    		r: Common Ratio For Geometric Progression
    		n: Number Of Terms
    :return: Sum of the series
	Examples:
	>>>sum(2, 3, 4, 0.5, 6)
	37.12
	"""
	s_n = ((a*b)-((a+(n*d))*(b*pow(r, n))))/(1-r) + (d*b*r*(1-pow(r, n)))/pow((1-r), 2)
	return s_n

def inf_sum(a, d, b, r):
	"""
	Using this fuction, you can get the infinite sum of the series
	:params a: Initial Value For Arithmetic Progression
    		d: Difference For Arithmetic Progression
    		b: Initial Value For Geometric Progression
    		r: Common Ratio For Geometric Progression
    :return: Infinite sum of the series
    Examples:
    >>>inf_sum(2, 3, 4, 0.5)
    40.00
    """
	s = (a*b)/(1-r) + (d*b*r)/pow((1-r), 2)
	return s

def kth_term_value(a, d, b, r, k):
	"""
	Using this fuction, you can get the value of K-th term of the series
	:params a: Initial Value For Arithmetic Progression
    		d: Difference For Arithmetic Progression
    		b: Initial Value For Geometric Progression
    		r: Common Ratio For Geometric Progression
    		k: Value Of K In K-th Term
    :return: Value of K-th term of the series
    Examples:
    >>>kth_term_value(2, 3, 4, 0.5, 3)
    8.00
    """
	return (a+(k-1)*d)*(b*pow(r, k-1)) 

if __name__=="__main__":
	a = float(input("\nEnter Initial Value For A.P. : "))
	d = float(input("Enter Difference For A.P. : "))
	b = float(input("Enter Initial Value For G.P. : "))
	r = float(input("Enter Common Ratio For G.P. : "))
	n = int(input("Enter Number Of Terms : "))
	k = int(input("Value Of Which Term You Want : "))

	print("\nFull Series : \n{}".format(full_series(a, d, b, r, n)))
	print("\nValue Of Last Term : {:.2f}".format(last_term_value(a, d, b, r, n)))
	print("\nSum Of Your A.G.S. : {:.2f}".format(sum(a, d, b, r, n)))
	print("\nInfinite Series Sum : {:.2f}".format(inf_sum(a, d, b, r)))
	print("\nValue Of {}-th Term : {:.2f}".format(k, kth_term_value(a, d, b, r, k)))
