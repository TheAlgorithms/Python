import functools
"""
Graham Scan is an algortihm to find the points included in the
convex hull of any set of points.

A convex hull can be visualized as followed:
So you have dart board full of darts. Now try to wrap
a rubber band around all of the darts. The shape created
with the rubber band is the convex hull. The points that
touch the rubber band are include in the convex hull.

For doctests, run the commands:
python -m doctest -v graham_scan.py
or
python3 -m doctest -v graham_scan.py

For manual testing:
python graham_scan.py

"""
def graham_scan(points):
  """
  A graham scan is clever algorithm to find the convex hull of
  any set of points.

  :param points: list with length >= 3 of points: [x, y]

  :return: list of points included in convex hull

  Examples:
  >>> graham_scan([(0.0, 0.0), (1.0, 0.0), (1.0, 1.0), (0.0, 1.0), (0.5, 0.5)])
  [(0.0, 0.0), (1.0, 0.0), (1.0, 1.0), (0.0, 1.0)]

  >>> graham_scan([(0.0, 0.0), (0.0, 1.0), (0.0, 4.0), (1.0, 1.0), (-1.0, -1.0)])
  [(-1.0, -1.0), (1.0, 1.0), (0.0, 4.0)]

  >>> graham_scan([(732.0, 590.0), (415.0, 360.0), (276.0, 276.0), (229.0, 544.0), (299.0, 95.0)])
  [(229.0, 544.0), (299.0, 95.0), (732.0, 590.0)]

  """

  start = min(points, key=lambda p: (p[0], p[1]))
  points.pop(points.index(start))

  #Next, sort the points by the slope created with the start point.
  #This will put the points in counter-clockwise order
  points.sort(key=lambda p: (slope(p,start), -p[1], p[0]))

  hull = [start]

  #Add each point in the counter-clockwise order.

  #If the additional point creates a clockwise (concave) section,
  #then it is not included in the hull. (remove it)
  for p in points:
    hull.append(p)
    while len(hull) > 2 and cross(hull[-3],hull[-2],hull[-1]) < 0:
      hull.pop(-2)

  return hull

def slope(p1, p2):
  if p1[0] == p2[0]:
    return float('inf')
  return (p2[1]-p1[1]) / (p2[0]-p1[0])

def cross(p1, p2, p3):
  return (p2[0] - p1[0]) * (p3[1] - p1[1]) - (p2[1] - p1[1]) * (p3[0] - p1[0])




if __name__ == '__main__':
  try:
    raw_input          # Python 2
  except NameError:
    raw_input = input  # Python 3

  user_input = raw_input("Input points in the following format: x1 y1 x2 y2... ").strip()
  vals = list(map(float, user_input.split(" ")))
  points = [(vals[2 * i], vals[2*i+1]) for i in range(len(vals)//2)]
  ans = ", ".join(list(map(str, graham_scan(points))))
  print("Points in Convex Hull:", ans)




