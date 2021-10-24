def simple_interest(principle, daily_interest_rate, number_of_days_between_payment):
    result = principle * daily_interest_rate * number_of_days_between_payment
    return result

def compound_interest(principle, nominal_annual_interest_rate_percentage , number_of_compounding_periods):
    result = principle * ((1 + nominal_annual_interest_rate_percentage) ** number_of_compounding_periods - 1)
    return result

