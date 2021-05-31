import random
import unittest

'''
A Segment Tree is a data structure that allows answering range queries over an array effectively,
while still being flexible enough to allow modifying the array. This includes finding the sum of
consecutive array elements a[l…r], or finding the minimum element in a such a range in O(logn) time.
'''

class Node(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.total = 0
        self.left = None
        self.right = None
        
class Segment_Trees:

    def __init__(self, nums):


        def build(nums,l,r):
            if l>r:
                return
            if l==r:
                temp = Node(l,r)
                temp.total = nums[l]
                return temp
            mid = (l+r)//2
            
            root = Node(l,r)
            
            root.left = build(nums,l,mid)
            root.right = build(nums,mid+1,r)
            
            root.total = root.left.total + root.right.total
            
            return root
        self.root = build(nums,0,len(nums)-1)
        
        

    def update(self, index, val):
        def updateVal(root,i,val):
            if root.start == root.end:
                root.total = val
                return val
            mid = (root.start + root.end)//2
            
            if i<=mid:
                updateVal(root.left,i,val)
            else:
                updateVal(root.right,i,val)
            root.total = root.left.total + root.right.total
            return root.total
        updateVal(self.root,index,val)
        
        

    def query(self, left, right):
        def rangeSum(root, i, j):
            if root.start == i and root.end == j:
                return root.total
            
            mid = (root.start + root.end) // 2
            
        
            if j <= mid:
                return rangeSum(root.left, i, j)
            elif i >= mid + 1:
                return rangeSum(root.right, i, j)
            else:
                return rangeSum(root.left, i, mid) + rangeSum(root.right, mid+1, j)
        return rangeSum(self.root,left,right)
    


class Test_Segment_Trees(unittest.TestCase):

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
        objt = Segment_Trees(arr)
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
