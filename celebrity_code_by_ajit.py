# Python3 program to find celebrity
 
# Max # of persons in the party
N = 8
 
# Person with 2 is celebrity
MATRIX = [ [ 0, 0, 1, 0 ],
           [ 0, 0, 1, 0 ],
           [ 0, 0, 0, 0 ],
           [ 0, 0, 1, 0 ] ]
            
def knows(a, b):
     
  return MATRIX[a][b]
 
def findCelebrity(n):
     
    # The graph needs not be constructed
    # as the edges can be found by
    # using knows function
       
    # degree array;
    indegree = [0 for x in range(n)]
    outdegree = [0 for x in range(n)]
       
    # Query for all edges
    for i in range(n):
        for j in range(n):
            x = knows(i, j)
               
            # Set the degrees
            outdegree[i] += x
            indegree[j] += x
       
    # Find a person with indegree n-1
    # and out degree 0
    for i in range(n):
        if (indegree[i] == n - 1 and
           outdegree[i] == 0):
            return i
             
    return -1
     
# Driver code   
if __name__ == '__main__':
     
    n = 4
    id_ = findCelebrity(n)
     
    if id_ == -1:
        print("No celebrity")
    else:
        print("Celebrity ID", id_)
