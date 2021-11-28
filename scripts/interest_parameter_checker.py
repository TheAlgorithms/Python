def is_valid_num(string):
	if string.isdigit():
		return True


	elif string.replace('.', '', 1).isdigit():
		return True

	else:
		return False




def interest_parameter_checker(amount, interest, num_times_int, time_period, time_period_in):
	valid_values = True
	select_box1 = ['Yearly', 'Quarterly', 'Monthly', 'Continuous']
	select_box2 = ['Years', 'Months', 'Days']

	if not (is_valid_num(amount) and is_valid_num(interest) and is_valid_num(time_period)):
		valid_values = False

	

	if not (num_times_int in select_box1 and time_period_in in select_box2):
		valid_values = False


	return valid_values







        

        