################################################
# N-Puzzle Solution                            #
# Artificial Intelligence Assignment - 1       #
# M.Tech CSE 24'                               #
                                               #
# Group Details                                #
# Name : Krishna Kant Verma (2211CS19)         #
# Name : Gourab Chatterji (2211CS08)           #
# Name : Aditi Marathe (2211CS01)              #
################################################

# Importing Queue having Stack Property for DFS
from queue import LifoQueue
#importing Queue 
from queue import Queue
#importing copy libarary for making deep copy
import copy
# importing time module
import time
#importing random function
import random

# declaring global variable N 
global N

# function that swaps upward element 
def moveUpward(currState,x,y):
    currState[x][y],currState[x-1][y] = currState[x-1][y],0
    return currState
# function that swaps left element 
def moveLeft(currState,x,y):
    currState[x][y],currState[x][y-1] = currState[x][y-1],0
    return currState
# function that swaps right element 
def moveRight(currState,x,y):
    currState[x][y],currState[x][y+1] = currState[x][y+1],0
    return currState
# function that swaps downward element 
def moveDownward(currState,x,y):
    currState[x][y],currState[x+1][y] = currState[x+1][y],0
    return currState

# Searching of blank location in grid 
def searchBlankLocation(Puzzle):
    for i in range(0,N):
        for j in range(0,N):
            if(Puzzle[i][j]==0):
                return i,j


# BFS Implementation 
def startBFS(Puzzle,final):
    steps=0
    q=Queue()
    q.put(Puzzle)

    # visited array for tracking states that are already explored 
    visited={}
    Puzzle=tuple(map(tuple,Puzzle))
    visited[Puzzle]=1

    while not q.empty():
        currState=q.get()
            
        if currState==final:
            return steps

        # finding the blank location    
        x,y=searchBlankLocation(currState)

        #up left right down movement of blank space

        #for up movement
        if x!=0:
            m=copy.deepcopy(currState)
            m=moveUpward(m,x,y)
            newpuzzle=tuple(map(tuple,m))

            if m==final:
                for i in range(0,N):
                    print(currState[i])  
                print("") 
                steps = steps + 1
                return steps

            if newpuzzle not in visited.keys() and isPossible(m):
                #printing current state
                for i in range(0,N):
                    print(currState[i])   
                print("") 
                steps = steps + 1
                visited[newpuzzle]=1
                q.put(m)      

        #for left movement
        if y!=0:
            m=copy.deepcopy(currState)
            m=moveLeft(m,x,y)
            newpuzzle=tuple(map(tuple,m))

            if m==final:
                for i in range(0,N):
                    print(currState[i])  
                print("") 
                steps = steps + 1
                return steps

            if newpuzzle not in visited.keys() and isPossible(m):
                #printing current state
                for i in range(0,N):
                    print(currState[i])   
                print("") 
                steps = steps + 1
                visited[newpuzzle]=1
                q.put(m)

        #for right movement
        if y<N-1:
            m=copy.deepcopy(currState)
            m=moveRight(m,x,y)
            newpuzzle=tuple(map(tuple,m))

            if m==final:
                for i in range(0,N):
                    print(currState[i])  
                print("") 
                steps = steps + 1
                return steps

            if newpuzzle not in visited.keys() and isPossible(m):
                #printing current state
                for i in range(0,N):
                    print(currState[i])   
                print("") 
                steps = steps + 1
                visited[newpuzzle]=1
                q.put(m)

        #for down movement
        if x<N-1:
            m=copy.deepcopy(currState)
            m=moveDownward(m,x,y)
            newpuzzle=tuple(map(tuple,m))

            if m==final:
                for i in range(0,N):
                    print(currState[i])  
                print("") 
                steps = steps + 1
                return steps

            if newpuzzle not in visited.keys() and isPossible(m):
                #printing current state
                for i in range(0,N):
                    print(currState[i])   
                print("") 
                steps = steps + 1
                visited[newpuzzle]=1
                q.put(m)
      
    return

# DFS Implementation 
def startDFS(Puzzle,final):
    steps=0
    s=LifoQueue()
    s.put(Puzzle)
    Puzzle=tuple(map(tuple,Puzzle))


    # tracking explored states
    visited={}
    visited[Puzzle]=1
    #implementing stack property using while loop 
    while not s.empty():
        currState=s.get()
        
        #printing current state
        for i in range(0,N):
            print(currState[i])   
        print("")

        if currState==final:
            return steps

        steps=steps+1

        # finding position of blank space 
        x,y=searchBlankLocation(currState)

        # Actual Ordering of movement of elements is Up Left Right Downward   

        #for down movement
        if x<N-1:
            m=copy.deepcopy(currState)
            m=moveDownward(m,x,y)
            newpuzzle=tuple(map(tuple,m))

            if newpuzzle not in visited.keys() and isPossible(m):
              visited[newpuzzle]=1
              s.put(m)

        #for right movement
        if y<N-1:
            m=copy.deepcopy(currState)
            m=moveRight(m,x,y)
            newpuzzle=tuple(map(tuple,m))
            
            if newpuzzle not in visited.keys() and isPossible(m):
              visited[newpuzzle]=1
              s.put(m)
               
        #for left movement
        if y!=0:
            m=copy.deepcopy(currState)
            m=moveLeft(m,x,y)
            newpuzzle=tuple(map(tuple,m))

            if newpuzzle not in visited.keys() and isPossible(m):
              visited[newpuzzle]=1
              s.put(m)


        #for up movement
        if x!=0:
            m=copy.deepcopy(currState)
            m=moveUpward(m,x,y)
            newpuzzle=tuple(map(tuple,m))

            if newpuzzle not in visited.keys() and isPossible(m):
              visited[newpuzzle]=1
              s.put(m)

    return


#Ref : Geeks For Geeks for inversions pairs
def countInversions(Puzzle):
	arr=[]
	for y in Puzzle:
		for x in y:
			arr.append(x)
            
	Puzzle=arr
	inv_count = 0

	for i in range(N * N - 1):
		for j in range(i + 1,N * N):
			# count pairs(arr[i], arr[j]) such that i < j and arr[i] > arr[j]
			if (Puzzle[j] and Puzzle[i] and Puzzle[i] > Puzzle[j]):
				inv_count+=1
		
	return inv_count


# find Position of blank from bottom
def findXPosition(Puzzle):
	# start from bottom-right corner of matrix
	for i in range(N - 1,-1,-1):
		for j in range(N - 1,-1,-1):
			if (Puzzle[i][j] == 0):
				return N - i


# Ref : Geeks For Geeks for inversions count 
def isPossible(Puzzle):
	# Count inversions in given Puzzle
	invCount = countInversions(Puzzle)
	# If grid is odd, return true if inversion count is even.
	if (N & 1):
		return not(invCount & 1)

	else: 
        # grid is even and pos of blank is even and inversion is odd, return true
        # grid is even and pos of blank is odd and inversion is even, return true
		pos = findXPosition(Puzzle)
		if (pos & 1):
			return not(invCount & 1)
		else:
			return invCount & 1
	


# Main Function that solve this Puzzle
if __name__=='__main__':
    # Taking Board Size Input
    print("Enter the value of N to create NxN Puzzle")
    N=int(input())
    print("To generate random puzzle enter R/Enter U for user input: ")
    # Taking Board Size Input
    f=input()

    # taking input initial puzzle state or also can generate random number
    if(f=='U'):
        print("Enter Initital State of the Puzzle(Space Seperated Value (N*N):  ",sep="")
        Puzzle=[]
        for i in range (1,N+1):
            print("enter values to row ",i,sep="")
            Puzzle.append(list(map(int,input().split(" "))))
    # generating random puzzle        
    elif(f=='R'):
        t=[]
        Puzzle=[]
        for i in range (0,N):
            temp=[]
            for j in range (0,N):
                temp.append(i)
            Puzzle.append(temp)
        for i in range (0,N*N):
            t.append(i)
        random.shuffle(t) 
        print(t)  
        k = 0
        for i in range (0,N):
            for j in range (0,N):
                Puzzle[i][j]=t[k]
                k=k+1

    
    #final target Puzzle state
    # it is fixed in this Puzzle
    final=[]
    l=[]
    for i in range (1,N*N+1):
        if i!=N*N:
            l.append(i)
        else:
            l.append(0)
        if i%N==0:
            final.append(l)
            l=[]
    
    print("Initial state of Puzzle:")
    # Printing intial state of puzzle  
    for i in range(0,N):
        print(Puzzle[i])
    
    if isPossible(Puzzle):

        print("\nPuzzle is solvable.")
        print("Order of movement of blank space is UP LEFT RIGHT DOWN")
        
        # printing all steps
        print("Running BFS algorithm..... ",end="\n")
        time.sleep(3)

        # finding steps taken by BFS Algorithm  
        starttimebfs=time.time()
        stepInBFS=startBFS(Puzzle,final)
        endtimebfs=time.time()
        
        print("BFS Algorithm Executed Successfully!")
        time.sleep(3)
        print("Running DFS algorithm.....",end="\n")
        time.sleep(3)
        # finding steps taken by BFS Algorithm
        
        starttimedfs=time.time()
        stepInDFS=startDFS(Puzzle,final)
        endtimedfs=time.time()
        print("BFS Algorithm Executed Successfully!")
        print("")


        # Final Output
        print("****************************Overall Statstics*******************************")
        print("Steps taken by BFS algorithm = ",end="")
        print(stepInBFS)
        print("Time taken by BFS : ",endtimebfs-starttimebfs)
        print("Steps taken by DFS algorithm = ",end="")
        print(stepInDFS)
        print("Time taken by DFS : ",endtimedfs-starttimedfs)


        # Comparison of Steps Taken by both the algorithms  
        if(stepInBFS<stepInDFS):
            print("BFS algorithm Performs Better than DFS algorithm for this given Puzzle.")
        elif(stepInBFS>stepInDFS):
            print("DFS algorithm Performs Better than BFS algorithm for this given Puzzle.")
        else:
            print("Both BFS and DFS algorithm solves the given Puzzle in equivalent time.")
        print("*************Thank You So Much For Using Our Application*******************")
    # Unsolvable
    else:
        print("Ooops! Try With New Puzzle")
          
