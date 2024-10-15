def find_peak_util(matrix, left, right, row_count):
    mid_col = (left + right) // 2
    
    max_row_index = 0
    for i in range(row_count):
        if matrix[i][mid_col] > matrix[max_row_index][mid_col]:
            max_row_index = i
            

    if (mid_col == 0 or matrix[max_row_index][mid_col] >= matrix[max_row_index][mid_col - 1]) and \
       (mid_col == len(matrix[0]) - 1 or matrix[max_row_index][mid_col] >= matrix[max_row_index][mid_col + 1]):
        return matrix[max_row_index][mid_col]
    

    if mid_col > 0 and matrix[max_row_index][mid_col - 1] > matrix[max_row_index][mid_col]:
        return find_peak_util(matrix, left, mid_col - 1, row_count)

    return find_peak_util(matrix, mid_col + 1, right, row_count)

def find_peak(matrix):
    if not matrix or not matrix[0]:
        return None
    return find_peak_util(matrix, 0, len(matrix[0]) - 1, len(matrix))

matrix = [
    [10, 8, 10, 10],
    [14, 13, 12, 11],
    [15, 9, 11, 21],
    [16, 17, 19, 20]
]

peak = find_peak(matrix)
print(f"Peak element is: {peak}")
