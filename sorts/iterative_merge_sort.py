"""
Implementation of iterative merge sort in python
Author: Aman Gupta

"""

def merge(low,mid,high,inputlist):
    """
    sorting left-half and right-half individually
    then merging them into result
    """
    result = []
    left , right = inputlist[low:mid] , inputlist[mid:high+1]
    while left and right:
        result.append((left if left[0] <= right[0] else right).pop(0))
    inputlist[low:high+1] = result + left + right
    return inputlist

# iteration over the unsorted list
def iter_merge_sort(inputlist):


    if len(inputlist) <= 1:
        return inputlist

    # iteration for two-way merging
    p=2
    while(p<len(inputlist)):
        #getting low, high and middle value for merge-sort of single list
        for i in range(0,len(inputlist),p):
            low = i
            high = i+p-1
            mid = (low+high+1)//2
            inputlist = merge(low,mid,high,inputlist)
        #final merge of last two parts
        if(p*2>=len(inputlist)):
            mid = i
            inputlist = merge(0,mid,len(inputlist)-1,inputlist)

        p *= 2

    return inputlist

if __name__ == "__main__":
    unsorted = list(map(int,input("Enter numbers separated by a comma:\n").split(',')))
    print(*iter_merge_sort(unsorted), sep=",")
