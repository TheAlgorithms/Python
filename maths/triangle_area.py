# Function to calculate the area of a triangle
def calculate_triangle_area(base, height):
    area = 0.5 * base * height
    return area


# Get input for the base length and height from the user
try:
    base = float(input("Enter the base length of the triangle: "))
    height = float(input("Enter the height of the triangle: "))

    # Check if both base and height are positive numbers
    if base > 0 and height > 0:
        triangle_area = calculate_triangle_area(base, height)
        print(f"The area of the triangle is: {triangle_area}")
    else:
        print("Base and height must be positive numbers.")
except ValueError:
    print("Invalid input. Please enter valid numbers for the base and height.")
