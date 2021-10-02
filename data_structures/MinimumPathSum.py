

def findPath( arr , rows, cols):
    #iterating the whole grid
    
    """
    since only two movements are allowed right and down. To arrive at a particular cell
    we can either comes from left cell(by taking right step) or
    from top cell (by taking  down step)
    """
    for r in range(rows):
        for c in range(cols):
            option1, option2 =None, None
            
            #option1 is when minimum path sum to arr[r][c] comes from left
            if(c-1>=0):
                option1= arr[r][c-1]
            #option2 is when minimum path sum to arr[r][c] comes from top
            if(r-1>=0):
                option2= arr[r-1][c]
                
            if(option1==None and option1==None):
                continue
            if(option1!=None and option2!=None):
                arr[r][c]= min(option1, option2) +arr[r][c]
            elif(option1!= None):
                arr[r][c]= option1+ arr[r][c]
            else:
                arr[r][c]= option2+ arr[r][c]
        
    return(arr[rows-1][cols-1])

#defining the grid matrix
grid= [[1,3,1],[1,5,1],[4,2,1]]
#number of rows
rows=len(grid)
#number of columns
cols=len(grid[0])

if(rows==0 or cols==0):
  print("please give a valid input")
else:
  print( findPath( grid, rows, cols));
  
  
"""
Time complexity for this algorithm is O(n^2) , since we are traversing the grid.
Space complexity is O(1), since we are not using any extra space.
"""
            
