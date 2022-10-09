from math import sqrt
from typing import List

def factors(n : int) -> List[int]:

    v = []
    v.append(1)

    for i in range(2, int(sqrt(n)) + 1, 1):

        if n % i == 0:
            v.append(i)
            if int(n / i) != i:
                v.append(int(n / i))
    return v


def abundant(n : int) -> bool:
	sum = 0
	v = factors(n)
	for i in range(len(v)):
		sum += v[i]
	if (sum > n):
		return True
	else:
		return False

def semi_perfect(n: int) -> bool:
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
			if j < v[i - 1]:
				subset[i][j] = subset[i - 1][j]
			else:
				subset[i][j] = subset[i - 1][j] or subset[i - 1][j - v[i - 1]]
				
	if (subset[r][n]) == 0:
		return False
	else:
		 return True

def weird(n : int) -> bool:
	if (abundant(n) == True and semi_perfect(n) == False):
		return True
	else:
		return False

def main() -> None:
	n = 70
	if (weird(n)):
		print("Weird Number")
	else:
		print("Not Weird Number")
    
if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
    main()
