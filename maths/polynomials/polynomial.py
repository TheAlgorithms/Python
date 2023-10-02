# Import the Polynomial class from polynomial_manipulation.py
from polynomial_manipulation import Polynomial

# Create a polynomial
p = Polynomial([3, 2, 1])  # 3x^2 + 2x + 1

# Print the polynomial
print(p)

# Perform addition with another polynomial
p2 = Polynomial([2, 0, 1])  # 2x^3 + x
result_add = p.add(p2)
print(result_add)

# Perform multiplication with another polynomial
result_multiply = p.multiply(p2)
print(result_multiply)

# Run doctests
if __name__ == "__main__":
    import doctest

    doctest.testmod()
