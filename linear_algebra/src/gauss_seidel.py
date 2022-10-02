# This is python code to implement Gauss-Seidel method for solving linear equations

# Gauss Seidel Method (https://en.wikipedia.org/wiki/Gauss%E2%80%93Seidel_method)
# initially assumes the solution to be zero
# Then in each iteration improves the solution by using the previous solution


# Defining our function as seidel which takes 3 arguments
# as A matrix, Solution and B matrix


def update_solution(a: list[list[float]], x: list[float], b: list[float]) -> list[float]:
    """
        Function to update the solution
        a: coefficient matrix
        x: solution vector
        b: constant vector

        Example:
        >>> a = [[10, -1, 2, 0], [-1, 11, -1, 3], [2, -1, 10, -1], [0, 3, -1, 8]]
        >>> x = [0, 0, 0, 0]
        >>> b = [6, 25, -11, 15]
        >>> update_solution(a, x, b)
        [0.6, 2.3272727272727276, -0.9872727272727271, 0.8788636363636363]
    """
    n = len(a)  # number of variables
    for i in range(0, n):
        # Update each variable
        d = b[i]
        for j in range(0, n):
            if(i != j):
                d -= a[i][j] * x[j]
        x[i] = d / a[i][i]
    return x


def gauss_seidel(a: list[list[float]], x: list[float], b: list[float], m: int) -> None:
    """
        Function to perform Gauss Seidel Iteration
        a: coefficient matrix
        x: solution vector
        b: constant vector
        m: max iterations

        Example:
        >>> a = [[10, -1, 2, 0], [-1, 11, -1, 3], [2, -1, 10, -1], [0, 3, -1, 8]]
        >>> x = [0, 0, 0, 0]
        >>> b = [6, 25, -11, 15]
        >>> gauss_seidel(a, x, b, 100)
        [1.0, 2.0, -1.0, 1.0]
    """
    for i in range(0, m):
        x = update_solution(a, x, b)
        # print("Iteration {}: {}".format(i, x))
    print(x)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
# if __name__ == "__main__":
#     n = int(input("Enter the number of variables: "))	# variables
#     a = []		# Coefficient Matrix
#     b = []		# Constant Matrix
#     x = []      # Solution Matrix
#     m=1000
#     # initial solution depending on n(here n=3)
#     print("Enter the coefficient Matrix (nxn)\n")
#     for i in range(0, n):
#         a.append([])
#         for j in range(0, n):
#             a[i].append(int(input("Enter a["+str(i)+"]["+ str(j)+"]: ")))
#         x.append(0)
#     for i in range(0, n):
#         b.append(int(input("Enter b["+str(i)+"]: ")))
#     m = int(input("Enter the number of iterations: "))	# iterations
#     print("Initial Guess : {}".format(x))
#     gauss_seidel(a, x, b, m)

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
