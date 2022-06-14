#!/usr/bin/env python
import rospy # Python library for ROS
import math # Pyton library for mathematical functions 
from sensor_msgs.msg import LaserScan #import library for lidar sensor
from geometry_msgs.msg import Twist #import geometry form twist

class laser_scan_data(): #main class
    def __init__(self): #main function
        global move
        move = Twist() #create object of twist type  
        self.pub = rospy.Publisher("/cmd_vel", Twist, queue_size=10) #publish message
        self.sub = rospy.Subscriber("/scan", LaserScan, self.callback) #subscribe message 
        self.count = 0
        self.max = 0
        self.min = 0.5
        self.amax = 0
        self.amin = 270
        self.ld = 0
        self.rd = 0
        self.AX = 0
        self.AY = 0
        self.center = 0
        self.BX = 0
        self.BY = 0
        self.CX = 0
        self.CY = 0
        #self.arr
        self.circle = 0
        self.ds = 0
        self.xr = 0
        self.yr = 0
        self.xl = 0
        self.yl = 0
        self.op = 0
        self.do = 0
    def callback(self, msg): #function for calculating various angles and distance related to object
        print('-------RECEIVING LIDAR SENSOR DATA-------')
        self.count = 0 #count of data points on the object
        self.max = 0 # max distance point on object
        self.min = 0.5 # min distance point on object
        self.amin = 270 # angle at right side of object
        self.amax = 0 # angle at left side of object
        self.ld = 0 # distance of the leftmost point
        self.rd = 0 # distance of rightmost point
        self.center = 0 # distance of the center data point on object
        self.AX = 0
        self.AY = 0
        self.BX = 0
        self.BY = 0
        self.CX = 0
        self.CY = 0
        self.radius = 0
        self.circle = 0
        self.ds = 0
        self.xr = 0
        self.yr = 0
        self.xl = 0
        self.yl = 0
        self.op = 0
        self.do = 0
        #self.arr = [None]*len(msg.ranges)
        for i in range(0,1079): # for loop to read the data of 1080 data points
         
           if (msg.ranges[i] < 10) and (msg.ranges[i] > 0.1): # assigning all the data points beyond the desired range as infinity
            #self.arr[i] = msg.ranges[i]
            self.count = self.count + 1 # extracting data points less than the desired diatance
            print('Angle = ', i*0.25) # calculating angle at each point
            print('Distance = ', msg.ranges[i])
            #print('Count = ', self.count)  
            if(msg.ranges[i] > self.max): # calculating max range
               self.max = msg.ranges[i]
            if(msg.ranges[i] < self.min): # calculating min range
               self.min = msg.ranges[i]
            if(i*0.25 > self.amax): # calculating leftmost angle
               self.amax = i*0.25
               self.ld = msg.ranges[i] # leftmost distance
            if(i*0.25 < self.amin): #calculating rightmost angle
               self.amin = i*0.25 
               self.rd = msg.ranges[i] # rightmost distance
            self.center = ((self.amax/0.25)-((self.amax-self.amin)/0.5)) # calculating center distance  
            self.AX = (self.rd*(math.cos(2.3561-(0.01745*self.amin))))
            self.AY = (self.rd*(math.sin(2.3561-(0.01745*self.amin))))
            self.BX = (self.ld*(math.cos((0.01745*self.amax)-2.3561)))
            self.BY = (self.ld*(math.sin((0.01745*self.amax)-2.3561)))
            self.CX = (self.AX + self.BX)/2.0
            self.CY = (self.AY + self.BY)/2.0
            self.radius = (((((self.BX - self.AX)**2)+((-self.BY - self.AY)**2))**0.5)/2.0) +0.3 
            #self.circle = 2 * math.pi * self.radius
            #print(((msg.ranges[int(self.center)])**2) - ((self.radius)**2))
            self.ds = (abs(((msg.ranges[int(self.center)])**2) - ((self.radius)**2)))**0.5
            self.op = (135 - ((self.center)*0.25))
            self.do = (math.atan(self.radius/self.ds))*56.295
            self.xl = self.ds*(math.cos(0.01745*(self.op + self.do)))
            self.yl = self.ds*(math.sin(0.01745*(self.op + self.do)))
            self.xr = self.ds*(math.cos(0.01745*(self.op - self.do)))
            self.yr = self.ds*(math.sin(0.01745*(self.op - self.do)))
        
            
             
        #print('Min Distance = ', self.min)  # printing required feilds
        #print('Max Distance = ', self.max)
        print('Min Angle = ', self.amin)
        print('Max Angle = ', self.amax)
        print('Right Distance = ', self.rd)
        print('Left Distance = ', self.ld)
        print('Distance at Center = ', msg.ranges[int(self.center)])
        print('Angle at Center = ', self.center*0.25)
        rospy.loginfo('A(X,Y) = (%f,%f)', self.AX, self.AY)
        rospy.loginfo('B(X,Y) = (%f,%f)', self.BX, -self.BY)
        #rospy.loginfo('C(X,Y) = (%f,%f)', self.CX, self.CY)
        rospy.loginfo('Unsafe Radius = %f', self.radius)
        #rospy.loginfo('Unsafe Circle = %f', self.circle)
        #print('X Coordinate of point A = ', self.AX)
        #print('Y Coordinate of point A = ', self.AY)
        #print('X Coordinate of point B = ', self.BX)
        #print('Y Coordinate of point B = ', self.BY)
        print(self.ds)
        print(self.op)
        print(self.do)
        rospy.loginfo('LT(X,Y) = (%f,%f)', self.xl, self.yl)
        rospy.loginfo('RT(X,Y) = (%f,%f)', self.xr, self.yr)
        
        self.pub.publish(move)
 
if __name__ == '__main__':
    rospy.init_node('check_obstacle') #initilize node
    laser_scan_data() #run class
    rospy.spin() #loop it
    
#CODER
# VEDANSH BENIWAL ^_^ 
