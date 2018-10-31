import datetime as dt
my_date1 = dt.datetime(2015, 1, 4) #Storing the date 4th Jan, 2015
print(my_date1)
print('The Weekday of that day was: ' + my_date1.strftime('%A'))

my_date2 = dt.datetime.strptime('August-15-2017', '%B-%d-%Y') #Storing the date 15th Aug, 2017
print(my_date2)
print('The Weekday of that day was: ' + my_date2.strftime('%A'))

print('The difference between two days: ' + str(abs(my_date1 - my_date2)))
