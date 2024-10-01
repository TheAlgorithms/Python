import pandas as pd
import numpy as np
import math
import matplotlib.pyplot as plt

class DBSCAN:
    '''
    Author : Gowtham Kamalasekar
    LinkedIn : https://www.linkedin.com/in/gowtham-kamalasekar/

    DBSCAN Algorithm :
    Density-Based Spatial Clustering Of Applications With Noise
    Refer this website for more details : https://en.wikipedia.org/wiki/DBSCAN

    Attributes:
    -----------
        minPts (int) : Minimum number of points needed to be within the radius to considered as core
        radius (int) : The radius from a given core point where other core points can be considered as core
        file (csv)   : CSV file location. Should contain x and y coordinate value for each point.

        Example :
        minPts = 4
        radius = 1.9
        file = 'data_dbscan.csv'

    File Structure of CSV Data:
    ---------------------------
        _____
        x | y
        -----
        3 | 7
        4 | 6
        5 | 5
        6 | 4
        7 | 3
        -----

    Functions:
    ----------
        __init__()       : Constructor that sets minPts, radius and file
        perform_dbscan() : Invoked by constructor and calculates the core and noise points and returns a dictionary.
        print_dbscan()   : Prints the core and noise points along with stating if the noise are border points or not.
        plot_dbscan()    : Plots the points to show the core and noise point.

    To create a object
    ------------------
    import DBSCAN
    obj = DBSCAN.DBSCAN(minPts, radius, file)
    obj.print_dbscan()
    obj.plot_dbscan()
    '''
    
    def __init__(self, minPts, radius, file):
        self.minPts = minPts
        self.radius = radius
        self.file = file
        self.dict1 = self.perform_dbscan()

    def perform_dbscan(self):
        data = pd.read_csv(self.file)

        minPts = self.minPts
        e = self.radius

        dict1 = {}
        for i in range(len(data)):
            for j in range(len(data)):
                dist = math.sqrt(pow(data['x'][j] - data['x'][i],2) + pow(data['y'][j] - data['y'][i],2))
                if dist < e:
                    if i+1 in dict1:
                        dict1[i+1].append(j+1)
                    else:
                        dict1[i+1] = [j+1,]

        return dict1

    def print_dbscan(self):
        for i in self.dict1:
            print(i," ",self.dict1[i], end=' ---> ')
            if len(self.dict1[i]) >= self.minPts:
                print("Core")
            else:
                for j in self.dict1:
                    if i != j and len(self.dict1[j]) >= self.minPts and i in self.dict1[j]:
                        print("Noise ---> Border")
                        break
                else:
                    print("Noise")

    def plot_dbscan(self):
        data = pd.read_csv(self.file)
        e = self.radius
        for i in self.dict1:
            if len(self.dict1[i]) >= self.minPts:
                plt.scatter(data['x'][i-1], data['y'][i-1], color='red')
                circle = plt.Circle((data['x'][i-1], data['y'][i-1]), e, color='blue', fill=False)
                plt.gca().add_artist(circle)
                plt.text(data['x'][i-1], data['y'][i-1], 'P'+str(i), ha='center', va='bottom')
            else:
                plt.scatter(data['x'][i-1], data['y'][i-1], color='green')
                plt.text(data['x'][i-1], data['y'][i-1], 'P'+str(i), ha='center', va='bottom')

        plt.xlabel('X')
        plt.ylabel('Y')
        plt.title('DBSCAN Clustering')

        plt.legend(['Core','Noise'])
        plt.show()
