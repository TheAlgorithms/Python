import random
import unittest

'''
A Segment Tree is a data structure that allows answering range queries over an array effectively,
while still being flexible enough to allow modifying the array. This includes finding the sum of
consecutive array elements a[l…r], or finding the minimum element in a such a range in O(logn) time.
'''

class Node(object):
    def __init__(self, start :int, end :int) -> None:
        self.start = start
        self.end = end
        self.total = 0
        self.left = None
        self.right = None
        
class segment_trees:

    def __init__(self, nums ) -> None:


        def build(nums ,left :int,right :int) -> None:
            if left>right:
                return
            if left==right:
                temp = Node(left,right)
                temp.total = nums[left]
                return temp
            mid = (left+right)//2
            
            root = Node(left,right)
            
            root.left = build(nums,left,mid)
            root.right = build(nums,mid+1,right)
            
            root.total = root.left.total + root.right.total
            
            return root
        self.root = build(nums,0,len(nums)-1)
        
        

    def update(self, index :int, val:int) -> None:
        def updateval(root :Node,indx :int,val:int) -> None: 
            if root.start == root.end:
                root.total = val
                return val
            mid = (root.start + root.end)//2
            
            if indx<=mid:
                updateval(root.left,indx,val)
            else:
                updateval(root.right,indx,val)
            root.total = root.left.total + root.right.total
            return root.total
        updateval(self.root,index,val)
        
        

    def query(self, left :int, right :int) -> int:
        def rangesum(root, start :int, end :int) -> int:
            if root.start == start and root.end == end:
                return root.total
            
            mid = (root.start + root.end) // 2
            
        
            if end <= mid:
                return rangesum(root.left, start, end)
            elif start >= mid + 1:
                return rangesum(root.right, start, end)
            else:
                return rangesum(root.left, start, mid) + rangesum(root.right, mid+1, end)
        return rangesum(self.root,left,right)
    


class test_segment_trees(unittest.TestCase):

    def test_sg(self):
        l = random.randint(2,100)
        arr = []
        for i in range(l):
            temp = random.randint(1,100)
            arr.append(temp)
        num1 = random.randint(0,l-1)
        num2 = random.randint(0,l-1)
        left = min(num1,num2)
        right = max(num1,num2)
        objt = segment_trees(arr)
        sum1 = objt.query(left,right)
        sum2 = 0
        for i in range(left,right+1):
            sum2+=arr[i]
        mess = "Segment Trees is not working fine!"
        self.assertEqual(sum1,sum2,mess)

        #After Updating Values
        idx = random.randint(0,l-1)
        value = random.randint(1,100)

        #Update Value in segment Tree
        objt.update(idx,value)

        #Update Value in Array or it will raise error
        arr[idx] = value

        #Check the sum again
        sum1 = objt.query(left,right)
        sum2 = 0
        for i in range(left,right+1):
            sum2+=arr[i]
        mess = "Segment Trees is not working fine!"
        self.assertEqual(sum1,sum2,mess)


if __name__ == '__main__':
    unittest.main()
