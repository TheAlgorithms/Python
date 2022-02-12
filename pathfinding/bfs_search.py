'''
We have a MxN maze.
We start from 0,0 and we try to reach (-1,-1)
Our program shows us the shortest path, if there is any.

  .W.
  .W.
  ...

  .W....
  .W....
  .W.W..
  .W.W..
  .W.W..
  ...W..

'''

def path_finder(maze):
    maze=maze.split('\n')
    ls=[(0,0),] #the list we store out coordinates.
    want=(len(maze)-1,len(maze)-1) #the variable which will be passed in the while loop
    x=len(maze)
    cs1,cs2=0,0 #those are trackers of the length of the nodes, so if one doesn't increase, that means that there are no more paths to go.
    ck=set(ls) #the set we use to check the coordinates.

    while True:
        b=[]
        for i in range(cs1,len(ls)):
            new=[(ls[i][0]-1,ls[i][1]),(ls[i][0]+1,ls[i][1]),(ls[i][0],ls[i][1]+1),(ls[i][0],ls[i][1]-1)] #generating all the possible nodes from the previous newly generated nodes
        
            for z in new:
                if -1 not in z and x not in z and maze[z[0]][z[1]]!='W': #testing if the newly generated nodes hit the wall or not
                    b.append(z)
            
        cs1=len(ls)-1
        for i in b:
            if i not in ck:
                #adding the new nodes
                ls.append(i)
                ck.update((i,))
        cs2=len(ls)-1
        if cs1==cs2: #if the nodes have no more paths to visit
            if want in ls:
                ans=[]
                last=want
                #from here, we are starting from the (-1,-1) and iterating throught the list
                #if there are any nodes which can connect with the previous node, add that to the shortest possible path.
                x=ls[::-1][1:]
                for i in x:
                    if sorted([abs(last[0]-i[0]),abs(last[1]-i[1])])==[0,1]: 
                        last=i
                        ans.append(i)
                ans.reverse() #reversing because the path is in reverse
                ans.append(want) #adding the last node for cosmetic reasons
                return ans
            else: #if the path didn't reach the end:
                return False