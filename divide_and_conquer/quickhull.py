'''
Quick-hull-
Created on 22/7/2020
---description---
Quick-hull is a divide and conquer algorithm designed to construct a convex hull.
it is called Quick-hull as its logic is closer to Quick-sort.
Complexity: O(n**2)
---------input---------
-->list of points in list format
---------output--------
--> list of end-points
>>> quickhull(a = [[1,3],[1,1],[2,2],[4,4],[0,0],[1,2],[3,1],[3,3]])
the hull endpoints are  [[0, 0], [1, 3], [4, 4], [3, 1]]

>>> quickhull(a = [[1,3],[1,1],[2,2],[4,4],[0,0],[1,2],[3,1],[3,3],[1,5],[3,2],[5,5],[4,0]])
the hull endpoints are  [[0, 0], [1, 5], [5, 5], [4, 0]]

>>> quickhull(a = ['lol'])
check the input format: its should be list of lists: [[5,6],[4,8]...]
given format:  ['lol']
'''

def min_max_x(a):
    #intial minimum and maximum
    min_x = -1 
    max_x = 0
    for i in range(len(a)):
        if a[i][0] < min_x or min_x == -1:
            #updating min value and holding the point
            min_x = a[i][0]
            min_x_l = a[i]
        if a[i][0] > max_x:
            #updating max value and holding the point
            max_x = a[i][0]
            max_x_l = a[i]
    return min_x_l,max_x_l
def dist(p0,p1,i):
    return abs(((i[1]-p0[1])*(p1[0]-p0[0]))-((p1[1]-p0[1])*(i[0]-p0[0])))

def left_right_division(a):
    #divides the given points into two lists
    p0,p1 = min_max_x(a)
    left_points = []
    right_points = []
    for i in a:
        if i != p0 or i != p1:
            val = ((i[1]-p0[1])*(p1[0]-p0[0]))-((p1[1]-p0[1])*(i[0]-p0[0]))
            if val>0 or val == 0:
                left_points.append(i)
            elif val<0:
                right_points.append(i)
    return left_points,right_points
def max_point(points,a):
    #finds the max perpendicular distance point from the division line
    p0,p1 = min_max_x(a)
    max_height = 0
    point_max = []
    for i in points:
        current = dist(p0,p1,i)
        if current>max_height and current != 0:
            max_height = current
            point_max = i
    return point_max
        
def quickhull(a:list(list())):
    #creating final set of hull end-points
    try:
        randcheck=random.randint(0,len(a)-1)
        if isinstance(a, list) != 1: raise TypeError
        if isinstance(a[randcheck],list) != 1: raise TypeError
        if isinstance(a[randcheck][0], int) !=1: raise TypeError
        p0,p1 = min_max_x(a)
        left_points,right_points = left_right_division(a)    
        hull = []
        hull.append(p0)
        hull.append(max_point(left_points,a))
        hull.append(p1)
        hull.append(max_point(right_points,a))
        print('the hull endpoints are ',hull)
    except TypeError:
        print('check the input format: its should be list of lists: [[5,6],[4,8]...]')
        print('given format: ',a)

    
#driver code
if __name__ == '__main__':
    import random
    import doctest
    doctest.testmod()