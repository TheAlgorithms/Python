def treug(a, b, c):
	p = (a + b + c) / 2 #Semi-Perimeter
	S = (p * (p - a) * (p - b) * (p - c)) ** (1 / 2) #Area by Heron's Formula
	return S

print(treug(5, 5, 5))