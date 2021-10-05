#!/usr/bin/python

""" Author: Sourav Verma """
from __future__ import annotations

class Solution:
    '''
    # Function to return the level order traversal of a tree.
    
    Input:
                10
             /      \
            20       30
          /   \
         40   60
         
    Output:10 20 30 40 60 N N
    '''
    def levelOrder(self, root):
        # Code here
        level_ordered_list, q = list(), list()
        q.append(root)
        while(q):
            tmp = q.pop(0)
            level_ordered_list.append(tmp.data)
            if tmp.left:
                q.append(tmp.left)
            if tmp.right:
                q.append(tmp.right)
        return level_ordered_list


if __name__ == "__main__":
    from doctest import testmod

    testmod(verbose=True)
