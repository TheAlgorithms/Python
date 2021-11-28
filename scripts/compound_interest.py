# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 23:20:14 2020

@author: Piyush
"""


def compound_interest(amount, interest, num_times_int, time_period, time_period_in):
    amount = float(amount)
    interest = float(interest) / 100
    time_period = float(time_period)
    
    
    time_convert_dict = {'Days' : 365, 'Months' : 12, 'Years' : 1}
    interest_convert_dict = {'Yearly' : 1, 
                             'Quarterly' : 4,
                             'Monthly' : 12,
                             'Continuous' : 12}
    
    n = interest_convert_dict[num_times_int]
    
    
    time_period_years = time_period / time_convert_dict[time_period_in]
    
    print(n)
    print('Effective n is %i' % (n * time_period_years))
    total_investment = amount * (1 + (interest / n)) ** (n * time_period_years)
    if total_investment >= 1000000000:
        total_investment = int(total_investment)
    return total_investment
    
    





























