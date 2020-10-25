import math 

def egyptianFraction(nr, dr): 

	print("The Egyptian Fraction " +
		"Representation of {0}/{1} is". 
				format(nr, dr), end="\n") 

	# empty list ef to store denominator 
	l = [] 

	# while loop runs until fraction becomes 0
	while nr != 0: 

		
		x = math.ceil(dr / nr) 
		l.append(x) 
		nr = x * nr - dr 
		dr = dr * x 

	# printing the values 
	for i in range(len(l)): 
		if i != len(l) - 1: 
			print(" 1/{0} +" . 
					format(l[i]), end = " ") 
		else: 
			print(" 1/{0}" . 
					format(l[i]), end = " ") 

# calling the function 
egyptianFraction(6, 14) 
