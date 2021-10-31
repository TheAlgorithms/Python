'''
This programs prints an input 2D matrix
in zig-zag fashion.
'''

def zig_zag_pattern(matrix):
    #Storing dimensions of the input matrix
    rows=len(matrix)
    cols=len(matrix[0])
    result=[[] for i in range(rows+cols-1)]
 
    for i in range(rows):
        for j in range(cols):
            ind=i+j
            if(ind%2 ==0):
 
                #adding at beginning
                result[ind].insert(0,matrix[i][j])
            else:
 
                #adding at end
                result[ind].append(matrix[i][j])
                
    for i in result:
        for j in i:
            print(j,end=" ")
            
if __name__ == "__main__":
    
    zig_zag_pattern([
            [ 1, 2, 3,],
            [ 4, 5, 6 ],
            [ 7, 8, 9 ],
        ])
    
