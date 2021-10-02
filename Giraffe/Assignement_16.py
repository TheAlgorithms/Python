#assignment 16
#finding sum of odd factors of a number
def Odd_factors_Sum(n):
    factor_sum = 0
    for i in range(1,int(n+1)):
        if n % i == 0 and i % 2 == 1 :
            factor_sum = factor_sum + i
    print("The sum of odd factors of the given number is: ", factor_sum)
"""End of Function"""
Reply = "Y"
while Reply == "Y" or Reply == "y":
    Number = int(input("Enter the number whose sum of factors you want: "))
    Odd_factors_Sum(Number)
    Reply = input("Press Y to continue or Press any other key to exit: ")
