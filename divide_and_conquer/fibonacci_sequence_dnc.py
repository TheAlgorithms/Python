"""
We can find the Fibonacci sequence more effectively than naive bottom-up algorithm
    We use One of the well-known properties of Fibonacci number is:

    | F(n+1) ,  F(n)   |       | 1 , 1 | ^ n
    |                  |   =   |       |
    | F(n)   ,  F(n-1) |       | 1 , 0 |

    We can therefore compute the (n)th power of A = ((1,1),(1,0)) using recursive squaring

    Time complexity: O(log(n)), because it is a divide and conquer algorithm
"""


def get_fibonacci(n):
    """
    :param n: number of Sequence
    :return: (n)th sequence of Fibonacci sequence

    >>> get_fibonacci(5)
    5
    >>> get_fibonacci(10)
    55
    >>> get_fibonacci(20)
    6765
    """
    if n < 2:
        matrix = [[1, n], [1, 0]]
        return matrix[0][1]
    else:
        matrix = [[1, 1], [1, 0]]
        return get_squared(matrix, n)[0][1]


def get_squared(matrix, n):
    if n == 1:
        return matrix
    elif n % 2 == 0:
        temp = get_squared(matrix, n / 2)
        return mul(temp, temp);
    else:
        temp = get_squared(matrix, (n - 1) / 2)
        temp2 = mul(temp, temp)
        return mul(temp2, matrix)


# perform matrix multiplication
def mul(left_matrix, right_matrix):
    n = 2
    multiplied_matrix  = [[0, 0], [0, 0]]

    for i in range(n):
        for j in range(n):
            multiplied_matrix[i][j] = 0

            for k in range(n):
                multiplied_matrix[i][j] = int(multiplied_matrix[i][j] + left_matrix[i][k] * right_matrix[k][j]);
    return multiplied_matrix

if __name__ == "__main__":
    import doctest

    doctest.testmod()
