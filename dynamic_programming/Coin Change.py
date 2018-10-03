import sys
infy=sys.maxsize
d=int(input("Enter the number of denominations available "))
print("Enter",d,"denominations ")
cd=[int(x) for x in input().split()]
a=int(input("Enter the amount "))
solution=[[infy for x in range(a+1)] for y in range(d)]
#print(solution)
cd.sort()
for i in range(d):
	for j in range(0,a+1):
		if j==0:
			solution[i][j]=0;
		else:
			#print("j=",j,"cd[i]=",cd[i])
			if cd[i]<=j:
				solution[i][j]=min(1+solution[i][j-cd[i]],solution[i-1][j])
			else:
				solution[i][j]=solution[i-1][j]
			#print("solution[i][j]=",solution[i][j])
print("Minimum number of coins required =",solution[d-1][a])