"""
problem_038: https://projecteuler.net/problem=38
Problem statement: What is the largest 1 to 9 pandigital 9-digit number that can be formed as the concatenated product of an integer with (1,2, ... , n) where n > 1
"""
def solution():
    # largest pandigital number
    largest = 0
    # for loop to loop till 4 digits
    for i in range(1,10000):
    	# value for concatenated string
    	multiplication = ''
    	int_eger = 1
    	# if the multiplication < 9 digits
    	while len(multiplication) < 9:
    		# concatenating the product at each stage
    		multiplication += str(i*int_eger)
    		int_eger += 1
    	# check for digits less than 9
    	# check for all 1-9 numbers
    	# check if '0' not in concatenated string
    	if ((len(multiplication) == 9) and (len(set(multiplication)) == 9)
    		and ('0' not in multiplication)):
    		# check if multiplication is greater than largest
    		if int(multiplication) > largest:
    			largest = int(multiplication)
    # return the largest
    return(largest)
if __name__=="__main__":
    print(solution())

