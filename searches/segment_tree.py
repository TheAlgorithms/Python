"""
Author  : Sanjay Muthu <https://github.com/XenoBytesX>

This is a Pure Python implementation of the Segment Tree Data Structure

The problem statement is:
    Given an array and q queries,
    each query is one of two types:-
        1. update:- (index, value)
        update the array at index i to be equal to the new value
        2. query:- (l, r)
        print the result for the query from l to r
        Here, the query depends on the problem which the segment tree is implemented on,
        a common example of the query is sum or xor
        (https://www.loginradius.com/blog/engineering/how-does-bitwise-xor-work/)

Example:
    array (a) = [5, 2, 3, 1, 7, 2, 9]
    queries (q) = 2
    query = sum

    query 1:- update 1 3
        - a[1] becomes 2
        - a = [5, 3, 3, 1, 7, 2, 9]

    query 2:- query 1 5
        - a[1] + a[2] + a[3] + a[4] + a[5] = 3+3+1+7+2 = 16
        - answer is 16

Time Complexity:- O(N Log N + Q Log N)
-- O(N Log N) time for building the segment tree
-- O(log n) time for each query
-- Q queries are there so total time complexity is O(Q Log n)

Space Complexity:- O(N)

Algorithm:-
We first build the segment tree. An example of what the tree would look like:-
(query type is sum)
array = [5, 2, 3, 6, 1, 2]
modified_array = [5, 2, 3, 6, 1, 2, 0, 0] size is 8 which a power of 2
so we can build the segment tree

segment tree:-
                              19
                            /   \
                        /           \
                    /                   \
             /                               \
            16                               3
        /       \\                         /     \
      /           \\                    /          \
    /               \\               /               \
    7               9               3               0
  /   \\           /   \\           /   \\           /   \
 /     \\         /     \\         /     \\         /     \
/       \\       /       \\       /       \\       /       \
5       2       3       6       1       2       0       0


This segment tree cannot be stored in code so we convert it into a list

segment tree list = [19, 16, 3, 7, 9, 3, 0, 5, 2, 3, 6, 1, 2, 0, 0]
There is a property of this list that we can use to make the code much simpler
segment tree list[2*i] and segment tree list[2*i+1]
are the children of segment tree list[i]


For Updating:-
We first update the base element (the last row elements)
and then slowly staircase up to update the entire segment tree part
from the updated element

For querying:-
We start from the root(the topmost element) and go down, each node has one of 3 cases:-
    Case 1. The node is completely inside the required range
        then return the node value
    Case 2. The node is completely outside the required range
        then return 0
    Case 3. The node is partially inside the required range
        Query both the children and add their results and return that
"""


class SegmentTree:
    def __init__(self, arr, merge_func, default):
        """
        Initializes the segment tree
        :param arr: Input array
        :param merge_func: The function which is used to merge
        two elements of the segment tree
        :param default: The default value for the nodes
        (Ex:- 0 if merge_func is sum, inf if merge_func is min, etc.)
        """
        self.arr = arr
        self.n = len(arr)

        # while self.n is not a power of two
        while (self.n & (self.n - 1)) != 0:
            self.n += 1
            self.arr.append(default)

        self.merge_func = merge_func
        self.default = default
        self.segment_tree = [default] * (2 * self.n)

        for i in range(self.n):
            self.segment_tree[self.n + i] = arr[i]

        for i in range(self.n - 1, 0, -1):
            self.segment_tree[i] = self.merge_func(
                self.segment_tree[2 * i], self.segment_tree[2 * i + 1]
            )

    def update(self, index, value):
        """
        Updates the value at an index and propagates the change to all parents
        """
        self.segment_tree[self.n + index] = value

        while index >= 1:
            index //= 2  # Go to the parent of index
            self.segment_tree[index] = self.merge_func(
                self.segment_tree[2 * index], self.segment_tree[2 * index + 1]
            )

    def query(self, left, right, node_index=1, node_left=0, node_right=None):
        """
        Finds the answer of self.merge_query(left, left+1, left+2, left+3, ..., right)
        """
        if not node_right:
            # We can't add self.n as the default value in the function
            # because self itself is a parameter so we do it this way
            node_right = self.n

        # If the node is completely outside the query region we return the default value
        if node_left > right or node_right < left:
            return self.default

        # If the node is completely inside the query region we return the node's value
        if node_left > left and node_right < right:
            return self.segment_tree[node_index]

        # Else:-
        # Find the middle element
        mid = int((node_left + node_right) / 2)

        # The answer is sum (or min or anything in the merge_func)
        # of the query values of both the children nodes
        return self.merge_func(
            self.query(left, right, node_index * 2, node_left, mid),
            self.query(left, right, node_index * 2 + 1, mid + 1, node_right),
        )
