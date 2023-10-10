"""
Author: Lakshmi Shree A
Topic: Interpolate using Newton’s Forward interpolation method.
Use Newtons forward interpolation to obtain the interpolating polynomial and hence
calculate y(2) for the following: 
x: 1 3 5 7 9
y: 6 10 62 210 50
"""


from sympy import simplify, symbols, lambdify
import numpy as np
import pprint

n = int( input ('Enter number of data points : ') )
210
x = np . zeros (( n ) )
y = np . zeros (( n , n ) )

# Reading data points
print ('Enter data for x and y: ')
for i in range ( n ):
    x[i] = float ( input ( 'x['+str( i )+']= ') )
    y[i][0] = float ( input ( 'y['+str( i )+']= ') )

# Generating forward difference table
for i in range (1 , n ):
    for j in range (0 , n-i ):
        y[j][i] = y[j+1][i-1] - y[j][i-1]
print ('\ nFORWARD DIFFERENCE TABLE \n') 
for i in range (0 , n ):
    print ('%0.2f ' %( x[i]) , end='')
    for j in range (0 , n-i ):
        print ('\t\t%0.2f ' %( y[i][j]) , end='')
    print ()

# obtaining the polynomial
t= symbols ('t')
f=[] # f is a list type data
p=( t-x[0])/( x[1]-x[0])
f . append ( p )
for i in range (1 , n-1 ):
    f . append ( f[i-1]*( p-i )/( i+1 ) )
    poly =y[0][0]
for i in range ( n-1 ):
    poly = poly +y[0][i+1]*f[i]

simp_poly = simplify ( poly )
print ('\ nTHE INTERPOLATING POLYNOMIAL IS\n') 
pprint ( simp_poly )

# if you want to interpolate at some point the next session will help
inter = input ('Do you want to interpolate at a point (y/n)? ') # y
if inter =='y':
    a= float ( input ('enter the point ') ) #2
    interpol = lambdify (t , simp_poly )
    result = interpol ( a )
    print ('\ nThe value of the function at ' ,a ,'is\n', result ) 