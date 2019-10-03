import sys
import unittest

class segment_tree:
    def __init__(self, values):
        self.min_arr = dict()
        #Storing the original array for later use.
        self.original_arr = values[:]

        # start is the starting index of node.
        # end is the ending index of node.
        # l is the lower bound of given query.
        # r is the upper bound of given query.

    def build_min_tree(self, start, end, node):
        if start == end:
            self.min_arr[node] = self.original_arr[start]
            return
        mid = (start + end) // 2
        # Building the left subtree of the node.
        self.build_min_tree(start, mid, node*2)
        # Building the right subtree of the node.
        self.build_min_tree(mid + 1, end, node*2 + 1)
        # Assign the value of node as the sum of its children.
        self.min_arr[node] = min(self.min_arr[node*2], self.min_arr[node*2 + 1])

    def min_range_query(self, node, start, end, l, r):
        if l <= start and end <= r:
            return self.min_arr[node]
        if r < start or l > end:
            return sys.maxsize
        mid = (start+end)//2
        return min(self.min_range_query(node*2, start, mid, l, r), self.min_range_query(node*2+1, mid+1, end, l, r))

    def update(self, node, new_value, position, start, end):
        if start <= position <= end:
            self.min_arr[node] = min(self.min_arr[node], new_value)
        # Updating all those nodes where position lies within its start and end index.
        if start != end:
            mid = (start + end) // 2
            self.update(node * 2, new_value, position, start, mid)
            self.update(node * 2 + 1, new_value, position, mid + 1, end)

#Defining the array on which the operations are to be performed.
arr = [10, 5, 9, 3, 4, 8, 6, 7, 2, 1]
#Making Segment Tree object.
st = segment_tree(arr)
#Building the Segment Tree for given array.
st.build_min_tree(0, len(arr)-1, 1)

class segment_tree_test(unittest.TestCase):
    
    def test_st_functions(self):
        #Minimum from index 6 to 9 i.e. 2.
        self.assertEqual(st.min_range_query(1, 1, len(arr), 6, 9), 2)
        
        #Updating element at 4th position to 1.
        st.update(1, 1, 4, 1, len(arr))
        #Updated array [10, 5, 9, 1, 4, 8, 6, 7, 2, 1]
        
        #Minimum from index 2 to 6 i.e. 1.
        self.assertEqual(st.min_range_query(1, 1, len(arr), 2, 6), 1)

if __name__ == '__main__': 
    unittest.main()

#ALl the operations are same for max range Query. Just replace each min() with max and sys.maxsize with -(sys.maxsize).