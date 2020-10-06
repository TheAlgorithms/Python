#Priyanka Gupta
# 8 puzzle--->A* search algo

import copy
import heapq

live=list()
used=set()

col=[-1,1,0,0]
row=[0,0,-1,1]

# to check possible to go this state
def isSafe(x,y):
  if x>=0 and x<3 and y>=0 and y<3:
    return True
  return False

# calculate heuristic cost
def heuristic(a,b):
  count=0
  for i in range(3):
    for j in range(3):
      if a[i][j] == b[i][j]:
        count=count+1
  return count

# print final matrix
def printMat(mat):
  for each in mat:
    print(each)

# main function
def solve(initial,final,x,y):

  fn=heuristic(initial,final)
  gn=1
  nextN = (fn,-1,initial,x,y,gn)
  used.add(str(initial))
  live.append((nextN, [str(initial)])) 
  heapq._heapify_max(live)

  while len(live): 
    # maintaining open queue
    state, state_seq = heapq._heappop_max(live) 
    fn,parent,arr,x,y,gn=state
    if heuristic(arr,final)==9: 
        print('State traversed:\n')
        for idx,state in enumerate(state_seq):
          print('State ',str(idx),'\n',state,'\n')
        print('Solution: ')
        printMat(arr)
        print('\nTotal levels travelled: ',gn-1)
        return

    # traversing all paths
    for i in range(4):
      nextX = x+row[i]
      nextY = y+col[i]
      if isSafe(nextX, nextY):
        nextS = copy.deepcopy(arr)
        new_state_seq = copy.deepcopy(state_seq)
        nextS[x][y],nextS[nextX][nextY]=nextS[nextX][nextY],nextS[x][y]
        # calculating fn=hn+gn
        fn=heuristic(nextS,final)+gn
        # updating gn inside the tuple
        nextN = (fn,arr,nextS,nextX,nextY,gn+1)
        new_state_seq.append(str(nextS))
        # checking nextS in used
        if str(nextS) not in used:
          used.add(str(nextS))
          heapq.heappush(live,(nextN,new_state_seq))
     
# input parameters
mat=[[2,0,3],[1,8,4],[7,6,5]]
final=[[1,2,3],[8,0,4],[7,6,5]]
x=0
y=1
solve(mat,final,x,y)
