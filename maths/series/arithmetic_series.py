# Python 3 Program to 
# print an arithmetic 
# progression series 
def printAP(a,d,n): 

	# Printing AP by simply adding d 
	# to previous term. 
	curr_term 
curr_term=a 

	for i in range(1,n+1): 
print(curr_term, end=' ') 
		curr_term =curr_term + d 
		

# Driver code 
a = 2 # starting number 
d = 1 # Common difference 
n = 5 # N th term to be find 

printAP(a, d, n) 
