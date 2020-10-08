"""
Given a partially or empty grid, attempts to solve (n^2)*(n^2) sudoku,
where n is the box size
Eg:
sudoku 4*4              sudoku 9*9
box_size = n = 2        box_size = n = 3
+-------+-------+       +----------+----------+----------+
| 01 02 | 03 04 |       | 01 02 03 | 04 05 08 | 09 06 07 |
| 03 04 | 01 02 |       | 04 05 08 | 06 07 09 | 01 02 03 |
+-------+-------+       | 09 06 07 | 01 02 03 | 08 04 05 |
| 02 01 | 04 03 |       +----------+----------+----------+
| 04 03 | 02 01 |       | 02 01 09 | 08 03 04 | 05 07 06 |
+-------+-------+       | 03 08 04 | 05 06 07 | 02 01 09 |
                        | 05 07 06 | 09 01 02 | 03 08 04 |
                        +----------+----------+----------+
                        | 08 09 01 | 03 04 06 | 07 05 02 |
                        | 06 03 02 | 07 08 05 | 04 09 01 |
sudoku 16*16            | 07 04 05 | 02 09 01 | 06 03 08 |
box_size = n = 4        +----------+----------+----------+
+-------------+-------------+-------------+-------------+
| 01 02 03 04 | 05 06 07 08 | 09 10 11 12 | 16 13 14 15 |
| 05 06 07 08 | 01 02 03 04 | 16 13 14 15 | 09 10 11 12 |
| 09 10 11 12 | 16 13 14 15 | 01 02 03 04 | 08 05 06 07 |
| 16 13 14 15 | 09 10 11 12 | 08 05 06 07 | 01 02 03 04 |
+-------------+-------------+-------------+-------------+
| 02 01 04 03 | 06 05 08 07 | 10 09 16 11 | 12 14 15 13 |
| 06 05 08 07 | 02 01 04 03 | 12 14 15 13 | 10 16 09 11 |
| 10 09 16 11 | 12 14 15 13 | 02 01 08 03 | 04 06 07 05 |
| 12 14 15 13 | 10 16 09 11 | 04 06 07 05 | 02 08 01 03 |
+-------------+-------------+-------------+-------------+
| 03 04 01 02 | 07 08 05 06 | 11 16 09 10 | 13 15 12 14 |
| 07 08 05 06 | 03 04 01 02 | 13 15 12 14 | 11 09 16 10 |
| 11 16 09 10 | 13 15 12 14 | 03 08 01 02 | 05 07 04 06 |
| 13 15 12 14 | 11 09 16 10 | 05 07 04 06 | 03 01 08 02 |
+-------------+-------------+-------------+-------------+
| 08 11 02 16 | 04 07 06 05 | 14 03 10 01 | 15 12 13 09 |
| 04 07 10 01 | 14 11 02 16 | 15 12 13 09 | 06 03 05 08 |
| 14 03 13 09 | 15 12 10 01 | 06 11 05 08 | 07 04 02 16 |
| 15 12 06 05 | 08 03 13 09 | 07 04 02 16 | 14 11 10 01 |
+-------------+-------------+-------------+-------------+
"""

class Sudoku:
    '''
    Class object for sudoku
    element 0 represents an empty element
    '''
    def __init__(self,box_size:int):
        '''
        initialize grid and box
        '''
        self.box_size = box_size
        self.grid_size = box_size**2
        self.grid = []
        self.box = dict()
        for r in range(self.grid_size):
            self.grid.append([])
            for c in range(self.grid_size):
                self.grid[-1].append(0)
                box_number = self.box_mapper(r,c)
                if box_number not in self.box:
                    self.box[box_number]={0}

    def load_grid(self,arr:list) -> None:
        '''
        Load the values from arr into the grid
        '''
        if len(arr)!=self.grid_size:
            raise ValueError("Input grid size do not match")

        for r in range(self.grid_size):
            if len(arr[r])!=self.grid_size:
                raise ValueError("Input grid size do not match")

            for c in range(self.grid_size):
                self.add_element(arr[r][c],r,c)

    def box_mapper(self,row:int, column:int) -> int:
        '''
        Maps row,column into their respective boxes
        '''
        return (row//self.box_size)*10 + (column//self.box_size)

    def possible_values(self,row:int,column:int) -> set:
        '''
        Gets the possible values at row,column
        '''
        box_number = self.box_mapper(row,column)

        possible_elements = set(range(1,(self.grid_size)+1))
        row_elements = set(self.grid[row])
        column_elements = set([self.grid[i][column] for i in range(self.grid_size)])
        box_elements = self.box[box_number]

        return possible_elements - box_elements.union(row_elements,column_elements)

    def next_empty(self, row:int, column:int) -> tuple:
        '''
        Returns the position of next empty element 0
        if there exist a empty element
            returns (True,row,column)
        else
            returns (False,-1,-1)
        '''
        (r,c) = (row, column)
        while r<self.grid_size:
            while c<self.grid_size:
                if self.grid[r][c]==0:
                    return (True,r,c)
                c+=1
            c=0
            r+=1
        return (False,-1,-1)

    def add_element(self,element:int,row:int,column:int) -> None:
        '''
        Adds element to grid[row][column]
        '''
        self.grid[row][column]=element
        box_number = self.box_mapper(row,column)
        self.box[box_number].add(element)

    def remove_element(self,row:int,column:int) -> None:
        '''
        Removes element at grid[row][column]
        '''
        box_number = self.box_mapper(row,column)
        element = self.grid[row][column]
        self.box[box_number].remove(element)
        self.grid[row][column]=0
        self.box[box_number].add(0)

    def solver(self,row:int,column:int) -> bool:
        '''
        solve the next empty element from row,column
        if the grid is complete
            return true
        else
            return false
        '''
        (status,new_row,new_column) = self.next_empty(row,column)
        if status==False:
            return True

        for element in self.possible_values(new_row,new_column):
            self.add_element(element,new_row,new_column)
            status = self.solver(new_row,new_column)
            if status == True:
                return True
            self.remove_element(new_row,new_column)
        return False

    def solve(self) -> bool:
        '''
        Invoke solver and return true if the grid is solved
        else return False
        '''
        return self.solver(0,0)

    def __str__(self):
        string = ''
        row_completer = ('+-' + '---'*self.box_size)*self.box_size + '+'
        box_edge = [x for x in range(self.grid_size) if x%self.box_size == self.box_size-1]

        string +=row_completer+'\n'
        for r in range(self.grid_size):
            string += '| '
            for c in range(self.grid_size):
                string += "%02d "%(self.grid[r][c])
                if c in box_edge:
                    string += "| "
            string+='\n'
            if r in box_edge:
                string += row_completer + '\n'

        return string


if __name__ == "__main__":

    accept_from_user = False
    if accept_from_user:
        box_size = int(input("Enter the box size: "))
        question_grid = []
        i=1
        print("Use zero to represent empty value")
        while(i<=box_size**2):
            row_values = list(map(int,input(f"Enter the row {i} : ")))
            if len(row_values)!=box_size**2:
                print(f"Row length should be {box_size**2}")
                continue
            quesiton_grid.append(row_values)
            i+=1
    else:
        box_size = 3
        question_grid = [
            [ 1, 0, 0, 0, 0, 7, 0, 9, 0 ],
            [ 0, 3, 0, 0, 2, 0, 0, 0, 8 ],
            [ 0, 0, 9, 6, 0, 0, 5, 0, 0 ],
            [ 0, 0, 5, 3, 0, 0, 9, 0, 0 ],
            [ 0, 1, 0, 0, 8, 0, 0, 0, 2 ],
            [ 6, 0, 0, 0, 0, 4, 0, 0, 0 ],
            [ 3, 0, 0, 0, 0, 0, 0, 1, 0 ],
            [ 0, 4, 0, 0, 0, 0, 0, 0, 7 ],
            [ 0, 0, 7, 0, 0, 0, 3, 0, 0 ]
        ]
        question = Sudoku(box_size)
        question.load_grid(question_grid)

    print("The initial question is ")
    print(question)
    print("\nSolving...",end='')

    if (question.solve()== True):
        print("Success. The answer is:")
        print(question)
    else:
        print("Failed. Could not find a possible solution")
