from __future__ import print_function
'''
Number letter counts
Problem 17

If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?


NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) 
contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.
'''

ones_counts = [0, 3, 3, 5, 4, 4, 3, 5, 5, 4, 3, 6, 6, 8, 8, 7, 7, 9, 8, 8] #number of letters in zero, one, two, ..., nineteen (0 for zero since its never said aloud)
tens_counts = [0, 0, 6, 6, 5, 5, 5, 7, 6, 6] #number of letters in twenty, thirty, ..., ninety (0 for numbers less than 20 due to inconsistency in teens)

count = 0

for i in range(1, 1001):
	if i < 1000:
		if i >= 100:
			count += ones_counts[i/100] + 7 #add number of letters for "n hundred"

			if i%100 is not 0:
				count += 3 #add number of letters for "and" if number is not multiple of 100

		if 0 < i%100 < 20:
			count += ones_counts[i%100] #add number of letters for one, two, three, ..., nineteen (could be combined with below if not for inconsistency in teens)
		else:
			count += ones_counts[i%10] + tens_counts[(i%100-i%10)/10] #add number of letters for twenty, twenty one, ..., ninety nine
	else:
		count += ones_counts[i/1000] + 8

print(count)