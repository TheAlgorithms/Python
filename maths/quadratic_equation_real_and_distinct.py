#Python Quadratic Equation solver for three terms
#Computes any possible solution for a qyuadratic equation
import math

def quadratics_equation_solver(a: int, b: int, c: int):
    """
    >>> quadratics_equation_solver(1,-2,1)
    Equation has one solution 1.0
    
    >>> quadratics_equation_solver(-1,4,-4)
    Equation has one solution 2.0
    """
    try:
        d = (b**2) - (4*a*c) #this computes the square of the number minus 4 times the values of a and c from the quadratic formula
        if d < 0:
            print("Equation has no real roots")
        elif d == 0:
            x = (-b + math.sqrt(d)) / (2 * a)
            round(x, 4)
            print(f"Equation has one solution {x}")
        else:
            x1 = (-b + math.sqrt(d)) / (2 * a)
            x2 = (-b - math.sqrt(d)) / (2 * a)
            print(f"Equation has two solutions {round(x1, 4)} and  {round(x2, 4)}")
            return x1,x2
    except: #if value passed is not an integer
        if not type(a,b,c) is int:
            raise TypeError("value must be of type int only")


def main():
    quadratics_equation_solver(1,-2,1)

if __name__ == '__main__':
    main()
