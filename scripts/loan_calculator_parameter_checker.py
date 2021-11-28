from scripts.interest_parameter_checker import is_valid_num



def loan_calculator_parameter_checker(amount, interest, time, time_interval):
	everything_okay = True
	if not (is_valid_num(amount) and is_valid_num(interest) and is_valid_num(time)):
		everything_okay = False

	if not time_interval in ['Years', 'Months']:
		everything_okay = False


	return everything_okay


