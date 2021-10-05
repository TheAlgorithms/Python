"""
Jump Search Algorithm
https://en.wikipedia.org/wiki/Jump_search
Author @divyanshugit 
"""
import math
class JumpSearch:
    def __init__(self,lst,value):
        self.list = lst
        self.value= value
    
    def jump_search(self):
        """
        -At first, It determines the jump size by computing math.sqrt(len(lys)).
        -Next, it computes the value of the right variable, which is the minimum of the length of the array minus 1, or the value of left+jump.
        -It checks whether our search element.
        -In the end we calculate the position of element.
        """

        length = len(self.list)
        val = self.value
        jump = int(math.sqrt(length))
        left, right = 0, 0
        while left < length and lst[left] <= val:
            right = min(length - 1, left + jump)
            if lst[left] <= val and lst[right] >= val:
                break
            left += jump;
        if left >= length or lst[left] > val:
            return -1
        right = min(length - 1, right)
        i = left
        while i <= right and lst[i] <= val:
            if lst[i] == val:
                return i
            i += 1
        return -1
    
if __name__ == "__main__":
    lst = [1,2,3,4,5,6,7,8,9]
    value = 5
    f = JumpSearch(lst,value)
    print(f.jump_search())
    
    
