"""

Author : Gowtham Kamalasekar
LinkedIn : https://www.linkedin.com/in/gowtham-kamalasekar/

"""

import math

import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
import pandas as pd


class DbScan:
    """
    DBSCAN Algorithm :
    Density-Based Spatial Clustering Of Applications With Noise
    Refer this website for more details : https://en.wikipedia.org/wiki/DBSCAN

    Functions:
    ----------
        __init__()       : Constructor that sets minPts, radius and file
        perform_dbscan() : Invoked by constructor and calculates the core
                            and noise points and returns a dictionary.
        print_dbscan()   : Prints the core and noise points along
                           with stating if the noise are border points or not.
        plot_dbscan()    : Plots the points to show the core and noise point.

    To create a object
    ------------------
    import dbscan
    obj = dbscan.DbScan(minpts, radius, file)
    obj.print_dbscan()
    obj.plot_dbscan()
    """

    def __init__(
        self,
        minpts: int,
        radius: int,
        file: str = "None",
    ) -> None:
        """
        Constructor

        Args:
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
        self.file = (
            file
            if file != "None"
            else (
                {"x": 3, "y": 7},
                {"x": 4, "y": 6},
                {"x": 5, "y": 5},
                {"x": 6, "y": 4},
                {"x": 7, "y": 3},
                {"x": 6, "y": 2},
                {"x": 7, "y": 2},
                {"x": 8, "y": 4},
                {"x": 3, "y": 3},
                {"x": 2, "y": 6},
                {"x": 3, "y": 5},
                {"x": 2, "y": 4},
            )
        )
        self.dict1 = self.perform_dbscan()

    def perform_dbscan(self) -> dict[int, list[int]]:
        """
        Args:
        -----------
            None

        Return:
        --------
            Dictionary with points and the list
            of points that lie in its radius

        >>> result = DbScan(4, 1.9).perform_dbscan()
        >>> for key in sorted(result):
        ...     print(key, sorted(result[key]))
        1 [1, 2, 10]
        2 [1, 2, 3, 11]
        3 [2, 3, 4]
        4 [3, 4, 5]
        5 [4, 5, 6, 7, 8]
        6 [5, 6, 7]
        7 [5, 6, 7]
        8 [5, 8]
        9 [9, 12]
        10 [1, 10, 11]
        11 [2, 10, 11, 12]
        12 [9, 11, 12]

        >>> result = DbScan(3, 2.5).perform_dbscan()
        >>> for key in sorted(result):
        ...     print(key, sorted(result[key]))
        1 [1, 2, 10, 11]
        2 [1, 2, 3, 10, 11]
        3 [2, 3, 4, 11]
        4 [3, 4, 5, 6, 7, 8]
        5 [4, 5, 6, 7, 8]
        6 [4, 5, 6, 7]
        7 [4, 5, 6, 7, 8]
        8 [4, 5, 7, 8]
        9 [9, 11, 12]
        10 [1, 2, 10, 11, 12]
        11 [1, 2, 3, 9, 10, 11, 12]
        12 [9, 10, 11, 12]

        >>> result = DbScan(5, 2.5).perform_dbscan()
        >>> for key in sorted(result):
        ...     print(key, sorted(result[key]))
        1 [1, 2, 10, 11]
        2 [1, 2, 3, 10, 11]
        3 [2, 3, 4, 11]
        4 [3, 4, 5, 6, 7, 8]
        5 [4, 5, 6, 7, 8]
        6 [4, 5, 6, 7]
        7 [4, 5, 6, 7, 8]
        8 [4, 5, 7, 8]
        9 [9, 11, 12]
        10 [1, 2, 10, 11, 12]
        11 [1, 2, 3, 9, 10, 11, 12]
        12 [9, 10, 11, 12]

        """
        if type(self.file) is str:
            data = pd.read_csv(self.file)
        else:
            data = pd.DataFrame(list(self.file))
        e = self.radius
        dict1: dict[int, list[int]] = {}
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

        >>> DbScan(4,1.9).print_dbscan()
        1   [1, 2, 10] ---> Noise ---> Border
        2   [1, 2, 3, 11] ---> Core
        3   [2, 3, 4] ---> Noise ---> Border
        4   [3, 4, 5] ---> Noise ---> Border
        5   [4, 5, 6, 7, 8] ---> Core
        6   [5, 6, 7] ---> Noise ---> Border
        7   [5, 6, 7] ---> Noise ---> Border
        8   [5, 8] ---> Noise ---> Border
        9   [9, 12] ---> Noise
        10   [1, 10, 11] ---> Noise ---> Border
        11   [2, 10, 11, 12] ---> Core
        12   [9, 11, 12] ---> Noise ---> Border

        >>> DbScan(5,2.5).print_dbscan()
        1   [1, 2, 10, 11] ---> Noise ---> Border
        2   [1, 2, 3, 10, 11] ---> Core
        3   [2, 3, 4, 11] ---> Noise ---> Border
        4   [3, 4, 5, 6, 7, 8] ---> Core
        5   [4, 5, 6, 7, 8] ---> Core
        6   [4, 5, 6, 7] ---> Noise ---> Border
        7   [4, 5, 6, 7, 8] ---> Core
        8   [4, 5, 7, 8] ---> Noise ---> Border
        9   [9, 11, 12] ---> Noise ---> Border
        10   [1, 2, 10, 11, 12] ---> Core
        11   [1, 2, 3, 9, 10, 11, 12] ---> Core
        12   [9, 10, 11, 12] ---> Noise ---> Border

        >>> DbScan(2,0.5).print_dbscan()
        1   [1] ---> Noise
        2   [2] ---> Noise
        3   [3] ---> Noise
        4   [4] ---> Noise
        5   [5] ---> Noise
        6   [6] ---> Noise
        7   [7] ---> Noise
        8   [8] ---> Noise
        9   [9] ---> Noise
        10   [10] ---> Noise
        11   [11] ---> Noise
        12   [12] ---> Noise

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

        >>> DbScan(4,1.9).plot_dbscan()
        Plotted Successfully

        >>> DbScan(5,2.5).plot_dbscan()
        Plotted Successfully

        >>> DbScan(5,2.5).plot_dbscan()
        Plotted Successfully

        """
        if type(self.file) is str:
            data = pd.read_csv(self.file)
        else:
            data = pd.DataFrame(list(self.file))
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
        core_legend = mpatches.Patch(color="red", label="Core")
        noise_legend = mpatches.Patch(color="green", label="Noise")
        plt.xlabel("X")
        plt.ylabel("Y")
        plt.title("DBSCAN Clustering")
        plt.legend(handles=[core_legend, noise_legend])
        plt.show()
        print("Plotted Successfully")


if __name__ == "__main__":
    import doctest

    doctest.testmod()
