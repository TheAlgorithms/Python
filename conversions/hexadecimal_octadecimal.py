# importing math package
import math
hex = "1AC"

# variable oct to store
# octal equivalent of hexa decimal
# number returned from the method
oct = ""
dec = i = 0
c = len(hex) - 1

# loop to extract each digit of number
while i < len(hex):
	
	# digit extracted
	d = hex[i]
	if d == '0' or d == '1' or d == '2' or \
		d == '3' or d == '4' or d == '5':
		dec = dec + int(d) * int(math.pow(16, c))
	elif d == '6' or d == '7' or d == '8' or d == '9':
		dec = dec + int(d) * int(math.pow(16, c))
	elif (d == 'A') or (d == 'a'):
		dec = dec + 10 * int(math.pow(16, c))
	elif (d == 'B') or (d == 'b'):
		dec = dec + 11 * int(math.pow(16, c))
	elif (d == 'C') or (d == 'c'):
		dec = dec + 12 * int(math.pow(16, c))
	elif (d == 'D') or (d == 'd'):
		dec = dec + 13 * int(math.pow(16, c))
	elif (d == 'E') or (d == 'e'):
		dec = dec + 14 * int(math.pow(16, c))
	elif (d == 'F') or (d == 'f'):
		dec = dec + 15 * int(math.pow(16, c))
	else:
		print("invalid input")
		break
	i+= 1
	c -= 1

# loop to find octal equivalent
# stored in dec i.e.
# conversion of decimal to octal.
while (dec > 0):
	oct = "".join([str(int(dec % 8)) , oct])
	dec = int(dec / 8)

# printing the final result
print("Equivalent Octal Value =",oct)
