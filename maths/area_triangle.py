#S=√(p*(p-a)*(p-b)*(p-c))
#p=(a+b+c)/2
#a,b,c-sidestriangle
#calculatestheareaofatriangleonthreesides.a,b,c-sidestriangle

def treug(a,b,c):
	p=(a+b+c)/2
	S=(p*(p-a)*(p-b)*(p-c))**(1/2)
	return(S)
treug(5,5,5)