import copy

#Taking user inputs
x=int(input('Enter number of rows of triangle\n'))
triangle = []
print('Enter space-separated values for each row on a new line')
for i in range (0,x):
	line = input().split(' ')
	line = [int(val) for val in line]
	triangle.append(line)
square = []
index = 0
k = x-1
'''convert to a 2D-array representation
if input is say   1
                 2 3,
change it to    -1000 1 -1000
                  2  -1000  3
so that it is easier to process. The negative paths won't give maximum sum anyway
'''
for i in range (0,x):
	temp_line = []
	for j in range (0,k):
		temp_line.append(-1000)
	for idx,j in enumerate(triangle[index]):
		temp_line.append(j)
		if idx == len(triangle[index])-1:
			break
		temp_line.append(-1000)
	for j in range (0,k):
		temp_line.append(-1000)
	square.append(temp_line)
	k = k - 1
	index = index + 1

path = copy.deepcopy(square) #Make a copy of the array to store the path in
#We use the rule that if maximum number came from left, we change that value of array to 'L', else 'R'
#The solution is done by dynamic programming
for i in range (0,x):
	if i==0:
		continue
	for j in range (2*x-1):
		if j == 0:
			square[i][j] += square[i-1][1]
			path[i][j] = 'R'
		elif j == 2*x-2:
			square[i][j] += square[i-1][2*x-3]
			path[i][j] = 'L'
		else:
			square[i][j] += max(square[i-1][j-1],square[i-1][j+1])
			if square[i-1][j-1]>square[i-1][j+1]:
				path[i][j] = 'L'
			else:
				path[i][j] = 'R'

print ('Maximum value is '+str(max(square[x-1])))
m = max(square[x-1])
pos = [i for i, j in enumerate(square[x-1]) if j == m][0] #Find the maximum index so that we can backtrack
trace = ""
for i in range (x-1,0,-1):
	trace += 'R' if path[i][pos] == 'L' else 'L' #Tracing reverse path
	if path[i][pos] == 'L':
		pos = pos - 1
	else:
		pos = pos + 1

#Comment the following line if path printing isn't required, as that wasn't asked in the question.
print('The path taken is '+trace)