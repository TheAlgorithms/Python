import math
from typing import List

def lagrange_interpolation(x: List[float], y: List[float], value: float) -> float:
    """
    Calculate the Lagrange interpolation of a function based on provided data points.

    Parameters:
        x (List[float]): List of x-values (independent variable).
        y (List[float]): List of corresponding y-values (dependent variable).
        value (float): The value at which to interpolate the function.

    Returns:
        float: The interpolated value of the function at the specified 'value'.

    for eg.:
        
        >>> x = [5, 6, 9, 11]
        >>> y = [12, 13, 14, 16]
        >>> lagrange_interpolation(x, y, 10)
        14.666666666666666

    """
    ans = 0
    n = len(x)

    for i in range(n):  
        term = y[i]
        for j in range(n):
            if i != j:
                term *= (value - x[j]) / (x[i] - x[j])
        ans += term

    return ans

def main():
    """
    Main function for performing Lagrange interpolation.
    Takes user input for data points and the value to interpolate, then displays the interpolated result.
    """
    n = int(input("Enter the number of values: "))
    x = []
    y = []

    print("Enter the values of x in a list: ")
    x = list(map(float, input().split()))

    print("Enter the values of corresponding y: ")
    y = list(map(float, input().split()))

    value_to_interpolate = float(input("Enter the value to interpolate:"))

    interpolated_value = lagrange_interpolation(x, y, value_to_interpolate)

    print(f"The interpolated value at {value_to_interpolate} is {interpolated_value}")

if __name__ == "__main__":
    main()
