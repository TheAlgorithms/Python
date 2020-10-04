"""
Count the number of ways to tile the floor of size n x m using 1 x m size tiles
Given a floor of size n x m and tiles of size 1 x m. The problem is to count the number of ways to tile the 
given floor using 1 x m tiles. A tile can either be placed horizontally or vertically.
Both n and m are positive integers and 2 < = m.

Examples:

Input : n = 2, m = 3
Output : 1
Only one combination to place 
two tiles of size 1 x 3 horizontally
on the floor of size 2 x 3. 

Input :  n = 4, m = 4
Output : 2
1st combination:
All tiles are placed horizontally
2nd combination:
All tiles are placed vertically.
"""

"""
This problem is mainly a more generalized approach to the Tiling Problem.
Approach: For a given value of n and m, the number of ways to tile the 
floor can be obtained from the following relation.


            |  1, 1 < = n < m
 count(n) = |  2, n = m
            | count(n-1) + count(n-m), m < n
"""          
def tiling(n,m):
	count=[]
	for i in range(n+2):
		count.append(0)
	count[0]=0
	for i in range(1,n+1):
		# recurssive cases
		if i > m:
			count[i]=count[i-1]+count[i-m]
		#base cases
		elif i <m:
			count[i]=1
		# i == m
		else:
			count[i]=2
	return count[n]


# print(tiling(7,4))

"""
Count number of ways to fill a “n x 4” grid using “1 x 4” tiles
Given a number n, count number of ways to fill a n x 4 grid using 1 x 4 tiles

Examples:

Input : n = 1
Output : 1

Input : n = 2
Output : 1
We can only place both tiles horizontally

Input : n = 3
Output : 1
We can only place all tiles horizontally.

Input : n = 4
Output : 2
The two ways are : 
  1) Place all tiles horizontally 
  2) Place all tiles vertically.

Input : n = 5
Output : 3
We can fill a 5 x 4 grid in following ways : 
  1) Place all 5 tiles horizontally
  2) Place first 4 vertically and 1 horizontally.
  3) Place first 1 horizontally and 4 horizontally.

Let “count(n)” be the count of ways to place tiles on a “n x 4” grid, 
following two cases arise when we place the first tile.

Place the first tile horizontally : If we place first tile horizontally, 
the problem reduces to “count(n-1)”
Place the first tile vertically : If we place first tile vertically, 
then we must place 3 more tiles vertically. So the problem reduces to 
“count(n-4)”

Therefore, count(n) can be written as below.

   count(n) = 1 if n = 1 or n = 2 or n = 3   
   count(n) = 2 if n = 4
   count(n) = count(n-1) + count(n-4) 
"""

def titling(n):
	count=[0 for i in range(n+1)]
	for i in range(1,n+1):
		if i<=3:
			count[i]=1
		elif i==4:
			count[i]==2
		else:
			count[i]=count[i-1]+count[i-4]
	return count[n]