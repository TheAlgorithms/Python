# Name: Ritika Rastogi
# Date: 27-10-2022
class MinStack(object):
    def __init__(self):
        self.object = []

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.val = val
        self.object.append(val)

    def pop(self):
        """
        :rtype: None
        """
        return self.object.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.object[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return min(self.object)


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
