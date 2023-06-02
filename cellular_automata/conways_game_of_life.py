import random , os , sys , time 


class cell:
    def __init__(self , i , j , size , body='.' , Alive=False):  
        #CREATING INDUVIDUL CELLS
        self.row = i 
        self.col = j 
        self.size = size
        self.body = body
        self.Alive = Alive
    
        #CONVERTING 2D INTO 1D TO NAME EACH CELL
        self.id = self.col + self.row * 10

    def update(self , Neibour):
        neibour_count = 0

        #CHECKING NEIBOUR
        if self.row > 0:
            if Neibour[self.row - 1][self.col].body == '*':
                neibour_count += 1
        if self.row < self.size -1:
            if Neibour[self.row + 1][self.col].body == '*':
                neibour_count += 1
        if self.col > 0:
            if Neibour[self.row][self.col- 1].body == '*':
                neibour_count += 1
        if self.col < self.size -1 :
            if Neibour[self.row][self.col + 1].body == '*':
                neibour_count += 1
        if self.row > 0 and self.col > 0:
            if Neibour[self.row - 1][self.col -1].body == '*':
                neibour_count += 1
        if self.row < self.size - 1 and self.col < self.size - 1:
            if Neibour[self.row + 1][self.col + 1].body == '*':
                neibour_count += 1
        if self.row < self.size - 1 and self.col > 0:
            if Neibour[self.row + 1][self.col - 1].body == '*':
                neibour_count += 1
        if self.row > 0 and self.col < self.size - 1:
            if Neibour[self.row - 1][self.col + 1].body == '*':
                neibour_count += 1

        #UPDATING STATE AS ALIVE OR NOT 
        if neibour_count < 2:
            self.Alive = False
        elif neibour_count > 3:
            self.Alive = False
        elif self.body == '*' and neibour_count == 2:
            self.Alive = True
        elif neibour_count == 3:
            self.Alive = True
        else:
            self.Alive = False
        
def display(life , size ):
    #RENDERING THE GRID WORLD
    for i in range(size):
        for j in range(size):
            if life[i][j].Alive:
                print(life[i][j].body, end=' ')
            else:
                print(life[i][j].body, end=' ')
        print()

def update(life , size):
    #UPDATING THE GRID WORLD
    for i in range(size):
        for j in range(size):
            life[i][j].update(life)

    for i in range(size):
        for j in range(size):            
            if life[i][j].Alive:
                life[i][j].body = '*'
            else:
                life[i][j].body = '.'

def main(size):
    #LIST CONTAINS ALL LIFE IN INTIIAL STATE
    life = [['*' for i in range(size)] for j in range(size)]
    for i in range(size):
        for j in range(size):
            rand_pop = random.randint(1 , 2)
            if rand_pop == 1:
                life[i][j] = cell(i , j , size , body='*' , Alive=True)
            else:
                life[i][j] = cell(i , j , size)

    while True:
        #LOOP TO RENDER THE GRID WORLD
        display(life , size)
        update(life , size)
        time.sleep(0.1)

        if sys.platform.startswith('win'):
            print("hi")
            os.system('cls')
        else:
            os.system('clear')
        print()
        print()


if __name__ == '__main__':
    grid_size = 10
    main(grid_size)
