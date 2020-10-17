"""
Project Euler Problem [problem_038]: https://projecteuler.net/problem=38

...[Problem statement: Take the number 192 and multiply it by each of 1, 2, and 3:

                    192 × 1 = 192
                    192 × 2 = 384
                    192 × 3 = 576
By concatenating each product we get the 1 to 9 pandigital, 192384576. We will call 192384576 the concatenated product of 192 and (1,2,3)

The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and 5, giving the pandigital, 918273645, which is the concatenated product of 9 and (1,2,3,4,5).

What is the largest 1 to 9 pandigital 9-digit number that can be formed as the concatenated product of an integer with (1,2, ... , n) where n > 1?] ...
    
"""
def solution():
    # largest pandigital number
    largest = 0 
    # for loop to loop till 4 digits
    for i in range(1,10000):
    	
    	# value for concatenated string
    	multiplication = ''   	
    	integer = 1
    	
    	# if the multiplication < 9 digits
    	while len(multiplication) < 9:
    		
    		# concatenating the product at each stage
    		multiplication += str(i*integer)       
    		integer += 1
    		
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
solution()
