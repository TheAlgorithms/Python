# This is python code to implement Gauss-Seidel method for solving linear equations

# Gauss Seidel Method 
# initially assumes the solution to be zero
# Then in each iteration improves the solution by using the previous solution


# Defining our function as seidel which takes 3 arguments
# as A matrix, Solution and B matrix

def seidel(a, x ,b):
	#Finding length of a(3)	
	n = len(a)				
	# for loop for 3 times as to calculate x, y , z
	for j in range(0, n):		
		# temp variable d to store b[j]
		d = b[j]				
		
		# to calculate respective xi, yi, zi
		for i in range(0, n):	
			if(j != i):
				d-=a[j][i] * x[i]
		# updating the value of our solution		
		x[j] = d / a[j][j]
	# returning our updated solution		
	return x	
	
if __name__ == "__main__":
    n = int(input("Enter the number of variables: "))	# variables						
    a = []		# Coefficient Matrix					
    b = []		# Constant Matrix
    x = []      # Solution Matrix
    # initial solution depending on n(here n=3)	
    print("Enter the coefficient Matrix (nxn)\n")	
    for i in range(0, n):
        a.append([])
        for j in range(0, n):
            a[i].append(int(input("Enter a["+str(i)+"]["+ str(j)+"]: "))) 
        x.append(0)
    for i in range(0, n):
        b.append(int(input("Enter b["+str(i)+"]: ")))           			
    # x = [0, 0, 0]						  # Solution Assumption
    # a = [[4, 1, 2],[3, 5, 1],[1, 1, 3]]   
    # b = [4,7,3]                           
    m=1000
    m = int(input("Enter the number of iterations: "))	# iterations
    print(x)
    #loop run for m times depending on m the error value
    for i in range(0, m):			
        x = seidel(a, x, b)
        #print each time the updated solution
        print(x)					


# ------------ Sample Input ------------
# 4x + y + 2z = 4
# 3x + 5y + z = 7
# x + y + 3z = 3

# For the above equations the input will be
# 3
# 4 1 2
# 3 5 1
# 1 1 3
# 4 7 3