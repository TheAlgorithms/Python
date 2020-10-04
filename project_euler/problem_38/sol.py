def solution():
	answer = ""
	for n in range(2, 10):
		for a in range(1, 10**(9 // n)):
			s = "".join(str(a * j) for j in range(1, n + 1))
			randomv = "".join(sorted(s))
            if randomv == "123456789":
				answer = max(s, answer)
	return answer
