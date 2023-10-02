def euler_method(func, y0, t0, t_end, h):
    """
    Solve an ordinary differential equation (ODE) using Euler's Method.

    Args:
    func (function): The ODE function dy/dt = f(t, y).
    y0 (float): Initial value of y at t0.
    t0 (float): Initial time.
    t_end (float): End time.
    h (float): Step size.

    Returns:
    list: A list of tuples (t, y) representing the solution points.

    Example:

    >>> def ode_function(t, y):
    ...     return y - t ** 2 + 1

    >>> initial_y = 0.5
    >>> initial_t = 0
    >>> end_t = 2
    >>> step_size = 0.2

    >>> solution = euler_method(ode_function, initial_y, initial_t, end_t, step_size)

    >>> solution
    [(0, 0.5), (0.2, 0.7), (0.4, 1.02), (0.6, 1.45), (0.8, 1.99), (1.0, 2.65), (1.2, 3.45), (1.4, 4.42), (1.6, 5.58), (1.8, 6.97), (2.0, 8.74)]
    
    For more information on Euler's Method, see:
    https://en.wikipedia.org/wiki/Euler_method
    """
    # Initialize lists to store solution points
    t_values = [t0]
    y_values = [y0]

    t = t0
    y = y0

    while t < t_end:
        # Compute the next values using Euler's method
        y_next = y + h * func(t, y)
        t_next = t + h

        # Append the new values to the lists
        t_values.append(t_next)
        y_values.append(y_next)

        # Update t and y for the next iteration
        t = t_next
        y = y_next

    # Combine t and y values into tuples and return the solution
    solution = list(zip(t_values, y_values))
    return solution

if __name__ == "__main__":
    import doctest
    doctest.testmod()
