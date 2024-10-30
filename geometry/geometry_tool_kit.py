# geometry_toolkit.py
from shapely.geometry import Point, Polygon
from sympy import Circle, Point as SymPoint, Polygon as SymPolygon
import matplotlib.pyplot as plt
from scipy.spatial import Voronoi, ConvexHull
import pyvista as pv
import numpy as np


class GeometryToolkit:
    def __init__(self, points):
        self.points = points
        self.shapely_points = [Point(p) for p in points]
        self.sympy_points = [SymPoint(*p) for p in points]
        self.np_points = np.array(points)

    def convex_hull(self):
        """Visualize the convex hull of a set of points."""
        hull = ConvexHull(self.np_points)
        plt.plot(self.np_points[:, 0], self.np_points[:, 1], 'o')
        for simplex in hull.simplices:
            plt.plot(self.np_points[simplex, 0], self.np_points[simplex, 1], 'k-')
        plt.title("Convex Hull")
        plt.show()

    def voronoi_diagram(self):
        """Visualize the Voronoi diagram for a set of points."""
        vor = Voronoi(self.np_points)
        plt.plot(self.np_points[:, 0], self.np_points[:, 1], 'o')
        plt.voronoi_plot_2d(vor)
        plt.title("Voronoi Diagram")
        plt.show()

    def calculate_area(self):
        """Calculate the area of a polygon formed by points (if applicable)."""
        sym_polygon = SymPolygon(*self.sympy_points)
        return sym_polygon.area

    def visualize_3d(self):
        """Visualize points in a 3D space."""
        plotter = pv.Plotter()
        plotter.add_mesh(pv.PolyData(self.np_points), color="red", point_size=10)
        plotter.show()

    def create_circle(self, center, radius):
        """Create a symbolic circle with a given center and radius."""
        return Circle(SymPoint(*center), radius)
