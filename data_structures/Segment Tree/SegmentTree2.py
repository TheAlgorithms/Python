import sys

class SegmentTree:
    def __init__(self, values):
        self.minarr = dict()
        #Storing the original array for later use.
        self.originalarr = values[:]

        # start is the starting index of node.
        # end is the ending index of node.
        # l is the lower bound of given query.
        # r is the upper bound of given query.

    def buildminTree(self, start, end, node):
        if start == end:
            self.minarr[node] = self.originalarr[start]
            return
        mid = (start + end) // 2
        # Building the left subtree of the node.
        self.buildminTree(start, mid, node*2)
        # Building the right subtree of the node.
        self.buildminTree(mid + 1, end, node*2 + 1)
        # Assign the value of node as the sum of its children.
        self.minarr[node] = min(self.minarr[node*2], self.minarr[node*2 + 1])

    def minRangeQuery(self, node, start, end, l, r):
        if l <= start and end <= r:
            return self.minarr[node]
        if r < start or l > end:
            return sys.maxsize
        mid = (start+end)//2
        return min(self.minRangeQuery(node*2, start, mid, l, r), self.minRangeQuery(node*2+1, mid+1, end, l, r))

    def update(self, node, newvalue, position, start, end):
        if start <= position <= end:
            self.minarr[node] = min(self.minarr[node], newvalue)
        # Updating all those nodes where position lies within its start and end index.
        if start != end:
            mid = (start + end) // 2
            self.update(node * 2, newvalue, position, start, mid)
            self.update(node * 2 + 1, newvalue, position, mid + 1, end)

arr = [10, 5, 9, 3, 4, 8, 6, 7, 2, 1]
st = SegmentTree(arr)
st.buildminTree(0, len(arr)-1, 1)
print("Segment Tree for given array", st.minarr)

#Minimum from index 6 to 9.
print("Minimum of numbers from index 6 to 9 is: ", st.minRangeQuery(1, 1, len(arr), 6, 9))
st.update(1, 2, 4, 1, len(arr))

print(st.minarr)

print("Updated minimum of numbers from index 2 to 9 is: ", st.minRangeQuery(1, 1, len(arr), 2, 6))

#ALl the operations are same for max range Query. Just replace each min() with max and sys.maxsize with -(sys.maxsize).