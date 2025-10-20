"""Drone's Domain
We call a square valid on a 2d coordinate plane if it satisfies the following conditions:

Area of the square should be equal to 1.
All vertices of the square have integer coordinates.
All vertices of square lie inside or on the circle of radius r, centered at origin.
Given the radius of circle r, count the number of different valid squares. Two squares are different if atleast one of the vertices of first square is not a vertex of second square.

Input Format
The first line contains the integer r, the radius of the circle.

Constraints
1 <= r <= 2 * 10^5
Use a 64-bit integer type (like long long in C++ or long in Java) for sum calculations to prevent overflow.

Output Format
Print the number of different squares in this circle of radius r.

Sample Input 1
Sample Output 0"""

# Title: Count Axis-Aligned Unit Squares in Circle
# Description: Counts the number of squares with area 1, integer vertices, fully inside a circle of radius r.

import sys
import math

r=int(sys.stdin.readline())
count=0
for x in range(-r,r):
    for y in range(-r,r):
        # Check all four vertices are inside the circle
        if (x*x+y*y<=r*r and
            (x+1)*(x+1)+y*y<=r*r and
            x*x+(y+1)*(y+1)<=r*r and
            (x+1)*(x+1)+(y+1)*(y+1)<=r*r):
            count += 1

print(count)
