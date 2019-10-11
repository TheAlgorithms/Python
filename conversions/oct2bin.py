# -*- coding: utf-8 -*-
"""
Created on Fri Oct 11 07:32:36 2019

@author: beast
"""

# Python Program - Convert Octal to Binary

print("Enter 'x' for exit.");
octal = input("Enter any number in Octal Format: ");
if octal == 'x':
    exit();
else:
    dec = str(int(octal, 8));
    decm = int(dec);
    print(octal,"in Binary =",bin(decm));