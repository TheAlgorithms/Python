from django.shortcuts import render
import os
from django.http import HttpResponse
from scripts.interest_parameter_checker import *
from scripts.compound_interest import compound_interest
from scripts.loan_calculator import calculate_periodic_payment
from scripts.loan_calculator_parameter_checker import loan_calculator_parameter_checker
# Create your views here.




def index(request):
	#return HttpResponse('welcome to home page')
	return render(request, 'calculator_app/index.html')



def interest_calc(request):


	return render(request, 'calculator_app/interest.html')





def results_interest(request):
	error_text = False


	try:
		amount = request.POST['amount']
		interest_rate = request.POST['interest_rate']
		num_times_interest = request.POST['num_times_interest']
		time_period = request.POST['time_period']
		time_periods = request.POST['time_periods']



	except:
		error_text = 'Sorry, no input received. '
		
		return render(request, 'calculator_app/results_interest.html', {
			"error_text" : error_text, "dict" : request.POST, 

			})


	is_valid = interest_parameter_checker(amount, interest_rate, num_times_interest, time_period, time_periods)

	if is_valid:
		compound_interest_ = compound_interest(amount, interest_rate, num_times_interest, time_period, time_periods)

	else:
		compound_interest_ = None

	context_dict = {
		"amount" : amount, 
		"interest_rate" : interest_rate, 	
		"num_times_interest" : num_times_interest, 
		"time_period" : time_period, 
		"time_periods" : time_periods,
		"is_valid" : is_valid, 
		"compound_interest" : compound_interest_


		


	}



	return render(request, 'calculator_app/results_interest.html', context_dict)

	


def loan_calculator(request):
	context = {}
	try:
		amount = request.POST["loan_amt"]
		interest = request.POST["interest"]
		time_period = request.POST["time_period"]
		time_interval = request.POST["time_interval"]

	except:
		data_entered = False

	else:
		data_entered = True

	if data_entered:
		context['data_entered'] = data_entered
		context['amount'] = amount
		context['interest'] = interest
		context['time_period'] = time_period
		context['time_interval'] = time_interval
		#context = {'data_entered' : data_entered, 'amount': amount, 'interest' : interest,
		 #'time_period' : time_period, 'time_interval' : time_interval}

	elif not data_entered:
		context['data_entered'] = data_entered
		context['return'] = True
		return render(request, 'calculator_app/loan.html', {'data_entered' : data_entered})


	if loan_calculator_parameter_checker(amount, interest, time_period, time_interval):
		valid_data = True
		amount = float(amount)
		interest = float(interest) / 100
		time_period = float(time_period)

	else:
		valid_data = False
		valid_data_error_message = HttpResponse('The inputs that you entered are of invalid format!<br>\
		Make sure you\'re typing numbers in the above fields. Try again<br>')
		context['valid_data_error_message'] = valid_data_error_message

	#To check in template if data is valid or not
	context['valid_data'] = valid_data


	if valid_data:
		monthly_amount = calculate_periodic_payment(amount, interest, time_period, time_interval)
		context['monthly_amount'] = monthly_amount

	elif not valid_data:
		invalid_data_error_text = 'Sorry, the inputs that you entered were not valid. Please try again. '
		context['invalid_data_error_text'] = invalid_data_error_text


	return render(request, 'calculator_app/loan.html', context)





