def newton_raphson(f, df, x0, tol, max_iter):
    x = x0
    for i in range(max_iter):
        x_next = x - f(x) / df(x)
        if abs(x_next - x) < tol:
            return x_next
        x = x_next
    return x

if __name__ == "__main__":
    def my_function(x):
        return x**2 - 4
    
    def my_derivative(x):
        return 2 * x
    
    initial_guess = 3
    tolerance = 1e-6
    max_iterations = 100
    
    estimated_root = newton_raphson(my_function, my_derivative, initial_guess, tolerance, max_iterations)
    
    print(f"Estimated root: {estimated_root}")
