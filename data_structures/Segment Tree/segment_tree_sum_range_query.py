import unittest

class segment_tree:
    def __init__(self, values):
        self.n = len(values)
        self.val_arr = values
        self.arr = dict()

    #start is the starting index of node.
    #end is the ending index of node.
    #l is the lower bound of given query.
    #r is the upper bound of given query.

    def build_tree(self, start, end, node):
        if start == end:
            self.arr[node] = self.val_arr[start]
            return
        mid = (start+end)//2
        #Building the left subtree of the node.
        self.build_tree(start, mid, node*2)
        #Building the right subtree of the node.
        self.build_tree(mid+1, end, node*2+1)
        #Assign the value of node as the sum of its children.
        self.arr[node] = self.arr[node*2]+self.arr[node*2+1]

    def range_query(self, node, start, end, l, r):
        #When start and end index of the given node lies between the query range[l, r].
        if (l <= start and r >= end):
            return self.arr[node]
        #When the start and end index of the given node lies completely outside of the query range[l, r].
        if (end < l or start > r):
            return 0
        #In case of overlapping of the regions of the start and end index of node and query range[l, r].
        mid = (start+end)//2
        return self.range_query(2*node, start, mid, l, r) + self.range_query(2*node+1, mid+1, end, l, r)

    def update(self, node, new_value, old_value, position, start, end):
        #If position where the given value to be inserted lies within start and end index of the node.
        if start <= position <= end:
            self.arr[node] += (new_value-old_value)
        #Updating all those nodes where position lies within its start and end index.
        if start != end:
            mid = (start+end)//2
            self.update(node*2, new_value, old_value, position, start, mid)
            self.update(node*2+1, new_value, old_value, position, mid+1, end)


#Defining the array on which operations are to be performed.
l = [1, 4, 8, 15, 7, 9]
#Making object of Segment Tree.
st = segment_tree(l)
#Building the Segment Tree.
st.build_tree(0, len(l)-1, 1)
    
#I have assumed 1 as the base index instead of 0.
baseindex = 1
endindex = len(l)


#Code to run the above functions

class segment_tree_test(unittest.TestCase): 
    
    def test_st_functions(self):  
        #To print the sum of number between index 3 and 5 i.e. (8+15+7).
        self.assertEqual(st.range_query(1, baseindex, endindex, 3, 5), 30)
        
        #Updating 3rd element of the array to 10.
        updateindex = 3
        updatevalue = 10
        st.update(1, updatevalue, l[updateindex-1], updateindex, baseindex, endindex)
        #[1, 4, 10, 15, 7, 9] is the updated array.
        
        #To print the sum of numbers between index 3 and 5 after updation i.e. (10+15+7).
        self.assertEqual(st.range_query(1, baseindex, endindex, 3, 5), 32)
         
  
if __name__ == '__main__': 
    unittest.main() 