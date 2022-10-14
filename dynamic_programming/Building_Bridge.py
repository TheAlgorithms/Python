
def maxBridges(values,n):
	
	values.sort(key=lambda x:(x[0],x[1]))
	
	clean = [values[i][1] for i in range(n)]
	
	dp = [1 for i in range(n)]
	for i in range(1,len(clean)):
		for j in range(i):
			if clean[i] >= clean[j] and dp[i] < dp[j]+1:
				dp[i] = dp[j]+1
	
	return max(dp)
values=[[6,2],[4,3],[2,6],[1,5]]
n=len(values)
print("Maximum number of bridges =", maxBridges(values,n))
