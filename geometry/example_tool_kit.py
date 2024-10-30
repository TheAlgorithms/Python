# examples/example_usage.py
from geometry_tool_kit import GeometryToolkit

# Define points for geometric analysis
points = [(0, 0), (10, 0), (1, 1), (0, 1)]

# Initialize the toolkit with points
toolkit = GeometryToolkit(points)


# Example: Display the convex hull
toolkit.convex_hull()

# Example: Display the Voronoi diagram
toolkit.voronoi_diagram()

# Example: Calculate the area of a polygon
print("Area of polygon:", toolkit.calculate_area())

# Example: Visualize points in 3D space
toolkit.visualize_3d()

# Example: Create a symbolic circle
circle = toolkit.create_circle((0, 0), 1)
print("Symbolic circle:", circle)
