import itertools


def compute():
	MOD = 10**9
	a = 0
	b = 1
	for i in itertools.count():
		# Loop invariants: a == fib(i) % MOD, b == fib(i+1) % MOD
		if "".join(sorted(str(a))) == "123456789":  # If suffix is pandigital
			f = fibonacci(i)[0]
			if "".join(sorted(str(f)[ : 9])) == "123456789":  # If prefix is pandigital
				return str(i)
		a, b = b, (a + b) % MOD
	return str(ans)


# Returns the tuple (F(n), F(n+1)), computed by the fast doubling method.
def fibonacci(n):
    if n == 0:
        return (0, 1)
    else:
        a, b = fibonacci(n // 2)
        c = a * (b * 2 - a)
        d = a * a + b * b
        if n % 2 == 0:
            return (c, d)
        else:
            return (d, c + d)


if __name__ == "__main__":
	print(compute())
