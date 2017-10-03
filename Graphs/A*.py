
grid = [[0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],#0 are free path whereas 1's are obstacles
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 1, 0],
        [0, 0, 0, 0, 1, 0]]

'''
heuristic = [[9, 8, 7, 6, 5, 4],
             [8, 7, 6, 5, 4, 3],
             [7, 6, 5, 4, 3, 2],
             [6, 5, 4, 3, 2, 1],
             [5, 4, 3, 2, 1, 0]]'''

init = [0, 0]
goal = [len(grid)-1, len(grid[0])-1]
cost = 1

#the cost map which pushes the path closer to the goal
heuristic = [[0 for row in range(len(grid[0]))] for col in range(len(grid))]
for i in range(len(grid)):    
    for j in range(len(grid[0])):            
        heuristic[i][j] = abs(i - goal[0]) + abs(j - goal[1])
        if grid[i][j] == 1:
            heuristic[i][j] = 99 #added extra penalty in the heuristic map


#the actions we can take
delta = [[-1, 0 ], # go up
         [ 0, -1], # go left
         [ 1, 0 ], # go down
         [ 0, 1 ]] # go right


#function to search the path
def search(grid,init,goal,cost,heuristic):

    closed = [[0 for col in range(len(grid[0]))] for row in range(len(grid))]# the referrence grid
    closed[init[0]][init[1]] = 1
    action = [[0 for col in range(len(grid[0]))] for row in range(len(grid))]#the action grid

    x = init[0]
    y = init[1]
    g = 0
    f = g + heuristic[init[0]][init[0]]
    cell = [[f, g, x, y]]

    found = False  # flag that is set when search is complete
    resign = False # flag set if we can't find expand

    while not found and not resign:
        if len(cell) == 0:
            resign = True
            return "FAIL"
        else:
            cell.sort()#to choose the least costliest action so as to move closer to the goal
            cell.reverse()
            next = cell.pop()
            x = next[2]
            y = next[3]
            g = next[1]
            f = next[0]

            
            if x == goal[0] and y == goal[1]:
                found = True
            else:
                for i in range(len(delta)):#to try out different valid actions
                    x2 = x + delta[i][0]
                    y2 = y + delta[i][1]
                    if x2 >= 0 and x2 < len(grid) and y2 >=0 and y2 < len(grid[0]):
                        if closed[x2][y2] == 0 and grid[x2][y2] == 0:
                            g2 = g + cost
                            f2 = g2 + heuristic[x2][y2]
                            cell.append([f2, g2, x2, y2])
                            closed[x2][y2] = 1
                            action[x2][y2] = i
    invpath = []
    x = goal[0]
    y = goal[1]
    invpath.append([x, y])#we get the reverse path from here
    while x != init[0] or y != init[1]:
    	x2 = x - delta[action[x][y]][0]
        y2 = y - delta[action[x][y]][1]
        x = x2
        y = y2
        invpath.append([x, y])

    path = []
    for i in range(len(invpath)):
    	path.append(invpath[len(invpath) - 1 - i])
    print "ACTION MAP"
    for i in range(len(action)):
        print action[i]
                  
    return path
    
a = search(grid,init,goal,cost,heuristic)
for i in range(len(a)):
	print a[i] 

