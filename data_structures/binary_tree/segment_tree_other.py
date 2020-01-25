#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from queue import Queue


class SegmentTreeNode(object):
    def __init__(self, start, end, val, left=None, right=None):
        self.start = start
        self.end = end
        self.val = val
        self.mid = (start + end) // 2
        self.left = left
        self.right = right

    def __str__(self):
        return 'val: %s, start: %s, end: %s' % (self.val, self.start, self.end)


class NumArray:
    def __init__(self, nums):
        self.nums = nums
        if self.nums:
            self.root = self._build_tree(0, len(nums) - 1)

    def update(self, i, val):
        self._update_tree(self.root, i, val)

    def sum_range(self, i, j):
        return self._sum_range(self.root, i, j)

    def _build_tree(self, start, end):
        if start == end:
            return SegmentTreeNode(start, end, self.nums[start])
        mid = (start + end) // 2
        left = self._build_tree(start, mid)
        right = self._build_tree(mid + 1, end)
        return SegmentTreeNode(start, end, left.val + right.val, left, right)

    def _update_tree(self, root, i, val):
        if root.start == i and root.end == i:
            root.val = val
            return
        if i <= root.mid:
            self._update_tree(root.left, i, val)
        else:
            self._update_tree(root.right, i, val)
        root.val = root.left.val + root.right.val

    def _sum_range(self, root, i, j):
        if root.start == i and root.end == j:
            return root.val
        """
         [i, j] [i, j] [i, j]
        [start mid] [mid+1 end]
        """
        if j <= root.mid:
            return self._sum_range(root.left, i, j)
        elif i > root.mid:
            return self._sum_range(root.right, i, j)
        else:
            return self._sum_range(root.left, i, root.mid) + self._sum_range(root.right, root.mid + 1, j)

    def traverse(self):
        result = []
        if self.root is not None:
            queue = Queue()
            queue.put(self.root)
            while not queue.empty():
                node = queue.get()
                result.append(node)

                if node.left is not None:
                    queue.put(node.left)

                if node.right is not None:
                    queue.put(node.right)
            return result


class MaxArray:
    def __init__(self, nums):
        self.nums = nums
        if self.nums:
            self.root = self._build_tree(0, len(nums) - 1)

    def update(self, i, val):
        self._update_tree(self.root, i, val)

    def max_range(self, i, j):
        return self._max_range(self.root, i, j)

    def _build_tree(self, start, end):
        if start == end:
            return SegmentTreeNode(start, end, self.nums[start])
        mid = (start + end) // 2
        left = self._build_tree(start, mid)
        right = self._build_tree(mid + 1, end)
        return SegmentTreeNode(start, end, max([left.val, right.val]), left, right)

    def _update_tree(self, root, i, val):
        if root.start == i and root.end == i:
            root.val = val
            return
        if i <= root.mid:
            self._update_tree(root.left, i, val)
        else:
            self._update_tree(root.right, i, val)
        root.val = max([root.left.val, root.right.val])

    def _max_range(self, root, i, j):
        if root.start == i and root.end == j:
            return root.val
        """
         [i, j] [i, j] [i, j]
        [start mid] [mid+1 end]
        """
        if j <= root.mid:
            return self._max_range(root.left, i, j)
        elif i > root.mid:
            return self._max_range(root.right, i, j)
        else:
            return max([self._max_range(root.left, i, root.mid), self._max_range(root.right, root.mid + 1, j)])

    def traverse(self):
        result = []
        if self.root is not None:
            queue = Queue()
            queue.put(self.root)
            while not queue.empty():
                node = queue.get()
                result.append(node)

                if node.left is not None:
                    queue.put(node.left)

                if node.right is not None:
                    queue.put(node.right)
            return result


class MinArray:
    def __init__(self, nums):
        self.nums = nums
        if self.nums:
            self.root = self._build_tree(0, len(nums) - 1)

    def update(self, i, val):
        self._update_tree(self.root, i, val)

    def min_range(self, i, j):
        return self._min_range(self.root, i, j)

    def _build_tree(self, start, end):
        if start == end:
            return SegmentTreeNode(start, end, self.nums[start])
        mid = (start + end) // 2
        left = self._build_tree(start, mid)
        right = self._build_tree(mid + 1, end)
        return SegmentTreeNode(start, end, min([left.val, right.val]), left, right)

    def _update_tree(self, root, i, val):
        if root.start == i and root.end == i:
            root.val = val
            return
        if i <= root.mid:
            self._update_tree(root.left, i, val)
        else:
            self._update_tree(root.right, i, val)
        root.val = min([root.left.val, root.right.val])

    def _min_range(self, root, i, j):
        if root.start == i and root.end == j:
            return root.val
        """
         [i, j] [i, j] [i, j]
        [start mid] [mid+1 end]
        """
        if j <= root.mid:
            return self._min_range(root.left, i, j)
        elif i > root.mid:
            return self._min_range(root.right, i, j)
        else:
            return min([self._min_range(root.left, i, root.mid), self._min_range(root.right, root.mid + 1, j)])

    def traverse(self):
        result = []
        if self.root is not None:
            queue = Queue()
            queue.put(self.root)
            while not queue.empty():
                node = queue.get()
                result.append(node)

                if node.left is not None:
                    queue.put(node.left)

                if node.right is not None:
                    queue.put(node.right)
            return result


if __name__ == '__main__':
    print('求和线段树')
    num_arr = NumArray([2, 1, 5, 3, 4])
    for node in num_arr.traverse():
        print(node)
    print()

    num_arr.update(1, 5)
    for node in num_arr.traverse():
        print(node)
    print()

    print(num_arr.sum_range(3, 4))  # 7
    print(num_arr.sum_range(2, 2))  # 5
    print(num_arr.sum_range(1, 3))  # 13

    print()
    print('求最大值线段树')
    max_arr = MaxArray([2, 1, 5, 3, 4])
    for node in max_arr.traverse():
        print(node)
    print()

    max_arr.update(1, 5)
    for node in max_arr.traverse():
        print(node)
    print()

    print(max_arr.max_range(3, 4))  # 4
    print(max_arr.max_range(2, 2))  # 5
    print(max_arr.max_range(1, 3))  # 5

    print()
    print('求最小值线段树')
    min_arr = MinArray([2, 1, 5, 3, 4])
    for node in min_arr.traverse():
        print(node)
    print()

    min_arr.update(1, 5)
    for node in min_arr.traverse():
        print(node)
    print()

    print(min_arr.min_range(3, 4))  # 3
    print(min_arr.min_range(2, 2))  # 5
    print(min_arr.min_range(1, 3))  # 3
