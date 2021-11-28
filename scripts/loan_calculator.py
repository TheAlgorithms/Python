# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 17:52:17 2020

@author: Piyush
"""

def periodic_payment_helper(amount, interestPA, time_period, periodic_payment):
    '''
    Takes in loan amount, interest rate per annum, time period and fixed
    monthly periodic payment. Returns the final balance after adding interest
    to every month and deducting periodic_payment amount. If the balance < 0
    then this means that the periodic_payment amount is too high. If balance >
    0 then this means that the periodic_payment amount is too low. 
    '''
    
    balance = amount
    total_intervals = int(12 * time_period)
    
    
    for i in range(total_intervals + 1):
        if i == 0:
            continue
        
        interest = balance * (interestPA / 12)
        balance = balance + interest
        balance = balance - periodic_payment
        
    return balance



def calculate_periodic_payment(amount, interestPA, time_period, time_interval):
    if time_interval == 'Months':
        time_period = (time_period) // 12



    low = 0
    high = amount
    
    average = (low + high) / 2
    balance = periodic_payment_helper(amount, interestPA, time_period, average)
    count = 0
    while balance > 1 or balance < -1:
        count += 1
        if balance > 0:
            low = average
            average = (low + high) / 2
            
        else:
            high = average
            average = (low + high) / 2
            
        balance = periodic_payment_helper(amount, interestPA, time_period, average)
            
        
        if count > 5000:
            print('Count Exceeded by 5000')
            return average
        
        
        
    return round(average, 2)
        
        
        
    
    