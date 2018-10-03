import sys
infy=sys.maxsize

d=int(input("Enter the number of denominations available "))
print("Enter",d,"denominations ")
cd=[int(x) for x in input().split()]
a=int(input("Enter the amount "))

coinLocation=[-1]*(a+1)
solution=[infy]*(a+1)
solution[0]=0

for i in range(d):
	for j in range(cd[i],a+1):
		if (solution[j-cd[i]]+1) < solution[j]:
			solution[j]=solution[j-cd[i]]+1
			coinLocation[j]=i

print("Minimum number of coins required =",solution[a])
answer=""
while a:
	answer+=" "+str(cd[solution[a]])
	a-=cd[solution[a]]
print("Denominations of coins required"+answer)