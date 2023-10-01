# using kadane's algorithm - we initialize an current and a maxtill now, maxtill now stores only when current is positive and current will keep on adding the elements of the array and maxtill will store only when current is positive 
#so there are overall 3 loops. to add all elements to current and second is to check wheather curr is positive or negative and then assigning it to maxtill now

#----------------CODE--------------------#
nums = [-2,1,-3,4,-1,2,1,-5,4]
n= len(nums)
curr=0
maxtillnow=0
for i in range(n):
    curr+=nums[i]
    maxtillnow=max(curr,maxtillnow)
    if curr<0:
        curr=0
return maxtillnow

#--- this have a limitation that it ignores negative values, to include negative sums too we can use-----------#

curr=0
maxtillnow= -inf #negative infinity
for c in nums:
    curr= max(c,curr+c)
    maxtillnow= max(curr,maxtillnow)
return maxtillnow
