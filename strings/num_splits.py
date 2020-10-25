"""
You are given a string s, a split is called good if you can split s into
2 non-empty strings p and q where its concatenation is equal to s and
the number of distinct letters in p and q are the same.

Return the number of good splits you can make in s. 
"""
from collections import Counter, defaultdict

def num_splits(self, s: str):
        """
        >> num_splits("aacaba")
        2
        >> num_splits("abcd")
        1
        >> num_splits("aaaaa")
        4
        """
        ans = 0
        rightSplit = Counter(s)
        leftSplit = defaultdict(int)
        
        leftCount = 0
        rightCount = len(rightSplit)
        
        for ch in s:
            rightSplit[ch] -= 1
            leftSplit[ch] += 1
            
            if rightSplit[ch] == 0:
                rightCount -= 1
            
            leftCount = len(leftSplit)
            
            if leftCount == rightCount:
                ans += 1
        
        return ans


if __name__ == "__main__":
    import doctest

    doctest.testmod()
