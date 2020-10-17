class Solution:
    def countSubstrings(self, s: str) -> int:
        l = []
        for itr in range(len(s)):
            for itr2 in range(itr+1,len(s)+1):
                #print(s[itr:itr2])
                st = s[itr:itr2]
                if(st == st[::-1]):
                    l.append(st)
        return(len(l))
