"""
Implementation of finding nth fibonacci number using matrix exponentiation.
Time Complexity is about O(log(n)*8), where 8 is the complexity of matrix multiplication of size 2 by 2.
And on the other hand complexity of bruteforce solution is O(n).
As we know
    f[n] = f[n-1] + f[n-1]
Converting to matrix,
    [f(n),f(n-1)] = [[1,1],[1,0]] * [f(n-1),f(n-2)]
->  [f(n),f(n-1)] = [[1,1],[1,0]]^2 * [f(n-2),f(n-3)]
    ...
    ...
->  [f(n),f(n-1)] = [[1,1],[1,0]]^(n-1) * [f(1),f(0)]
So we just need the n times multiplication of  the matrix [1,1],[1,0]].
We can decrease the n times multiplication by following  the divide and conquer approach.

"""
from __future__ import print_function


def multiply(matrix_a, matrix_b):
    matrix_c = []
    n = len(matrix_a)
    for i in range(n):
        list_1 = []
        for j in range(n):
            val = 0
            for k in range(n):
                val = val + matrix_a[i][k] * matrix_b[k][j]
            list_1.append(val)
        matrix_c.append(list_1)
    return matrix_c


def identity(n):
    return [[int(row == column) for column in range(n)] for row in range(n)]


def nth_fibonacci(n):
    """
    >>> nth_fibonacci(100)
    354224848179261915075L
    >>> nth_fibonacci(-100)
    -100
    """
    if n <= 1:
        return n
    res_matrix = identity(2)
    fibonacci_matrix = [[1, 1], [1, 0]]
    n = n - 1
    while n > 0:
        if n % 2 == 1:
            res_matrix = multiply(res_matrix, fibonacci_matrix)
        fibonacci_matrix = multiply(fibonacci_matrix, fibonacci_matrix)
        n = int(n / 2)
    return res_matrix[0][0]


def nth_fibonacci_test(n):
    if n <= 1:
        return n
    fib0 = 0
    fib1 = 1
    for i in range(2, n + 1):
        fib0, fib1 = fib1, fib0 + fib1
    return fib1


def main():
    print(
        "0th fibonacci number using matrix exponentiation is %s and using bruteforce is %s \n"
        % (nth_fibonacci(0), nth_fibonacci_test(0))
    )
    print(
        "1st fibonacci number using matrix exponentiation is %s and using bruteforce is %s \n"
        % (nth_fibonacci(1), nth_fibonacci_test(1))
    )
    print(
        "2nd fibonacci number using matrix exponentiation is %s and using bruteforce is %s \n"
        % (nth_fibonacci(2), nth_fibonacci_test(2))
    )
    print(
        "3rd fibonacci number using matrix exponentiation is %s and using bruteforce is %s \n"
        % (nth_fibonacci(3), nth_fibonacci_test(3))
    )
    print(
        "10th fibonacci number using matrix exponentiation is %s and using bruteforce is %s \n"
        % (nth_fibonacci(10), nth_fibonacci_test(10))
    )
    print(
        "100th fibonacci number using matrix exponentiation is %s and using bruteforce is %s \n"
        % (nth_fibonacci(100), nth_fibonacci_test(100))
    )
    print(
        "1000th fibonacci number using matrix exponentiation is %s and using bruteforce is %s \n"
        % (nth_fibonacci(1000), nth_fibonacci_test(1000))
    )


if __name__ == "__main__":
    main()
