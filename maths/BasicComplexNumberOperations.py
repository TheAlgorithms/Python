import cmath
a = complex(2, 3)
b = complex(1, 2)
print "Addition is :", a+b
print "Dot product is :", (a.real*b.real)+(a.imag+b.imag)
print "Absolute value of a is : ", abs(a)
print "Exponential value of a is: ",(cmath.exp(a))