'''
By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.

   3
  7 4
 2 4 6
8 5 9 3

That is, 3 -> 7 -> 4 -> 9 = 23.

Find the maximum total from top to bottom of the triangle below:

				     75
			       95 64
			      17 47 82
			    18 35 87 10
		       20 04 82 47 65
             19 01 23 75 03 34
            88 02 77 73 07 63 67
          99 65 04 28 06 16 70 92
         41 41 26 56 83 40 80 70 33
       41 48 72 33 47 32 37 16 94 29
      53 71 44 65 25 43 91 52 97 51 14
    70 11 33 28 77 73 17 78 39 68 17 57
   91 71 52 38 17 14 91 43 58 50 27 29 48
 63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23


'''


def solution(ar,n):
	""" Returns the max sum going down the triangle
	
	>>> solution(
		[
			[75], 
			[95, 64], 
			[17, 47, 82], 
			[18, 35, 87, 10], 
			[20, 4, 82, 47, 65], 
			[19, 1, 23, 75, 3, 34], 
			[88, 2, 77, 73, 7, 63, 67], 
			[99, 65, 4, 28, 6, 16, 70, 92], 
			[41, 41, 26, 56, 83, 40, 80, 70, 33], 
			[41, 48, 72, 33, 47, 32, 37, 16, 94, 29], 
			[53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14], 
			[70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57], 
			[91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48], 
			[63, 66, 4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31], 
			[4, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23]
		], 15)
	
	724

	>>> solution(
		[
			[3],
			[7,4],
			[2,4,6],
			[8,5,9,3]
		],4)
	
	23

	"""
	dp = [[0 for i in range(n)] for j in range(n)]
	dp[0][0] = ar[0][0]
	for i in range(1,n):
		dp[i][0] = dp[i-1][0] + ar[i][0]
		dp[i][i] = dp[i-1][i-1] + ar[i][i]
		for j in range(1,i):
			dp[i][j] = max(dp[i-1][j-1],dp[i-1][j])+ar[i][j]
	return dp[n-1][n-1]
    
if __name__=="__main__":
    tree = []
    n = int(input("Length of triangle: "))
    for i in range(n):
    	tree.append(list(map(int,input().strip().split())))
    print(tree)
    print(solution(tree,n))