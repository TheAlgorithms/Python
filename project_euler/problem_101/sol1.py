import itertools
from fractions import Fraction


DEGREE = 10
def compute():
	ans = Fraction(0, 1)
	for k in range(1, DEGREE + 1):
		for n in itertools.count(k + 1):
			if n == DEGREE + 2:
				raise AssertionError()
			reference = Fraction(generating_function(n), 1)
			term = optimum_polynomial(k, n)
			if term != reference:
				ans += term
				break
	return str(ans.numerator) + ("" if ans.denominator == 1 else "/" + str(ans.denominator))


def optimum_polynomial(k, n):
	# Lagrange interpolation
	sum = Fraction(0, 1)
	for i in range(k + 1):
		product = Fraction(generating_function(i), 1)
		for j in range(1, k + 1):
			if j != i:
				product *= Fraction(n - j, i - j)
		sum += product
	return sum


def generating_function(n):
	return sum((-n)**i for i in range(DEGREE + 1))


if __name__ == "__main__":
	print(compute())
