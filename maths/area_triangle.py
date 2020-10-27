#S= √ (p * (p - a)*(p - b)*(p - c))
#p=(a+b+c)/2;
#a,b,c - sides triangle
#calculates the area of a triangle on three sides. a,b,c - sides triangle

def treug(a,b,c):
	p=(a+b+c)/2
	S=(p * (p - a)*(p - b)*(p - c))**(1/2)
	return(S)
	

print(treug(5,5,5))
