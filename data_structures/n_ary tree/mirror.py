# Python program to mirror an n-ary tree 
  
class Node : 
  
    def __init__(self ,key): 
        self.key = key  
        self.child = [] 
  

def mirrorTree(root): 
      

    if root is None: 
        return
      

    n = len(root.child) 

    if n <2 : 
        return

    for i in range(n): 
        mirrorTree(root.child[i]); 
      
    root.child.reverse() 
      
  

def printNodeLevelWise(root): 
    if root is None: 
        return 

    queue = [] 
    queue.append(root) 
  

    while(len(queue) >0): 
  
        n = len(queue) 
        while(n > 0) : 
  
            # Dequeue an item from queue and print it 
            p = queue[0] 
            queue.pop(0) 
            print p.key, 
      
            # Enqueue all children of the dequeued item 
            for index, value in enumerate(p.child): 
                queue.append(value) 
  
            n -= 1
        print "" # Seperator between levels 
          

  
root = Node(10) 
root.child.append(Node(2)) 
root.child.append(Node(34)) 
root.child.append(Node(56)) 
root.child.append(Node(100)) 
root.child[2].child.append(Node(1)) 
root.child[3].child.append(Node(7)) 
root.child[3].child.append(Node(8)) 
root.child[3].child.append(Node(9)) 
  
print "Level order traversal Before Mirroring"
printNodeLevelWise(root) 
  
mirrorTree(root) 
      
print "\nLevel Order traversal After Mirroring"
printNodeLevelWise(root) 
