from math import sqrt

def factors(n):
	
	v = []
	v.append(1)

	for i in range(2, int(sqrt(n)) + 1, 1):
		
		
		if (n % i == 0):
			v.append(i)
			if (int(n / i) != i):
				v.append(int(n / i))
	return v

def abundant(n):
	sum = 0
	v = factors(n)
	for i in range(len(v)):
		sum += v[i]
	if (sum > n):
		return True
	else:
		return False

def semiPerfect(n):
	v = factors(n)
	v.sort(reverse = False)
	r = len(v)
	subset = [[0 for i in range(n + 1)]
				for j in range(r + 1)]

	for i in range(r + 1):
		subset[i][0] = True
    
	for i in range(1, n + 1):
		subset[0][i] = False
    
	for i in range(1, r + 1):
		for j in range(1, n + 1):
			if (j < v[i - 1]):
				subset[i][j] = subset[i - 1][j]
			else:
				subset[i][j] = (subset[i - 1][j] or
								subset[i - 1][j - v[i - 1]])

	if ((subset[r][n]) == 0):
		return False
	else:
		return True
  
def weird(n):
	if (abundant(n) == True and semiPerfect(n) == False):
		return True
	else:
		return False

if __name__ == '__main__':
	n = 70

	if (weird(n)):
		print("Weird Number")
	else:
		print("Not Weird Number")
