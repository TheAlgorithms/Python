# QUESTION : Given a positive integer 'n', find and return the minimum number of steps 
    # that 'n' has to take to get reduced to 1. You can perform
        #  any one of the following 3 steps:
# 1.) Subtract 1 from it. (n = n - ­1) ,
# 2.) If n is divisible by 2, divide by 2.( if n % 2 == 0, then n = n / 2 ) ,
# 3.) If n is divisible by 3, divide by 3. (if n % 3 == 0, then n = n / 3 ). 

from sys import stdin
from sys import maxsize as MAX_VALUE



def countMinStepsToOne(n,dp) :
    if n == 1:
        return 0

    if dp[n-1] == -1:
        ans1 = countMinStepsToOne(n-1,dp)
        dp[n-1] = ans1
    else:
        ans1 = dp[n-1]

    ans2 = n-1

    if n%2==0:
        if dp[n//2] == -1:
            ans2 = countMinStepsToOne(n//2,dp)
            dp[n//2] = ans2
        else:
            ans2 = dp[n//2]

    ans3 = n-1

    if n%3 == 0:
        if dp[n//3] == -1:
            ans3 = countMinStepsToOne(n//3,dp)
            dp[n//3] = ans3
        else:
            ans3 = dp[n//3]

    return 1 + min(ans1,ans2,ans3)


#main
n = int(stdin.readline().rstrip())
dp = [-1 for i in range(n)]
print(countMinStepsToOne(n,dp))
