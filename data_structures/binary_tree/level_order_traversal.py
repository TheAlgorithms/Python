# Level order traversal of a binary tree means to traverse node values from left to right, level by level
class Trees: 
      
    """Constructor to create a new tree node"""
    def __init__(self,data): 
        self.val = data 
        self.left = None
        self.right = None
      
    """Prints level order traversal line by  
    line using two queues."""
    def levelOrder(self,node): 
        q1 = [] # Queue 1 
        q2 = [] # Queue 2 
        q1.append(node) 
          
        """Executing loop till both the  
        queues become empty"""
        while(len(q1) > 0 or len(q2) > 0): 
          
            """Empty string to concatenate  
            the string for q1"""
            concat_str_q1 = '' 
            while(len(q1) > 0): 
                  
                """Poped node at the first  
                pos in queue 1 i.e q1"""
                poped_node = q1.pop(0) 
                concat_str_q1 += poped_node.val +' '
                  
                """Pushing left child of current  
                node in first queue into second queue"""
                if poped_node.left: 
                    q2.append(poped_node.left) 
                      
                """Pushing right child of current node 
                in first queue into second queue"""
                if poped_node.right: 
                    q2.append(poped_node.right) 
            print( str(concat_str_q1)) 
            concat_str_q1 = '' 
              
            """Empty string to concatenate the  
            string for q1"""
            concat_str_q2 = '' 
            while (len(q2) > 0): 
              
                """Poped node at the first pos 
                in queue 1 i.e q1"""
                poped_node = q2.pop(0) 
                concat_str_q2 += poped_node.val + ' '
                  
                """Pushing left child of current node 
                in first queue into first queue"""
                if poped_node.left: 
                    q1.append(poped_node.left) 
                  
                """Pushing right child of current node  
                in first queue into first queue"""
                if poped_node.right: 
                    q1.append(poped_node.right) 
            print(str(concat_str_q2)) 
            concat_str_q2 = '' 
  
""" Driver program to test above functions"""
node = Trees("1") 
node.left = Trees("2") 
node.right = Trees("3") 
node.left.left = Trees("4") 
node.left.right = Trees("5") 
node.right.right = Trees("6") 
node.levelOrder(node) 