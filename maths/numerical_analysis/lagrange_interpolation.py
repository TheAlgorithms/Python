def lagrange_interpolation(x: list[float], y: list[float], value: float) -> float:
    """
    Calculate the Lagrange interpolation of a function based on provided data points.

    Parameters:
        x (list[float]): List of x-values (independent variable).
        y (list[float]): List of corresponding y-values (dependent variable).
        value (float): The value at which to interpolate the function.

    Returns:
        float: The interpolated value of the function at the specified 'value'.

    Examples:
        >>> x = [5.0, 6.0, 9.0, 11.0]
        >>> y = [12.0, 13.0, 14.0, 16.0]
        >>> lagrange_interpolation(x, y, 10.0)
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
    Takes user input for data points and the value to interpolate,
    then displays the interpolated result.
    """
    n = int(input("Enter the number of values: "))
    x = []
    y = []

    print("Enter the values of x in a list:")
    for i in range(n):
        value = float(input())
        x.append(value)

    print("Enter the values of corresponding y:")
    for j in range(n):
        value = float(input())
        y.append(value)

    value_to_interpolate = float(input("Enter the value to interpolate:"))

    interpolated_value = lagrange_interpolation(x, y, value_to_interpolate)

    print(f"The interpolated value at {value_to_interpolate} is {interpolated_value}")

if __name__ == "__main__":
    main()
