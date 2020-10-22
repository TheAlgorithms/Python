
'''
  Test cases:

  find_minimum_change(987)
  500 100 100 100 100 50 20 10 50 2
  find_minimum_change(500)
  500
  find_minimum_change(0)
  The total value cannot be zero or negetive
  find_minimum_change(-96)
  The total value cannot be zero or negetive
  find_minimum_change(56)
  50 5 1 

'''
def find_minimum_change(V): 
    total_value =  int(V) #store the value of v as an integer so that it can be used for comparision
   
    # All denominations of Indian Currency 
    denominations = [1, 2, 5, 10, 20, 50, 100, 500, 2000] 
    length = len(denominations) #find the total length of the array so as to transverse the array in the following code
      
    # Initialize Result 
    answer = [] 
  
    # Traverse through all denominations
    i = length - 1 # as the array values range from 0 to n-1 we initialize the value of i to n-1
    while(i >= 0): #repeat until i is does not reach zero so as to lead to our answer
          
        # Find denominations that will finally lead the "total_value" to zero giving us the set of values or number of nodes we need
        while (int(total_value) >= int(denominations[i])): 
            total_value -= int(denominations[i]) #subtract the current denomination value from total_value if the denomination is greater than the current total_value
            answer.append(denominations[i])   #append the answer in the "answers" array
  
        i -= 1 #decrement the i value so as to move to the lower denomination
  
    # Print result 
    for i in range(len(answer)): 
        print(answer[i], end = " ") 
  
# Driver Code 
if __name__ == '__main__': 
    n = input("Enter the change you want to make in Indian Currency: ") #get input from user to make the change they want
    if int(n) == 0 or int(n) < 0:  #it cannot be 0 or negetive
      print("The total value cannot be zero or negetive.")
    else:
      print("Following is minimal number", 
          "of change for", n, ": ", end = "") 
      find_minimum_change(n) 
     
