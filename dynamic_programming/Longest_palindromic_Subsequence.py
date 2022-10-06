
def longestPalindrome(s):
    #dp[i][j] means whether s[i] to s[j] is a panlindrome

    dp=[[False for i in range(len(s))] for j in range(len(s))]      # act as base case
    for i in range(len(s)):
        dp[i][i]=True
    maxl=1
    begin=0                     #bottom up DP always start from base case, so we will scan backward
    for i in range(len(s)-1,-1,-1):
        for j in range(i+1,len(s)):        
            if s[i]==s[j]:      #if i+1=j and they are same character,of course this is a panlindrome
                if j-i==1:
                    dp[i][j]=True
                else:                   #if the substring between i and j are panlindrome    
                    dp[i][j]=dp[i+1][j-1]   
            if dp[i][j]:                   #update the result
                if j-i+1>maxl:
                    maxl=j-i+1
                    begin=i

    return s[begin:begin+maxl]

s = "ababas"
answer = longestPalindrome(s)