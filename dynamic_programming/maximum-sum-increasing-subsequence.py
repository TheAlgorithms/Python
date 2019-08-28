#############################
# Author: Ujjal Das( github.com/ujjaldas132)
# File: lis.py
# comments:Given an array A . Fin d the sum of maximum sum increasing subsequence of the given array.
#           if A=[1 101 2 3 100 4 5] then answer shold be 106>>>>>>1,2,3,100
#############################

def max_sum(a):
    n=len(a)
    
    sum_list=[a[0]]
    max_val=a[0]
    for i in range(1,n):
        temp=a[i]
        j=i-1
        while j>-1:
            if a[j]<a[i]:
                if temp<a[i]+sum_list[j]:
                    temp=a[i]+sum_list[j]
                if sum_list[j]==temp:
                    #print("break",sum_list[j],i,j)
                    break
                    
            j-=1
        sum_list.append(temp)
        if temp>max_val:
            max_val=temp
            
    return max_val
    
a=[1,101,2,3,100,4,5]
print(max_sum(a))
