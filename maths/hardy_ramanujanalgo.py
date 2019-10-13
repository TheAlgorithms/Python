import math 

def exactPrimeFactorCount(n) : 
	count = 0
	if (n % 2 == 0) : 
		count = count + 1
		while (n % 2 == 0) : 
			n = int(n / 2) 

	i = 3
	
	while (i <= int(math.sqrt(n))) : 
		if (n % i == 0) :	 
			count = count + 1
			while (n % i == 0) : 
				n = int(n / i) 
		i = i + 2

	if (n > 2) : 
		count = count + 1
	return count 

n = 51242183
print ("The number of distinct prime factors is/are {}". 
	format(exactPrimeFactorCount(n), end = "\n")) 
print ("The value of log(log(n)) is {0:.4f}"
			.format(math.log(math.log(n)))) 

