
#Represent a node of binary tree  
class Node:  
    def __init__(self,data):  
        #Assign data to the new node, set left and right children to None  
        self.data = data;  
        self.left = None;  
        self.right = None;  
   
class SumOfNodes:  
    def __init__(self):  
        #Represent the root of binary tree  
        self.root = None;  
      
    #calculateSum() will calculate the sum of all the nodes present in the binary tree  
    def calculateSum(self, temp):  
        sum = sumRight = sumLeft = 0;  
          
        #Check whether tree is empty  
        if(self.root == None):  
            print("Tree is empty");  
            return 0;  
        else:  
            #Calculate the sum of nodes present in left subtree  
            if(temp.left != None):  
                sumLeft = self.calculateSum(temp.left);  
              
            #Calculate the sum of nodes present in right subtree  
            if(temp.right != None):  
                sumRight = self.calculateSum(temp.right);  
              
            #Calculate the sum of all nodes by adding sumLeft, sumRight and root node's data  
            sum = temp.data + sumLeft + sumRight;   
        return sum;  
   
bt = SumOfNodes();  
#Add nodes to the binary tree  
bt.root = Node(5);  
bt.root.left = Node(2);  
bt.root.right = Node(9);  
bt.root.left.left = Node(1);  
bt.root.right.left = Node(8);  
bt.root.right.right = Node(6);  
   
#Display the sum of all the nodes in the given binary tree  
print("Sum of all nodes of binary tree: " + str(bt.calculateSum(bt.root)));  
