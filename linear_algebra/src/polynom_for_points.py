def points_to_polynomial(coordinates) -> str:
    """
    coordinates is a two dimensional matrix: [[x, y], [x, y], ...]
    number of points you want to use

    >>> print(points_to_polynomial([]))
    Traceback (most recent call last):
        ...
    ValueError: The program cannot work out a fitting polynomial.
    >>> print(points_to_polynomial([[]]))
    Traceback (most recent call last):
        ...
    ValueError: The program cannot work out a fitting polynomial.
    >>> print(points_to_polynomial([[1, 0], [2, 0], [3, 0]]))
    f(x)=x^2*0.0+x^1*-0.0+x^0*0.0
    >>> print(points_to_polynomial([[1, 1], [2, 1], [3, 1]]))
    f(x)=x^2*0.0+x^1*-0.0+x^0*1.0
    >>> print(points_to_polynomial([[1, 3], [2, 3], [3, 3]]))
    f(x)=x^2*0.0+x^1*-0.0+x^0*3.0
    >>> print(points_to_polynomial([[1, 1], [2, 2], [3, 3]]))
    f(x)=x^2*0.0+x^1*1.0+x^0*0.0
    >>> print(points_to_polynomial([[1, 1], [2, 4], [3, 9]]))
    f(x)=x^2*1.0+x^1*-0.0+x^0*0.0
    >>> print(points_to_polynomial([[1, 3], [2, 6], [3, 11]]))
    f(x)=x^2*1.0+x^1*-0.0+x^0*2.0
    >>> print(points_to_polynomial([[1, -3], [2, -6], [3, -11]]))
    f(x)=x^2*-1.0+x^1*-0.0+x^0*-2.0
    >>> print(points_to_polynomial([[1, 5], [2, 2], [3, 9]]))
    f(x)=x^2*5.0+x^1*-18.0+x^0*18.0
    """
    set_x = {x for x, _ in coordinates}
    error_handle(coordinates, set_x)
    
    if len(set_x) == 1:
        return f"x={coordinates[0][0]}"

    x = len(coordinates)

    matrix = feature_matrix(x, coordinates)

    vector = y_coordinates(x, coordinates)

    find_solution(x, vector, matrix)
        
    solved = str_solution(x, vector, matrix)

    return solved

def error_handle(coordinates, set_x) -> None:
    """
    Handling illegal inputs.

    Args:
        coordinates (list[list[float]]): input data points
        set_x (set): x coordinates

    Raises:
        ValueError: Empty input or dimension of each point is not the same
        ValueError: Empty point detected.
        ValueError: Empty point detected.
    """
    if len(coordinates) == 0 or not all(len(pair) == 2 for pair in coordinates):
        raise ValueError("The program cannot work out a fitting polynomial.")

    if len({tuple(pair) for pair in coordinates}) != len(coordinates):
        raise ValueError("The program cannot work out a fitting polynomial.")

    if len(set_x) != len(coordinates):
        raise ValueError("The program cannot work out a fitting polynomial.")

def feature_matrix(x, coordinates): 
    """
    Return the feature matrix of the data points.
    
    Args:
        x (int): order of the polynomial + 1
        coordinates (list[list[float]]): input data points
        
    Returns:
        list[list[float]]: feature matrix.
    """
    count_of_line = 0
    matrix: list[list[float]] = []
    # put the x and x to the power values in a matrix
    while count_of_line < x:
        count_in_line = 0
        a = coordinates[count_of_line][0]
        count_line: list[float] = []
        while count_in_line < x:
            count_line.append(a ** (x - (count_in_line + 1)))
            count_in_line += 1
        matrix.append(count_line)
        count_of_line += 1
    return matrix

def y_coordinates(x, coordinates):
    """
    Return the y coordinates of the data points.

    Args:
        x (int): order of the polynomial + 1
        coordinates (list[list[float]]): input data points

    Returns:
        list[float]: y coordinates of the data points
    """
    count_of_line = 0
    # put the y values into a vector
    vector: list[float] = []
    while count_of_line < x:
        vector.append(coordinates[count_of_line][1])
        count_of_line += 1
    return vector

def find_solution(x, vector, matrix):
    """
    Find coefficients of the polynomial using Gaussian Elimination.
    The coefficients will be stored in the diagonal of matrix.

    Args:
        x (int): order of the polynomial + 1
        vector (list[float]): y coordinates of the points
        matrix (list[list[float]]): feature matrix
    """
    count = 0

    while count < x:
        zahlen = 0
        while zahlen < x:
            if count == zahlen:
                zahlen += 1
            if zahlen == x:
                break
            bruch = matrix[zahlen][count] / matrix[count][count]
            for counting_columns, item in enumerate(matrix[count]):
                # manipulating all the values in the matrix
                matrix[zahlen][counting_columns] -= item * bruch
            # manipulating the values in the vector
            vector[zahlen] -= vector[count] * bruch
            zahlen += 1
        count += 1

def str_solution(x, vector, matrix) -> str:
    """
    Stringfy the solution.
    
    Args:
        x (int): order of the polynomial + 1
        vector (list[float]): y coordinates of the points
        matrix (list[list[float]]): feature matrix

    Returns:
        str: polynomial represented as string
    """
    count = 0
    solution: list[str] = []
    while count < x:
        solution.append(str(vector[count] / matrix[count][count]))
        count += 1

    count = 0
    solved = "f(x)="

    while count < x:
        remove_e: list[str] = solution[count].split("E")
        if len(remove_e) > 1:
            solution[count] = f"{remove_e[0]}*10^{remove_e[1]}"
        solved += f"x^{x - (count + 1)}*{solution[count]}"
        if count + 1 != x:
            solved += "+"
        count += 1
    return solved
        
if __name__ == "__main__":
    print(points_to_polynomial([]))
    print(points_to_polynomial([[]]))
    print(points_to_polynomial([[1, 0], [2, 0], [3, 0]]))
    print(points_to_polynomial([[1, 1], [2, 1], [3, 1]]))
    print(points_to_polynomial([[1, 3], [2, 3], [3, 3]]))
    print(points_to_polynomial([[1, 1], [2, 2], [3, 3]]))
    print(points_to_polynomial([[1, 1], [2, 4], [3, 9]]))
    print(points_to_polynomial([[1, 3], [2, 6], [3, 11]]))
    print(points_to_polynomial([[1, -3], [2, -6], [3, -11]]))
    print(points_to_polynomial([[1, 5], [2, 2], [3, 9]]))