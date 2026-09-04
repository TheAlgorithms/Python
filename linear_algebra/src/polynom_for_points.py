def points_to_polynomial(coordinates: list[list[int]]) -> str:
    """
    coordinates is a two dimensional matrix: [[x, y], [x, y], ...]
    number of points you want to use

    >>> points_to_polynomial([])
    Traceback (most recent call last):
        ...
    ValueError: The program cannot work out a fitting polynomial.
    >>> points_to_polynomial([[]])
    Traceback (most recent call last):
        ...
    ValueError: The program cannot work out a fitting polynomial.
    >>> points_to_polynomial([[1, 0], [2, 0], [3, 0]])
    'f(x)=x^2*0.0+x^1*-0.0+x^0*0.0'
    >>> points_to_polynomial([[1, 1], [2, 1], [3, 1]])
    'f(x)=x^2*0.0+x^1*-0.0+x^0*1.0'
    >>> points_to_polynomial([[1, 3], [2, 3], [3, 3]])
    'f(x)=x^2*0.0+x^1*-0.0+x^0*3.0'
    >>> points_to_polynomial([[1, 1], [2, 2], [3, 3]])
    'f(x)=x^2*0.0+x^1*1.0+x^0*0.0'
    >>> points_to_polynomial([[1, 1], [2, 4], [3, 9]])
    'f(x)=x^2*1.0+x^1*-0.0+x^0*0.0'
    >>> points_to_polynomial([[1, 3], [2, 6], [3, 11]])
    'f(x)=x^2*1.0+x^1*-0.0+x^0*2.0'
    >>> points_to_polynomial([[1, -3], [2, -6], [3, -11]])
    'f(x)=x^2*-1.0+x^1*-0.0+x^0*-2.0'
    >>> points_to_polynomial([[1, 5], [2, 2], [3, 9]])
    'f(x)=x^2*5.0+x^1*-18.0+x^0*18.0'
    >>> points_to_polynomial([[1, 1], [1, 2], [1, 3]])
    'x=1'
    >>> points_to_polynomial([[1, 1], [2, 2], [2, 2]])
    Traceback (most recent call last):
        ...
    ValueError: The program cannot work out a fitting polynomial.
    >>> points_to_polynomial([[0, 1], [1, 2], [2, 5]])
    'f(x)=x^2*1.0+x^1*0.0+x^0*1.0'
    >>> points_to_polynomial([[1, 2], [0, 1], [2, 5]])
    Traceback (most recent call last):
        ...
    ValueError: The program cannot work out a fitting polynomial.
    """
    if len(coordinates) == 0 or not all(len(pair) == 2 for pair in coordinates):
        raise ValueError("The program cannot work out a fitting polynomial.")

    if len({tuple(pair) for pair in coordinates}) != len(coordinates):
        raise ValueError("The program cannot work out a fitting polynomial.")

    set_x = {x for x, _ in coordinates}
    if len(set_x) == 1:
        return f"x={coordinates[0][0]}"

    if len(set_x) != len(coordinates):
        raise ValueError("The program cannot work out a fitting polynomial.")

    x = len(coordinates)

    # put the x and x to the power values in a matrix
    matrix: list[list[float]] = [
        [
            coordinates[count_of_line][0] ** (x - (count_in_line + 1))
            for count_in_line in range(x)
        ]
        for count_of_line in range(x)
    ]

    # put the y values into a vector
    vector: list[float] = [coordinates[count_of_line][1] for count_of_line in range(x)]

    for count in range(x):
        for number in range(x):
            if count == number:
                continue
            if matrix[count][count] == 0:
                # Diagonal element is zero which results in zero-division-error
                # as per bug #14817.
                # Using partial pivoting: before each elimination step, swap in a row
                # whose matrix[r][count] is non-zero (largest magnitude).
                # This removes the zero-pivot crash and improves numerical stability.

                swap_row_index = count
                max_col_value = matrix[count][count]
                # Search downwards from current row as earlier rows are
                # already processed.
                for row in range(count, x):
                    if matrix[row][count] > max_col_value:
                        swap_row_index = row
                        max_col_value = matrix[row][count]

                # If maximum value found in the current column is
                # again zero, raise error.
                if int(max_col_value) == 0:
                    raise ValueError(
                        "The program cannot work out a fitting polynomial."
                    )

                # Swap pivot row with row index found in previous step,
                # with maximum value present in matrix[r][count] column.
                matrix[count], matrix[swap_row_index] = (
                    matrix[swap_row_index],
                    matrix[count],
                )
                vector[count], vector[swap_row_index] = (
                    vector[swap_row_index],
                    vector[count],
                )
                # Continue to perform scaling row reduction.

            fraction = matrix[number][count] / matrix[count][count]
            for counting_columns, item in enumerate(matrix[count]):
                # manipulating all the values in the matrix
                matrix[number][counting_columns] -= item * fraction
            # manipulating the values in the vector
            vector[number] -= vector[count] * fraction

    # make solutions
    solution: list[str] = [
        str(vector[count] / matrix[count][count]) for count in range(x)
    ]

    solved = "f(x)="

    for count in range(x):
        remove_e: list[str] = solution[count].split("E")
        if len(remove_e) > 1:
            solution[count] = f"{remove_e[0]}*10^{remove_e[1]}"
        solved += f"x^{x - (count + 1)}*{solution[count]}"
        if count + 1 != x:
            solved += "+"

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

    # Added under bug fix: #14817
    print(points_to_polynomial([[0, 1], [1, 2], [2, 5]]))
    print(points_to_polynomial([[1, 2], [0, 1], [2, 5]]))
