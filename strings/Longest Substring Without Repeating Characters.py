'''
LeetCode:3
Longest Substring Without Repeating Characters

Input 1:
s="abcabcbb"
output: 3
Explanation: The answer is "abc", with the length of 3.
-------------
Input 2:
s="bbbbb"
output: 1
-------------
Input 3:
s="pwwkew"
output: 3
'''


def lengthOfLongestSubstring(s):
    l=0
    res=0
    charset=set()
    for r in range(len(s)):
        while(s[r] in charset):
            charset.remove(s[l])
            l+=1  
        charset.add(s[r])
        res=max(res,r-l+1)
    return (res)
s=input()
print(lengthOfLongestSubstring(s))

