import math

def QuadraticEquation(a,b,c):
    """
    Prints the solutions for a quadratic equation, given the numerical coefficients a, b and c,
    for a*x*x + b*x + c.
    Ex.: a = 1, b = 3, c = -4
    Solution1 = 1 and Solution2 = -4
    """
    Delta = b*b - 4*a*c
    if a != 0:
        if Delta >= 0:
            Solution1 = (-b + math.sqrt(Delta))/(2*a)
            Solution2 = (-b - math.sqrt(Delta))/(2*a)
            print ("The equation solutions are: ", Solution1," and ", Solution2)
        else:
            """
            Treats cases of Complexes Solutions(i = imaginary unit)
            Ex.: a = 5, b = 2, c = 1
            Solution1 = (- 2 + 4.0 *i)/2 and Solution2 = (- 2 + 4.0 *i)/ 10
            """
            if b > 0:
                print("The equation solutions are: (-",b,"+",math.sqrt(-Delta),"*i)/2  and  (-",b,"+",math.sqrt(-Delta),"*i)/", 2*a)
            if b < 0:
                print("The equation solutions are: (",b,"+",math.sqrt(-Delta),"*i)/2  and  (",b,"+",math.sqrt(-Delta),"*i/",2*a)
            if b == 0:
                print("The equation solutions are: (",math.sqrt(-Delta),"*i)/2  and  ",math.sqrt(-Delta),"*i)/", 2*a)
    else: 
        print("Error. Please, coeficient 'a' must not be zero for quadratic equations.")
def main():
    a = 5
    b = 6
    c = 1

    QuadraticEquation(a,b,c) # The equation solutions are:  -0.2  and  -1.0
    
    
if __name__ == '__main__':
    main()
