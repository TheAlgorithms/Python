#Python Program to convert Kilometers to Miles
#Formula:
#1 kilometer equals 0.62137 miles.
#Miles = kilometer * 0.62137   
#Kilometer = Miles / 0.62137

# conversion factor 
conv = 0.621371
  
kilometers = 1.7
  
# calculate miles 
miles = kilometers * conv 
print('%0.2f kilometers is equal to %0.2f miles' %(kilometers,miles)) 


#Program to convert centimeter into meter and kilometer
#Formula to be used:
#1m = 100cm
#1km = 100000cm

# Python3 program to convert centimeter into meter and kilometer  
cm = 1000;
  
# Converting centimeter into meter and kilometer 
meter = cm / 100.0; 
kilometer = cm / 100000.0; 
  
# Driver Code 
print("Length in meter = " , meter , "m"); 
print("Length in Kilometer = ", kilometer , "km"); 


#Program to convert Centimeter to Feet and Inches
#Formula:
#1. We know that 1 inch is equal to 2.54 centimeter, so 1 centimeter is equal to 0.3937 inches. Therefore, n centimeters are equal to (n * 0.3937)inches.
#2. We also know that 1 foot is equal to 30.48 centimeter, therefore, 1 centimeter is equal to 0.0328 feet. So, n centimeters are equal to (n * 0.0328)feet.

# Python program to convert centimeter to feet and Inches Function to perform conversion 
def Conversion(centi): 
    inch = 0.3937 * centi 
    feet = 0.0328 * centi 
    print ("Inches is:", round(inch, 1)) 
    print ("Feet is:", round(feet, 1)) 
  
# Driver Code 
centi = 100
Conversion(centi) 
