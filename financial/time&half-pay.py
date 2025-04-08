"""
Calculate time and a half pay

"""
def pay(hours_worked, pay_rate, hours = 40):
	"""
	hours_worked = The total hours worked
	pay_rate = Ammount of money per hour
	hours = Number of hours that must be worked before you recieve time and a half
	"""
	normal_pay = hours_worked * pay_rate
	over_time = hours_worked - hours
	# Another way
	# over_time_pay = ((over_time * ((over_time + (over_time ** 2) ** 0.5) / (2 * over_time))) / 2) * pay_rate
	over_time_pay = (max(0, over_time) / 2) * pay_rate
	total_pay = normal_pay + over_time_pay
	return total_pay


if __name__ == "__main__":
	# Test
	print(pay(41, 1))
	print(pay(65, 19))
	print(pay(10, 1))
