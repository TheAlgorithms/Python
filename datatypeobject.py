import datetime as dt
new_date = dt.date(1998, 9, 5) #Store date 5th septemberm, 1998

print("The Date is: " + str(new_date))
print("Ordinal value of given date: " + str(new_date.toordinal()))
print("The weekday of the given date: " + str(new_date.weekday())) #Monday is 0

my_date = dt.date.fromordinal(732698) #Create a date from the Ordinal value.
print("The Date from ordinal is: " + str(my_date))

td = my_date - new_date #Create a timedelta object
print('td Type: ' + str(type(td)) + '\nDifference: ' + str(td))
