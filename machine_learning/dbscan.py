import pandas as pd
import math
import matplotlib.pyplot as plt
from typing import dict, list


class dbScan:
    """
    DBSCAN Algorithm :
    Density-Based Spatial Clustering Of Applications With Noise
    Refer this website for more details : https://en.wikipedia.org/wiki/DBSCAN

    Functions:
    ----------
        __init__()       : Constructor that sets minPts, radius and file
        perform_dbscan() : Invoked by constructor and calculates the core and noise points and returns a dictionary.
        print_dbscan()   : Prints the core and noise points along with stating if the noise are border points or not.
        plot_dbscan()    : Plots the points to show the core and noise point.

    To create a object
    ------------------
    import dbscan
    obj = dbscan.dbscan(minpts, radius, file)
    obj.print_dbscan()
    obj.plot_dbscan()
    """

    def __init__(self, minpts: int, radius: int, file: str) -> None:
        """
        Constructor

        Attributes:
        -----------
            minpts (int) : Minimum number of points needed to be
                           within the radius to considered as core
            radius (int) : The radius from a given core point where
                           other core points can be considered as core
            file (csv)   : CSV file location. Should contain x and y
                           coordinate value for each point.

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
        """
        self.minpts = minpts
        self.radius = radius
        self.file = file
        self.dict1 = self.perform_dbscan()

    def perform_dbscan(self) -> dict[int, list[int]]:
        """
        >>>perform_dbscan()

        Parameters:
        -----------
        None

        Return:
        --------
        Dictionary with points and the list of points
        that lie in its radius
        """
        data = pd.read_csv(self.file)

        minpts = self.minpts
        e = self.radius

        dict1 = {}
        for i in range(len(data)):
            for j in range(len(data)):
                dist = math.sqrt(
                    pow(data["x"][j] - data["x"][i], 2)
                    + pow(data["y"][j] - data["y"][i], 2)
                )
                if dist < e:
                    if i + 1 in dict1:
                        dict1[i + 1].append(j + 1)
                    else:
                        dict1[i + 1] = [
                            j + 1,
                        ]

        return dict1

    def print_dbscan(self) -> None:
        """
        Outputs:
        --------
        Prints each point and if it is a core or a noise (w/ border)
        """
        for i in self.dict1:
            print(i, " ", self.dict1[i], end=" ---> ")
            if len(self.dict1[i]) >= self.minpts:
                print("Core")
            else:
                for j in self.dict1:
                    if (
                        i != j
                        and len(self.dict1[j]) >= self.minpts
                        and i in self.dict1[j]
                    ):
                        print("Noise ---> Border")
                        break
                else:
                    print("Noise")

    def plot_dbscan(self) -> None:
        """
        Output:
        -------
        A matplotlib plot that show points as core and noise along
        with the circle that lie within it.
        """
        data = pd.read_csv(self.file)
        e = self.radius
        for i in self.dict1:
            if len(self.dict1[i]) >= self.minpts:
                plt.scatter(data["x"][i - 1], data["y"][i - 1], color="red")
                circle = plt.Circle(
                    (data["x"][i - 1], data["y"][i - 1]), e, color="blue", fill=False
                )
                plt.gca().add_artist(circle)
                plt.text(
                    data["x"][i - 1],
                    data["y"][i - 1],
                    "P" + str(i),
                    ha="center",
                    va="bottom",
                )
            else:
                plt.scatter(data["x"][i - 1], data["y"][i - 1], color="green")
                plt.text(
                    data["x"][i - 1],
                    data["y"][i - 1],
                    "P" + str(i),
                    ha="center",
                    va="bottom",
                )
        plt.xlabel("X")
        plt.ylabel("Y")
        plt.title("DBSCAN Clustering")
        plt.legend(["Core", "Noise"])
        plt.show()
