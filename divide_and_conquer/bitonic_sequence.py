"""
Given an array A[1..n], which is a bitonic sequence. Also this
sequence can be rotated left or right. I have to find the smallest 
element in this bitonic sequence.

In this implementation, I provide a divide-and-conquer
algorithm.
"""

def bitonic(nums):
    if(len(nums)==1):
        return nums[0]
    if(len(nums)==2):
        return min(nums[0],nums[1])
    n=len(nums)
    
    start = 0
    end= len(nums)-1
    while(start<=end):
        mid=(start+end)//2
        #res= float('inf')
        if(mid==0):
            if(nums[0]<nums[n-1] and nums[0]<nums[1]):
                #no rotation
                return nums[0]
            else:
                start=mid+1
        elif(mid==n-1):
            if(nums[n-1]<nums[n-2] and nums[0]>nums[n-1]):
                #decreasing and end< start (231)
                return nums[n-1]
            else:
                end=mid-1
        else:
            currval=nums[mid]
            leftval=nums[mid-1]
            rightval=nums[mid+1]
            #mid between 1 and n-2
            if(nums[0]>nums[-1]):
                #inc dec inc
                if(currval<leftval and currval<rightval):
                    return currval
                elif(currval>leftval and currval>rightval):
                    #bitonic point
                    start=mid+1
                elif(currval<rightval):
                        #increasing first part--recurse right
                    if(currval>nums[0]):
                        start=mid+1
                    else:
                            #increasing second part ---recurse left
                        end=mid-1
                elif(currval>rightval):
                    #decreasing ---recurse right
                    start=mid+1
            elif(nums[0]<nums[-1]):
                    #decreasing increasing decreasing
                if(currval<leftval and currval<rightval):
                    return currval
                elif(currval>leftval and currval>rightval):
                    #bitonic point
                    end=mid-1
                elif(currval>rightval):
                    #decreasing first part--recurse right
                    if(currval<nums[0]):
                        start=mid+1
                    else:
                        #decreasing second part ---recurse left
                        end=mid-1
                elif(currval<rightval):
                    #increasing ---recurse right
                    end=mid-1
        
        
def main():
    nums=[1, 4, 6, 8, 3,-5,-9]
    #[3,1,2] right
    #[2,3,1] left
    a=bitonic(nums)
    print(a)
    
if __name__=="__main__": 
    main() 
