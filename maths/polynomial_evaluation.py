def evaluate_poly(poly, x):
    """
        Objective: Computes the polynomial function for a given value x. 
                Returns that value. 
        Input Prams: 
            poly: tuple of numbers - value of cofficients
            x: value for x in f(x)
        Return: value of f(x)

        >>> evaluate_poly((0.0, 0.0, 5.0, 9.3, 7.0), 10)
        79800.0
    """

    return sum(c * (x ** i) for i, c in enumerate(poly))


if __name__ == "__main__":
    """
        Example: poly = (0.0, 0.0, 5.0, 9.3, 7.0)  # f(x) = 7.0x^4 + 9.3x^3 + 5.0x^2 
                 x = -13
                 print (evaluate_poly(poly, x))  # f(-13) = 7.0(-13)^4 + 9.3(-13)^3 + 5.0(-13)^2 = 180339.9
    """
    poly = (0.0, 0.0, 5.0, 9.3, 7.0)
    x = 10
    print(evaluate_poly(poly, x))
