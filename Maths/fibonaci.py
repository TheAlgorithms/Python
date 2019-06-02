def calculating_fibonacci(number):
	if number in [0,1]:
		return 1
	else: 
		return calculating_fibonacci(number-1)+ calculating_fibonacci(n-2)


def find_first_n_fibonacci(number):
	for i in range(0,number):
		print(calculating_fibonacci(i))


