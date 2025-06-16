#Giving the output 
def lucas_func(n):
    #PREDFINING THE VALUES
    a = 2
    b = 1
    
    if n == 0:
        return a
 
    # GENERATING THE NUMBER 
    for i in range(2, n + 1):
        c = a + b
        a = b
        b = c
    
    return b
    
# USER INPUT 
n = int(input("Enter the position n to find the nth Lucas Number: "))
print(f"The {n}th Lucas Number is: {lucas_func(n)}")

"""

THE OUTPUT:- 
Enter the position n to find the nth Lucas Number: 6
The 6th Lucas Number is: 18

"""