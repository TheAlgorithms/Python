class SegmentTree:
    def __init__(self, values):
        self.valarr = values
        self.arr = dict()

    #start is the starting index of node.
    #end is the ending index of node.
    #l is the lower bound of given query.
    #r is the upper bound of given query.

    def buildTree(self, start, end, node):
        if start == end:
            self.arr[node] = self.valarr[start]
            return
        mid = (start+end)//2
        #Building the left subtree of the node.
        self.buildTree(start, mid, node*2)
        #Building the right subtree of the node.
        self.buildTree(mid+1, end, node*2+1)
        #Assign the value of node as the sum of its children.
        self.arr[node] = self.arr[node*2]+self.arr[node*2+1]

    def rangeQuery(self, node, start, end, l, r):
        #When start and end index of the given node lies between the query range[l, r].
        if (l <= start and r >= end):
            return self.arr[node]
        #When the start and end index of the given node lies completely outside of the query range[l, r].
        if (end < l or start > r):
            return 0
        #In case of overlapping of the regions of the start and end index of node and query range[l, r].
        mid = (start+end)//2
        return self.rangeQuery(2*node, start, mid, l, r) + self.rangeQuery(2*node+1, mid+1, end, l, r)

    def update(self, node, newvalue, oldvalue, position, start, end):
        #If position where the given value to be inserted lies within start and end index of the node.
        if start <= position <= end:
            self.arr[node] += (newvalue-oldvalue)
        #Updating all those nodes where position lies within its start and end index.
        if start != end:
            mid = (start+end)//2
            self.update(node*2, newvalue, oldvalue, position, start, mid)
            self.update(node*2+1, newvalue, oldvalue, position, mid+1, end)

#Code to run the above functions
if __name__ == '__main__':
    l = list(map(int, input("Enter the elements of the array separated by space:\n").split()))
    st = SegmentTree(l)
    st.buildTree(0, len(l)-1, 1)

    #I have assumed 1 as the base index instead of 0.
    baseindex = 1
    endindex = len(l)

    #To print the constructed segment tree.
    print(st.arr)

    #To print the sum of numbers between index 3 and 5.
    print("Sum of numbers from index 3 and 5 is: ", st.rangeQuery(1, baseindex, endindex, 3, 5))

    #Updating 3rd element of the array to 10.
    updateindex = 3
    updatevalue = 10
    st.update(1, updatevalue, l[updateindex-1], updateindex, baseindex, endindex)

    #To print the sum of numbers between index 3 and 5 after updation
    print("Updated sum of numbers from index 3 and 5 is: ", st.rangeQuery(1, baseindex, endindex, 3, 5))