import math

print('The Floor and Ceiling value of 23.56 are: ' + str(math.ceil(23.56)) + ', ' + str(math.floor(23.56)))
x = 10
y = -15
print('The value of x after copying the sign from y is: ' + str(math.copysign(x, y)))
print('Absolute value of -96 and 56 are: ' + str(math.fabs(-96)) + ', ' + str(math.fabs(56)))
my_list = [12, 4.25, 89, 3.02, -65.23, -7.2, 6.3]
print('Sum of the elements of the list: ' + str(math.fsum(my_list)))

print('The GCD of 24 and 56 : ' + str(math.gcd(24, 56)))

x = float('nan')
if math.isnan(x):
    print('It is not a number')
    
x = float('inf')
y = 45
if math.isinf(x):
    print('It is Infinity')
    
print(math.isfinite(x)) #x is not a finite number
print(math.isfinite(y)) #y is a finite number
