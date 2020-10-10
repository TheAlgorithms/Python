"""
Problem 19: Counting Sundays
You are given the following information, but you may prefer to do some research
for yourself.
1 Jan 1900 was a Monday.
Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.
A leap year occurs on any year evenly divisible by 4, but not on a century
unless it is divisible by 400.
How many Sundays fell on the first of the month during the twentieth century
(1 Jan 1901 to 31 Dec 2000)?
"""


""""
Solution:
Without using python's datetime package we can make solve it by ourselves using  Zeller's congruence.
This is the algorithm to calculate the day of the week of Gregorian Calendar-

h = q + floor((13*(month[m]+1)/5)) + K + floor(K/4) + floor(J/4) - 2*J) % 7
​
where,
    h = day of the week (0 = Saturday, 1 = Sunday, 2 = Monday, ..., 6 = Friday).
    q is the day of the month.
    m is the month (3 = March, 4 = April, 5 = May, ..., 14 = February).
    K the year of the century (year % 100).
    J is the zero-based century (actually year // 100).
"""     
import math
def day_of_the_week(y, m, q):
    J = y//100
    K = y%100
    month = [13, 14, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]  # month -> (3 = March, 4 = April, 5 = May, ..., 14 = February)
    # Zeller's congruence
    return (q + math.floor((13*(month[m]+1)/5)) + K + math.floor(K/4) + math.floor(J/4) - 2*J) % 7


""""
Method to count all the sundays
"""
def total_sundays():
    sundays = 0
    for i in range(1901, 2001, 1):
        for j in range(12):
            if day_of_the_week(i,j,1)== 0:
                sundays += 1             
    return sundays

'''
Expected output=171
'''
print(total_sundays()) 
