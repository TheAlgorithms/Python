# -*- coding: utf-8 -*-
"""
Created on Fri Oct 11 07:33:27 2019

@author: beast
"""

# Python Program - Convert Binary to Decimal

print("Enter 'x' for exit.");
binary = input("Enter number in Binary Format: ");
if binary == 'x':
    exit();
else:
    decimal = int(binary, 2);
    print(binary,"in Decimal =",decimal);