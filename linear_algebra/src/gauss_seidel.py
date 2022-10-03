# This is python code to implement Gauss-Seidel method for solving linear equations

# Gauss Seidel Method (https://en.wikipedia.org/wiki/Gauss%E2%80%93Seidel_method)
# initially assumes the solution to be zero
# Then in each iteration improves the solution by using the previous solution


# Defining our function as gauss_seidel which takes 4 arguments
# as A matrix(nxn), Solution and B matrix and max iterations


def update_solution(
    coefficient_matrix: list[list], solution_vector: list, constant_vector: list
) -> list:
    """
    Function to update the solution
    :param coefficient_matrix: list, Coefficient Matrix
    :param solution_vector: list, Solution Vector
    :param constant_vector: list, Constant Vector
    :return: list, Updated Solution Vector
    Example:
    >>> a = [[10, -1, 2, 0], [-1, 11, -1, 3], [2, -1, 10, -1], [0, 3, -1, 8]]
    >>> x = [0, 0, 0, 0]
    >>> b = [6, 25, -11, 15]
    >>> update_solution(a, x, b)
    [0.6, 2.3272727272727276, -0.9872727272727271, 0.8788636363636363]
    """
    n = len(coefficient_matrix)  # number of variables
    for i in range(0, n):
        # Update each variable
        d = constant_vector[i]
        for j in range(0, n):
            if i != j:
                d -= coefficient_matrix[i][j] * solution_vector[j]
        solution_vector[i] = d / coefficient_matrix[i][i]
    return solution_vector


def gauss_seidel(
    coefficient_matrix: list[list],
    solution_vector: list,
    constant_vector: list,
    maximum_iterations: int,
) -> None:
    """
    Function to perform Gauss Seidel Iteration
    :param coefficient_matrix: list, Coefficient Matrix
    :param solution_vector: list, Solution Vector
    :param constant_vector: list, Constant Vector
    :param maximum_iterations: int, Maximum Iterations
    :return: None

    Example:
    >>> a = [[10, -1, 2, 0], [-1, 11, -1, 3], [2, -1, 10, -1], [0, 3, -1, 8]]
    >>> x = [0, 0, 0, 0]
    >>> b = [6, 25, -11, 15]
    >>> gauss_seidel(a, x, b, 100)
    [1.0, 2.0, -1.0, 1.0]
    """
    for i in range(0, maximum_iterations):
        solution_vector = update_solution(
            coefficient_matrix, solution_vector, constant_vector
        )
        # print("Iteration {}: {}".format(i, x))
    print(solution_vector)


if __name__ == "__main__":
    import doctest

    doctest.testmod()

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
