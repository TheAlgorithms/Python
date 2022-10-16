hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))
mins += hour * 60 + dura # find a total of all minutes

hour = (mins//60) % 24 # find a number of hours hidden in minutes and update the hour
mins = round(float(((mins/60) % 1) * 60)) # correct minutes to fall in the (0..59) range
# correct hours to fall in the (0..23) range
print(hour, ":", mins, sep='')
