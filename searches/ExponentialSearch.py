'''
Exponential search is another search algorithm that can be implemented quite simply in Python, compared to jump search and Fibonacci search which are both a bit complex. It is also known by the names galloping search, doubling search and Struzik search.

Exponential search depends on binary search to perform the final comparison of values. The algorithm works by:
'''

#test input list
list1=[1,2,3,4,5,6,7,7,8,9]

#test input value
val=6


if list1[0] == val:
    print("0")
i = 1
#Finding range for binarySearch
while(i<len(list1) and list1[i]<=val):
        i = i * 2
min1=min(i,len(list1))
def binarySearch(data_list,low,high,value):

    if(high>= low):
        mid=int(low + ( high-low )//2)

        if data_list[mid] == value:
            return mid

        if data_list[mid] > value:
            return binarySearch(data_list,low,mid - 1,value)
        else:
            return binarySearch(data_list,mid + 1,high,value)
    
    if(high<low):
        return -1
    # Applying binary search for specified range
index=binarySearch(list1,i/2,min(i,len(list1)),val)
if(index==-1):
    print("Element not found")
else:
    print("Element found at index ",index)