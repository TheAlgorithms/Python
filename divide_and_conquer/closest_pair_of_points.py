"""
The algorithm finds distance between closest pair of points in the given n points.
Approach: Divide and conquer 
The points are sorted based on x-cords 
& by applying divide and conquer approach, 
minimum distance is obtained recursively.

Edge case: closest points lie on different sides of partition
This case handled by forming a strip of points 
which are at a distance (< closest_pair_dis) from mid-point.
(It is a proven that strip contains at most 6 points)
And brute force method is applied on strip to find closest points. 

Time complexity: O(n * (logn) ^ 2)
"""


import math 


def euclidean_distance(point1, point2):
    return math.sqrt(pow(point1[0] - point2[0], 2) + pow(point1[1] - point2[1], 2))


def column_based_sort(array, column = 0):
    return sorted(array, key = lambda x: x[column])
    

#brute force approach to find distance between closest pair points
def dis_btw_closest_pair(points, no_of_points, min_dis = float("inf")):
    for i in range(no_of_points - 1):
        for j in range(i+1, no_of_points):
            current_dis = euclidean_distance(points[i], points[j])
            if current_dis < min_dis:
                min_dis = current_dis
    return min_dis


#divide and conquer approach
def closest_pair_of_points(points, no_of_points):
    # base case
    if no_of_points <= 3:
        return dis_btw_closest_pair(points, no_of_points)
    
    #recursion
    mid = no_of_points//2
    closest_in_left = closest_pair_of_points(points[:mid], mid)
    closest_in_right = closest_pair_of_points(points[mid:], no_of_points - mid)
    closest_pair_dis = min(closest_in_left, closest_in_right)
    
    #points which are at a distance (< closest_pair_dis) from mid-point
    cross_strip = []
    for point in points:
        if abs(point[0] - points[mid][0]) < closest_pair_dis:
            cross_strip.append(point)

    cross_strip = column_based_sort(cross_strip, 1)
    closest_in_strip = dis_btw_closest_pair(cross_strip, 
                     len(cross_strip), closest_pair_dis)
    return min(closest_pair_dis, closest_in_strip)
    

points = [[2, 3], [12, 30], [40, 50], [5, 1], [12, 10]]
points = column_based_sort(points)
print("Distance:", closest_pair_of_points(points, len(points)))


