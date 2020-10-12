#
#      question link - https://projecteuler.net/problem=81
#
#    Find the minimal path sum from the top left to the bottom right by
#    only moving right and down in matrix.txt 
#
#
#



import os



def solution() -> int :
    matrix=[]	

    # following line of codes are used to input data from a txt file
    #script_dir=os.path.abspath(os.path.dirname(__file__))
    #p081_matrix=os.path.join(script_dir,"p081_matrix.txt")
    #with open("p081_matrix.txt","r") as file_hand:
        #for line in file_hand:
            #vector=list(map(int,line.split(',')))
            #matrix.append(vector)
	
	
    row=len(matrix)
    col=len(matrix[0])

    for i in range(1, col):
	       matrix[0][i] += matrix[0][i-1]

    for i in range(1, row):
	       matrix[i][0] += matrix[i-1][0]

    for i in range(1, row):
	       for j in range(1, col):
	              matrix[i][j] += min(matrix[i-1][j], matrix[i][j-1])

    return matrix[row-1][col-1]









if __name__ == "__main__":
    print(solution())
