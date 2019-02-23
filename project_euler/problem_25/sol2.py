def fibonacci_genrator():
	a, b = 0,1
	while True:
		a,b = b,a+b
		yield b
answer = 1
gen = fibonacci_genrator()
while len(str(next(gen))) < 1000:
	answer += 1
assert answer+1 == 4782
