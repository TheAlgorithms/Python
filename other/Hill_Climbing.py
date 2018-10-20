#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: nairit-11
"""

import random
import time

class hillClimb(object):
    
    def getDistance(self,P1,P2): #Distance between 2 points
        self.P1 = P1
        self.P2 = P2
        distance = ((self.P1[0]-self.P2[0])**2 + (self.P1[1]-self.P2[1])**2)**(1/2)
        return distance

    def generateCoordinates(self): #Generate random coordinates
        x = random.randint(0,101)
        y = random.randint(0,101)
        return [x,y]

    
    def solver(self):
        
        number = input("How many cities do you want to generate: ")
        self.coord ={}
        cityList = []
        self.number = int(number)
        for i in range(self.number):
            a = str(i)
            l = self.generateCoordinates()
            self.coord[a] = l
            cityList.append(a)
        cityList.append('0')
        currentState = cityList[:]

        totalDist = 0
        for i in range(self.number):
            xi = currentState[i]
            yj = currentState[i+1]
            dist = self.getDistance(self.coord[xi],self.coord[yj])
            totalDist += dist
        
        currentDist = totalDist
        initialDist = totalDist
        
        counter = 0
        while (counter<1000): #Increasing this counter makes the result better
            
            changeIndexOne = random.randint(1,self.number-1)
            changeIndexTwo = random.randint(1,self.number-1)
            
            transState = currentState[:] 
            dummy1 = transState[changeIndexOne]
            dummy2 = transState[changeIndexTwo]

            transState[changeIndexOne] = dummy2
            transState[changeIndexTwo] = dummy1
            
            totalDist = 0
            dist = 0
            for i in range(self.number):
                xi = transState[i]
                yj = transState[i+1]
                dist = self.getDistance(self.coord[xi],self.coord[yj])
                totalDist+=dist 
            
            if totalDist < currentDist:
                currentState = transState[:]
                currentDist = totalDist
            counter+=1
            
        print("Initial state looked like this: ",cityList,"\n")
        print("Point coordinates were: ",self.coord,"\n")
        print("Initial distance was: %.2f km \n" %initialDist)
        print("Final state looks like: ",currentState,"\n")
        print("Optimized distance is: %.2f km" %currentDist)

def main():
    start = time.time()
    hC = hillClimb() 
    hC.solver()
    end = time.time()
    print("Time measure: %.2f sec" % (end-start))

if __name__ == "__main__":
    main() 
