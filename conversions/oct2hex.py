# -*- coding: utf-8 -*-
"""
Created on Fri Oct 11 07:33:01 2019

@author: beast
"""

# Python Program - Convert Octal to Hexadecimal

print("Enter 'x' for exit.");
octal = input("Enter a number in Octal Format: ");
if octal == 'x':
    exit();
else:
    dec = str(int(octal, 8));
    decm = int(dec);
    print(octal,"in Hexadecimal =",hex(decm));