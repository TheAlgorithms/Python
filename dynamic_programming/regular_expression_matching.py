"""
Given an input string (s) and a pattern (p), implement regular expression matching with support for '.' and '*' where: 

'.' Matches any single character.
'*' Matches zero or more of the preceding element.
The matching should cover the entire input string (not partial).

https://leetcode.com/problems/regular-expression-matching/
"""
def isMatch(self, s: str, p: str) -> bool:
        dp = [[0 for i in range(len(p)+1)] for j in range(len(s)+1)]
        
        dp[0][0] = 1
        
        for j in range(2,len(p)+1):
            if(p[j-1] == "*"):
                dp[0][j] = dp[0][j-2]
                
        
        
        for i in range(1,len(s)+1):
            for j in range(1,len(p)+1):
                if(p[j-1]==s[i-1] or p[j-1]=="."):
                    dp[i][j] = dp[i-1][j-1]
                    
                elif(j>1 and p[j-1]=="*"):
                    if (p[j-2] =="." or s[i-1]==p[j-2]):
                        dp[i][j] = dp[i][j-2] or dp[i-1][j]
                    else:
                        dp[i][j] = dp[i][j-2]  
       
        return True if dp[-1][-1] == 1 else False
 
 if __name__ == "__main__":
    str1 = input("Enter the first string: ")
    str2 = input("Enter the second string: ")
    solution = isMatch(str1,str2)
    print(solution)

