'''Online Reference: https://www.geeksforgeeks.org/insertion-sort/ '''
def insertionSort(arr):
    #we 1st loop over the items
    for i in range(1,len(arr)-1):
        key= arr[i]
        j=i-1 #so j starts from 1st element
        while j>=0 and key<arr[j]:
            arr[j+1]= arr[j] #shifting to right to make room for key
            j=j-1
        else:
            arr[j+1]=key
    return arr

arr = [6,5,3,1,8,7,2,4]
print(insertionSort(arr))