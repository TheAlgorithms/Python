if __name__ == "__main__":
    
    N = int(input("How many numbers you want to add:"))
    
    result = 0
    i = 0
    
    while i < N:
           
        number = input("Enter your number:")
        """
        >> number = "5"
           result += 5
        """     
        
        """
        >> number = "s"
           print the exception
        """
        try:
            number = int(number)  # check input can be converted into number
        except Exception as e:
            print(e)   
        else:
            result += number      # add number in result and add 1 to i
            i += 1    
            




    print(f"The total sum is {result}")
