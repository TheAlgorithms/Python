import random as rand
import matplotlib.pyplot as plt

def point_inside_outside(polygon,point):

    INT_MAX = 10000
    def onSegment(p:tuple, q:tuple, r:tuple) -> bool:
     
        if ((q[0] <= max(p[0], r[0])) &
            (q[0] >= min(p[0], r[0])) &
            (q[1] <= max(p[1], r[1])) &
            (q[1] >= min(p[1], r[1]))):
            return True
        return False
 
    def orientation(p:tuple, q:tuple, r:tuple) -> int:
        val = (((q[1] - p[1]) *(r[0] - q[0])) - ((q[0] - p[0]) * (r[1] - q[1])))
         
        if (val > 0):
            return 1
        elif (val < 0):
            return 2
        else:
            return 0
 
    def doIntersect(p1, q1, p2, q2):
        o1 = orientation(p1, q1, p2)
        o2 = orientation(p1, q1, q2)
        o3 = orientation(p2, q2, p1)
        o4 = orientation(p2, q2, q1)

        if (o1 != o2) and (o3 != o4):
            return True

        if (o1 == 0) and (onSegment(p1, p2, q1)):
            return True

        if (o2 == 0) and (onSegment(p1, q2, q1)):
            return True

        if (o3 == 0) and (onSegment(p2, p1, q2)):
            return True

        if (o4 == 0) and (onSegment(p2, q1, q2)):
            return True
 
        return False

    def is_inside_polygon(points:list, p:tuple) -> bool:
     
        n = len(points)

        if n < 3:
            return False

        extreme = (INT_MAX, p[1])
        count = i = 0
     
        while True:
            next = (i + 1) % n

            if (doIntersect(points[i], points[next], p, extreme)):

                if orientation(points[i], p, points[next]) == 0:
                    return onSegment(points[i], p, points[next])
                count += 1
            i = next
            if (i == 0):
                break
        return (count % 2 == 1)
    return is_inside_polygon(points = polygon, p = point)

randomXY = []
X=[]
Y=[]
for number in range(1000):
    XY = rand.uniform(2,9),rand.uniform(2,9)
    randomXY.append(XY)

for points in randomXY:
    X.append(points[0])
    Y.append(points[1])

plt.scatter(X,Y,c='red')

def area_polygon(point):
   x = []
   y = []
   for p in point:
       x.append(p[0])
       y.append(p[1])

       ar = 0
   for index in range(len(point)-1):
       ar += (x[index]*y[index+1])-(y[index]*x[index+1])
   return abs(ar/2)

square_xy = [(2,2),(9,2),(9,9),(2,9),(2,2)]
polygon_xy = [(3,3),(3,5),(6,8),(8,8),(6,6),(7,3),(3,3)]

area_of_square = area_polygon(square_xy)
area_of_polygon = area_polygon(polygon_xy)

def area_of_irregular_shape():
   count_inside_point = 0
   count_outside_point = 0
   for points in randomXY:
       if(point_inside_outside(polygon_xy,points)):
           count_inside_point += 1
       else:
           count_outside_point += 1
   return (count_inside_point/len(randomXY))*area_of_square

area_of_irregular_shape_approx = area_of_irregular_shape()

SX = [2,9,9,2,2]
SY = [2,2,9,9,2]
Y = []
XY = [(3,3),(3,5),(6,8),(8,8),(6,6),(7,3),(3,3)]
X= []
for point in XY:
        X.append(point[0])
        Y.append(point[1])

plt.plot(SX,SY, c='green')
plt.plot(X,Y,)
plt.title('Approx Area= %d' %(area_of_irregular_shape_approx))

plt.scatter(X,Y)
plt.xlabel('X axis')
plt.ylabel('Y axis')

plt.show()
