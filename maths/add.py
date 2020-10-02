if __name__ == "__main__":
    
    N = int(input("How many numbers you want to add:"))
    
    result = 0
    i = 0
    
    while i < N:
    
        number = input("Enter your number:")
        try:
            number = int(number)
        except:
            print("Enter only numbers")   
        else:
            result += number
            i += 1    
            




    print(f"The total sum is {result}")
