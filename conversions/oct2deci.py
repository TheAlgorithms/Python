# -*- coding: utf-8 -*-
"""
Created on Fri Oct 11 07:31:57 2019

@author: beast
"""

# Python Program - Convert Octal to Decimal

print("Enter 'x' for exit.");
octal = input("Enter number in Octal Format: ");
if octal == 'x':
    exit();
else:
    decimal = str(int(octal, 8));
    print(octal,"in Decimal =",decimal);