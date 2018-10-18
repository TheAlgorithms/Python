#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#program to count the number of times a given substring has been repeated in a given string
def countingSubstrings(string,substring):
    count=0
    for i in range(0,len(string)):
        if string[i:i+len(substring)]==substring:
            count=count+1
    return count
S=input("Enter a string: ")
SUB=input("Enter the subsring: ")
COUNT=countingSubstrings(S,SUB)
print ("The number of times the given substring: ",SUB," ,in the string: ",S,", is: ",COUNT)
