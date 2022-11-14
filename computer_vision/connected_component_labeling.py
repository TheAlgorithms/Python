# """
#   Connected-Component Labeling
#
#   Source:
#   https://en.wikipedia.org/wiki/Connected-component_labeling
#
#   Basically, there's two versions of CCL two-pass algorithm:
#   4-connectivity and 8-connectivity.
#   4-connectivity means that only horizontal and vertical neighbours
#   are considered, while 8-connectivity means that diagonal neighbours
#   are also considered.
# """


def connected_component_labeling_8(matrix: list) -> list:
    """
    Connected Component Labeling algorithm (8-connectivity version)
    Takes a matrix of binary values and returns a matrix of labels,
    where each connected component is assigned a unique label.

    args:
        matrix: 2D list of 0s and 1s

    returns:
        2D list of labels

    >>> connected_component_labeling_8([[1, 0, 0, 1],
    ...                                 [1, 0, 0, 1],
    ...                                 [0, 0, 1, 0],
    ...                                 [0, 1, 1, 0]])
    [[1, 0, 0, 2], [1, 0, 0, 2], [0, 0, 2, 0], [0, 2, 2, 0]]
    >>> connected_component_labeling_8([[0, 1, 0, 1],
    ...                                 [1, 1, 0, 0],
    ...                                 [0, 0, 1, 1],
    ...                                 [1, 0, 1, 0]])
    [[0, 1, 0, 2], [1, 1, 0, 0], [0, 0, 1, 1], [3, 0, 1, 0]]
    >>> connected_component_labeling_4([])
    Traceback (most recent call last):
        ...
    ValueError: Matrix must be non-empty
    >>> connected_component_labeling_4([[1, 1, 1], [1, 0], [1, 0, 1]])
    Traceback (most recent call last):
        ...
    ValueError: Matrix must be rectangular
    >>> connected_component_labeling_4([[1, 0, 0], [1, 0, 2], [1, 0, 1]])
    Traceback (most recent call last):
        ...
    ValueError: Matrix must contain only 0s and 1s
    """

    if len(matrix) == 0 or len(matrix[0]) == 0:
        raise ValueError("Matrix must be non-empty")
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise ValueError("Matrix must be rectangular")
    if not all(all(x in (0, 1) for x in row) for row in matrix):
        raise ValueError("Matrix must contain only 0s and 1s")

    row_len = len(matrix[0])

    # add padding
    padded_matrix = (
        [[0] * (row_len + 2)]
        + [[0] + row + [0] for row in matrix]
        + [[0] * (row_len + 2)]
    )

    # after the first traverse, we might label some elements incorrectly.
    # when we spot incorrect labeling, we add neighbours label as a key
    # and the element label as a value
    mapping: dict = {}

    next_label = 1

    # first traverse
    for i in range(1, len(padded_matrix) - 1):
        for j in range(1, row_len + 1):

            if padded_matrix[i][j] == 1:

                neighbours = [
                    padded_matrix[i - 1][j - 1],
                    padded_matrix[i - 1][j],
                    padded_matrix[i - 1][j + 1],
                    padded_matrix[i][j - 1],
                ]

                if any(neighbours):

                    min_label = min([v for v in neighbours if v > 0])
                    padded_matrix[i][j] = min_label

                    for label in neighbours:
                        # if any of the neighbors appears to have label \
                        # greater than current element - add it's \
                        # label to mapping
                        if label > min_label:
                            if label not in mapping:
                                mapping[label] = set()
                            mapping[label].add(min_label)

                else:
                    padded_matrix[i][j] = next_label
                    next_label += 1

    # "unpad" the matrix
    matrix = [row[1:-1] for row in padded_matrix[1:-1]]

    # restructure the mapping, so that:
    # 3: (2, 1)         3: (2, 1)
    # 6: (3)        ->  6: (3, 1)
    #                   2: (1,)
    for key in sorted(mapping.keys()):
        adj_labels = mapping[key]
        min_label = min(adj_labels)
        for adj_label in adj_labels:
            if adj_label not in mapping:
                mapping[adj_label] = set()
            mapping[adj_label].add(min_label)

    # apply the mapping
    for i in range(len(matrix)):
        for j in range(row_len):
            if matrix[i][j] in mapping:
                matrix[i][j] = min(mapping[matrix[i][j]])

    return matrix


def connected_component_labeling_4(matrix: list) -> list:
    """
    Connected Component Labeling algorithm (4-connectivity version)
    Takes a matrix of binary values and returns a matrix of labels,
    where each connected component is assigned a unique label.


    args:
        matrix: 2D list of 0s and 1s

    returns:
        2D list of labels

    >>> connected_component_labeling_4([[1, 0, 0, 1],
    ...                                 [1, 0, 0, 1],
    ...                                 [0, 0, 1, 0],
    ...                                 [0, 1, 1, 0]])
    [[1, 0, 0, 2], [1, 0, 0, 2], [0, 0, 3, 0], [0, 3, 3, 0]]
    >>> connected_component_labeling_4([[0, 1, 0, 1],
    ...                                 [1, 1, 0, 0],
    ...                                 [0, 0, 1, 1],
    ...                                 [1, 0, 1, 0]])
    [[0, 1, 0, 2], [1, 1, 0, 0], [0, 0, 4, 4], [5, 0, 4, 0]]
    >>> connected_component_labeling_4([])
    Traceback (most recent call last):
        ...
    ValueError: Matrix must be non-empty
    >>> connected_component_labeling_4([[1, 1, 1], [1, 0], [1, 0, 1]])
    Traceback (most recent call last):
        ...
    ValueError: Matrix must be rectangular
    >>> connected_component_labeling_4([[1, 0, 0], [1, 0, 2], [1, 0, 1]])
    Traceback (most recent call last):
        ...
    ValueError: Matrix must contain only 0s and 1s
    """

    if len(matrix) == 0 or len(matrix[0]) == 0:
        raise ValueError("Matrix must be non-empty")
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise ValueError("Matrix must be rectangular")
    if not all(all(x in (0, 1) for x in row) for row in matrix):
        raise ValueError("Matrix must contain only 0s and 1s")

    row_len = len(matrix[0])

    # add padding
    padded_matrix = (
        [[0] * (row_len + 2)]
        + [[0] + row + [0] for row in matrix]
        + [[0] * (row_len + 2)]
    )

    # after the first traverse, we might label some elements incorrectly.
    # when we spot incorrect labeling, we add neighbours label as a key
    # and the element label as a value
    mapping: dict = {}

    next_label = 1

    # first traverse
    for i in range(1, len(padded_matrix) - 1):
        for j in range(1, row_len + 1):

            if padded_matrix[i][j] == 1:

                neighbours = [padded_matrix[i - 1][j], padded_matrix[i][j - 1]]

                if any(neighbours):

                    min_label = min([v for v in neighbours if v > 0])
                    padded_matrix[i][j] = min_label

                    for label in neighbours:
                        # if any of the neighbors appears to have label \
                        # greater than current element - add it's \
                        # label to mapping
                        if label > min_label:
                            if label not in mapping:
                                mapping[label] = set()
                            mapping[label].add(min_label)

                else:
                    padded_matrix[i][j] = next_label
                    next_label += 1

    # "unpad" the matrix
    matrix = [row[1:-1] for row in padded_matrix[1:-1]]

    # restructure the mapping, so that:
    # 3: (2, 1)         3: (2, 1)
    # 6: (3)        ->  6: (3, 1)
    #                   2: (1,)
    for key in sorted(mapping.keys()):
        adj_labels = mapping[key]
        min_label = min(adj_labels)
        for adj_label in adj_labels:
            if adj_label not in mapping:
                mapping[adj_label] = set()
            mapping[adj_label].add(min_label)

    # apply the mapping
    for i in range(len(matrix)):
        for j in range(row_len):
            if matrix[i][j] in mapping:
                matrix[i][j] = min(mapping[matrix[i][j]])

    return matrix


if __name__ == "__main__":
    import doctest

    doctest.testmod()
