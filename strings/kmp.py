def lca(s):
	i = 1
	j = 0
	dp = [0] * len(s)
	while(i < len(s)):
		if(s[i] == s[j]):
			dp[i] = j + 1
			i = i + 1
			j = j + 1
		elif j > 0:
			j = dp[j - 1]
		else:
			i = i + 1
	return dp
def kmp(s, p, dp):
	i = 1
	j = 0
	l = list()
	while i < len(s):
		if(j == len(p)):
			l.append(i - j)
			j = dp[j - 1]
		elif(s[i] == p[j]):
			j = j + 1
		elif j > 0:
			j = dp[j - 1]
		i = i + 1
	return l

if __name__ == '__main__':
	print(kmp("ijaosdprajsaihdhprajsajdho", "praj", lca("praj")))

