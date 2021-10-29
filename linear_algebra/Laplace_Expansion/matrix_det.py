import math

class vector():
    def __init__(self, numbers):
        self.content = list(numbers)
        self.length = len(self.content)
    
    def scalar_multiplication(self, scalar):
        for i in range(self.length):
            self.content[i] = self.content[i] * scalar

class matrix(vector):
    def __init__(self, rows):
        self.rows = list(rows)

        self.width = self.rows[0].length
        self.height = len(self.rows)

    # takes an indice and deletes that row of the indice
    def delete_row(self, index):
        del self.rows[index]
    
    # delete a column of the matrix
    def delete_col(self, index):
        for row in range(self.height):
            del self.rows[row].content[index]
    

    def sum_row(self, factor, rowtoadd, row):
        for i in range(self.width):
            self.rows[row].content[i] += factor * self.rows[rowtoadd].content[i]
            



def determinant(matrix):

    # the recursive part of the determinant
    det_rec_element = 0.0

    # make the row_clear index global
    row_clear_ind = 0

    # this is the row we use for clearing out the others
    clearing_row_ind = 0

    # For a 1x1 matrix, the determinant is just the entry of the matrix
    if matrix.width == 1 and matrix.height == 1:
        return matrix.rows[0].content[0] 

    if matrix.width != matrix.height:
        raise ValueError('matrix not square -> no determinant')

    for row in range(matrix.height):

        if matrix.rows[row].content[0] != 0.0:
            
            # if this is the first line we find with no 0 as its first element, then make it clearing_row
            if clearing_row_ind == 0:
                clearing_row_ind = row

                if matrix.rows[row].content[0] == 1.0:
                    break # means we already found a matrix element we can clear out the rest with

                else:
                    # we clear the row by multiplying it with 1/diagonal element of its row, so we get a 11111111... diagonal
                    matrix.rows[row].scalar_multiplication(1/(matrix.rows[row].content[row]))
                    continue

        # if the first column is a 0 column, then we don't have a quadratic matrix anymore
        if row == matrix.height and matrix.rows[row].content[row] == 0.0:
            return 0
             
    for row_to_clear_ind in range(0, matrix.height):

        if row_to_clear_ind == clearing_row_ind:
            # we don't want to clear the row we are clearing with obviously :D
            continue

        else:
            # subtract the negative of the clearing row so eg
            '''
            8 16 0   0 0 0
            1 2 0 -> 1 2 0
            3 6 0    0 0 0
            '''
            # clear the row by subtracting the negative multiple of the first clearrow indice times the row that we re clearing with from the clearrow
            clear_row_first = matrix.rows[row_to_clear_ind].content[0]
            matrix.sum_row(-clear_row_first, clearing_row_ind, row_to_clear_ind)

    # just a part of the Laplace Expansion Method           
    det_element = matrix.rows[clearing_row_ind].content[clearing_row_ind]

    if clearing_row_ind % 2 != 0:
        det_element *= -1

    # Erase the row of the element in which you started and also erase the column
    new_matrix = matrix

    new_matrix.delete_col(0)

    new_matrix.width -= 1

    new_matrix.delete_row(row_clear_ind)

    new_matrix.height -= 1

    # recursively call the funciton on the (n-1,n-1) matrix
    return det_element * determinant(new_matrix)
                    

if __name__ == '__main__':
    numbers1 = [1.0, 2.0]
    numbers2 = [3.0, 4.0]

    vector1 = vector(numbers1)
    vector2 = vector(numbers2)   

    vectors = [vector1, vector2]
    matrix1 = matrix(vectors) 

    print(determinant(matrix1))  





        