'''
This function searches through list(s) of items
for a specific item and returns the last occurrence 
of that item's location as a tuple.

'''

def last_occurrence(x_list,x):
  
    for i in range(len(x_list)-1,-1,-1):
        
        for j in range(len(x_list[i])-1,-1,-1):
            
            if x_list[i][j] == x:
                
                return (i, j)
                
last_occurrence([[2,3,1,5],[8,2,2],[9,0,2]], 2) # will return (2,2)
last_occurrence([[2,3,1,5],[8,1,2],[9,0,0]], 1) # will return (1,1)
last_occurrence([[2,3,1,5],[8,1,2],[9,0,0]], 3) # will return (0,1)
