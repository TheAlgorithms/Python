M = 8
N = 8

# A recursive function to replace 
# previous color 'prevC' at '(x, y)' 
# and all surrounding pixels of (x, y) 
# with new color 'newC' and 
def floodFillUtil(screen, x, y, prevC, newC):
	
	# Base cases
	if (x < 0 or x >= M or y < 0 or
		y >= N or screen[x][y] != prevC or
		screen[x][y] == newC):
		return

	# Replace the color at (x, y)
	screen[x][y] = newC

	# Recur for north, east, south and west
	floodFillUtil(screen, x + 1, y, prevC, newC)
	floodFillUtil(screen, x - 1, y, prevC, newC)
	floodFillUtil(screen, x, y + 1, prevC, newC)
	floodFillUtil(screen, x, y - 1, prevC, newC)

# It mainly finds the previous color on (x, y) and 
# calls floodFillUtil() 
def floodFill(screen, x, y, newC):
	prevC = screen[x][y]
	if(prevC==newC):
	    return
	floodFillUtil(screen, x, y, prevC, newC)

# Driver Code
screen = [[1, 1, 1, 1, 1, 1, 1, 1], 
		[1, 1, 1, 1, 1, 1, 0, 0], 
		[1, 0, 0, 1, 1, 0, 1, 1], 
		[1, 2, 2, 2, 2, 0, 1, 0], 
		[1, 1, 1, 2, 2, 0, 1, 0], 
		[1, 1, 1, 2, 2, 2, 2, 0], 
		[1, 1, 1, 1, 1, 2, 1, 1], 
		[1, 1, 1, 1, 1, 2, 2, 1]]

x = 4
y = 4
newC = 3
floodFill(screen, x, y, newC)

print ("Updated screen after call to floodFill:")
for i in range(M):
	for j in range(N):
		print(screen[i][j], end = ' ')
	print()