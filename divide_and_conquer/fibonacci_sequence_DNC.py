"""
We can find the Fibonacci sequence more effectively than naive bottom-up algorithm

	 We use One of the well-known properties of Fibonacci number is:

	 | F(n+1) ,  F(n)   |       | 1 , 1 | ^ n
	 |                  |   =   |       |
	 | F(n)   ,  F(n-1) |       | 1 , 0 |

	 We can therefore compute the (n)th power of A = ((1,1),(1,0)) using recursive squaring

	 Time complexity: O(log(n)), because it is a divide and conquer algorithm
"""

# return (n)th term of Fibonacci sequence
def getFibonacci(n):
    if n < 2:
        matrix = [[1, n], [1, 0]]
        return matrix[0][1]
    else:
        matrix = [[1, 1], [1, 0]]
        return pow(matrix, n)[0][1]

def pow(matrix, n):
    if n == 1:
        return matrix
    elif n % 2 == 0:
        temp = pow(matrix, n / 2)
        return mul(temp, temp);
    else:
        temp = pow(matrix, (n - 1) / 2)
        temp2 = mul(temp, temp)
        return mul(temp2, matrix)

# perform matrix multiplication
def mul(a, b):
    n = 2
    c = [[0, 0], [0, 0]]

    for i in range(n):
        for j in range(n):
            c[i][j] = 0

            for k in range(n):
                c[i][j] = int(c[i][j] + a[i][k] * b[k][j]);

    return c



