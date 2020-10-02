'''
Addition of N numbers 
'''
def add_numbers(*numbers):
	numbers=[*numbers]
	try:
		total=str(sum(numbers))
		print('Sum of Numbers is '+ str(total))

	except:
		print("Addition invalid")

add_numbers(1,2,34,2)		# output is 39
add_numbers(8,5,52,31,12) # output is 108
add_numbers(1,2,'hello') # output is Addition invalid

