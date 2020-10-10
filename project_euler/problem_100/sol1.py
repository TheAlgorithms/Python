import eulerlib
def compute():
	# Fundamental solution
	x0 = 3
	y0 = 1
	
	# Current solution
	x = x0
	y = y0  # An alias for the number of red discs
	while True:
		# Check if this solution is acceptable
		sqrt = eulerlib.sqrt(y**2 * 8 + 1)
		if sqrt % 2 == 1:  # Is odd
			blue = (sqrt + 1) // 2 + y
			if blue + y > 10**12:
				return str(blue)
		
		# Create the next bigger solution
		nextx = x * x0 + y * y0 * 8
		nexty = x * y0 + y * x0
		x = nextx
		y = nexty


if __name__ == "__main__":
	print(compute())
