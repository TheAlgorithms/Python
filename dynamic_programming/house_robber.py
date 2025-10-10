"""
Code for house robber problem LeetCode : 198 using dynamic programming (tabulation).
"""

### Question explanation:
# Given array of numbers which says how much money you can steel form houses.
# The only constraint is if you rob from adjacent houses, it will ring alarm to police.

### My Approach with DP:
# As starting with DP, I will explain the approach in recursion with memoization which is more intuitive.
# At each node in recursion, we have counter which True or False
# Starting from last house, we have 2 options 1) If choosen, counter=True will be passed in recursion.
#                                             2) If not choosen, counter=False will be passes in recursion.
# If choosen=True at current house means previous house is choose so you can't choose current house.
# If choosen=False at current house means it is not choosen, it means you have option to choose or not current house.
## Example nums=[1,2,3,1]

### Last index value   (1,  counter=False) (as we are starting from here we are free to choose)
#                         /          \
###            (3,counter=True)     (3,counter=False)     (counter=True mean 1 is choosen,so avoid 3)
#                      /                   /       \
###        (2,counter=False)            (2,True)  (2,False)
#  (here 2,False means 1 is choosen, so we avoid 3 and 
# as 3 is avoided now again we are free to choose at house 2)


## Note: dp[i][0]=>0 is True and 1 is False in convention.
def rob(nums):
    def helper(nums,dp,i,j):
        if i<0:
            return 0
        if dp[i][j]!=-1:
            return dp[i][j]
        if j==True:
            dp[i][0]=helper(nums,dp,i-1,False)
            return dp[i][0]
        else:
            dp[i][1] = max(nums[i] + helper(nums,dp,i-1,True), helper(nums,dp,i-1,False))
            return dp[i][1]
    dp=[[-1]*2 for _ in range(0,len(nums))]
    return helper(nums,dp,len(nums)-1,False)
    
if __name__ == "__main__":
    nums=[2,7,9,3,1]
    if not nums:                 
        print('The list is empty')
    else:
        max_amount=rob(nums)
        print(max_amount)


        
