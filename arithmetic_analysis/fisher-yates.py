# Python Program to shuffle a given array 
import random 
  
# A function to generate a random permutation of arr[] 
def randomize (arr, n): 
    # Start from the last element and swap one by one. We don't 
    # need to run for the first element that's why i > 0 
    for i in range(n-1,0,-1): 
        # Pick a random index from 0 to i 
        j = random.randint(0,i+1) 
  
        # Swap arr[i] with the element at random index 
        arr[i],arr[j] = arr[j],arr[i] 
    return arr 
  
# Driver program to test above function. 
arr = [1, 2, 3, 4, 5, 6, 7, 8] 
n = len(arr) 
print(randomize(arr, n)) 