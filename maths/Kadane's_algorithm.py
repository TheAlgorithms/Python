"""
    Kadane's algorithm to get maximum subarray sum
    Please enter the decimal values only and use spaces as seperator
"""
def negative_exist(arr):

    """
     checks wether the max value in -ve or not
     eg :- 
      arr = [-2,-8,-9]
      so max element is negative i.e. -2
      so answer is -2

      and if max value is positive it will return 0
      and then apply the kadane's algorithm
      eg :- 
      arr = [2,8,-9]
      positive number exist so it will return 0
    """
    max=arr[0]
    for i in arr:
        if(i>=0):
            return 0;
        elif(max<=i):
            max=i
    return max 


def kadanes_implementation(arr):


    """
     if negative_exist return 0 than this function will execute
     else it will return the value return by negative_exist function
     
     Eg :- 
     arr = [2,3,-9,8,-2]
       initially the value of max_sum = 0 and max_till_element is 0
       than when max_sum less than max_till particular element it will assign that value to max_sum
       and when value of max_till_sum is less than 0 it will assign 0 to i
       and after whole process it will return the value

       So th output for above arr is :- 8
    """
    if(negative_exist(arr)<0):
        return negative_exist(arr)

    max_sum = 0
    max_till_element=0
    
    for i in arr:
        max_till_element=max_till_element+i
        if max_sum <= max_till_element:
            max_sum = max_till_element
        if max_till_element < 0:
            max_till_element = 0
    
    return max_sum



if __name__ == "__main__":
    try:
        print("Enter the element of array with spaces  :- ")
        arr = list(map(int, input().split()))
        print(kadanes_implementation(arr))
    except ValueError:
        print("Please,enter decimal values")
    