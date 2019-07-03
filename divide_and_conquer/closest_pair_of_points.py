"""
The algorithm finds distance btw closest pair of points in the given n points.
Approach used -> Divide and conquer 
The points are sorted based on Xco-ords 
& by applying divide and conquer approach, 
minimum distance is obtained recursively.

>> closest points lie on different sides of partition
This case handled by forming a strip of points 
whose Xco-ords distance is less than closest_pair_dis
from mid-point's Xco-ords.
Closest pair distance is found in the strip of points. (closest_in_strip)

min(closest_pair_dis, closest_in_strip) would be the final answer.
 
Time complexity: O(n * (logn)^2)
"""


import math 


def euclidean_distance_sqr(point1, point2):
    return pow(point1[0] - point2[0], 2) + pow(point1[1] - point2[1], 2)


def column_based_sort(array, column = 0):
    return sorted(array, key = lambda x: x[column])
    

def dis_between_closest_pair(points, points_counts, min_dis = float("inf")):
    """ brute force approach to find distance between closest pair points

    Parameters : 
    points, points_count, min_dis (list(tuple(int, int)), int, int) 
    
    Returns : 
    min_dis (float):  distance between closest pair of points

    """

    for i in range(points_counts - 1):
        for j in range(i+1, points_counts):
            current_dis = euclidean_distance_sqr(points[i], points[j])
            if current_dis < min_dis:
                min_dis = current_dis
    return min_dis


def dis_between_closest_in_strip(points, points_counts, min_dis = float("inf")):
    """ closest pair of points in strip

    Parameters : 
    points, points_count, min_dis (list(tuple(int, int)), int, int) 
    
    Returns : 
    min_dis (float):  distance btw closest pair of points in the strip (< min_dis)

    """

    for i in range(min(6, points_counts - 1), points_counts):
        for j in range(max(0, i-6), i):
            current_dis = euclidean_distance_sqr(points[i], points[j])
            if current_dis < min_dis:
                min_dis = current_dis
    return min_dis


def closest_pair_of_points_sqr(points, points_counts):
    """ divide and conquer approach

    Parameters : 
    points, points_count (list(tuple(int, int)), int) 
    
    Returns : 
    (float):  distance btw closest pair of points 

    """

    # base case
    if points_counts <= 3:
        return dis_between_closest_pair(points, points_counts)
    
    # recursion
    mid = points_counts//2
    closest_in_left = closest_pair_of_points(points[:mid], mid)
    closest_in_right = closest_pair_of_points(points[mid:], points_counts - mid)
    closest_pair_dis = min(closest_in_left, closest_in_right)
    
    """ cross_strip contains the points, whose Xcoords are at a 
    distance(< closest_pair_dis) from mid's Xcoord
    """

    cross_strip = []
    for point in points:
        if abs(point[0] - points[mid][0]) < closest_pair_dis:
            cross_strip.append(point)

    cross_strip = column_based_sort(cross_strip, 1)
    closest_in_strip = dis_between_closest_in_strip(cross_strip, 
                     len(cross_strip), closest_pair_dis)
    return min(closest_pair_dis, closest_in_strip)

    
def closest_pair_of_points(points, points_counts):
    return math.sqrt(closest_pair_of_points_sqr(points, points_counts))


points = [(2, 3), (12, 30), (40, 50), (5, 1), (12, 10), (0, 2), (5, 6), (1, 2)]
points = column_based_sort(points)
print("Distance:", closest_pair_of_points(points, len(points)))


