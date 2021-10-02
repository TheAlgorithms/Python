#Kadane's algorithm is used to find the largest subarray sum in any given array.
#Time Complexity-O(n)
#Functioning- Initially the largest_sum and current_sum are initialized to 0,
#then we basically calculate running sum from left to right
#and at any point if the current sum is negative we assume it to be zero,
#with every maximum achieved in current_sum the maximum_sum gets updated
#author:Manish Tiwari
def kadane_algo(arr,size):
    
    current_sum = arr[0]
    largest_sum = 0
    
    for i in range(0, size):
        largest_sum = largest_sum + arr[i]
        if largest_sum < 0:
            largest_sum = 0
        
        
        elif (current_sum < largest_sum):
            current_sum = largest_sum
            
    return current_sum

arr = [-2, -3, 4, -1, -2, 5, -3] #array
print("Max subarray sum is" , kadane_algo(arr,len(arr))) #output