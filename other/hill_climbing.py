#!/usr/bin/env python3
"""
@author: nairit-11
"""

import random
import time


class hillClimb(object):
    def getDistance(self, point1, point2):
        """Distance between 2 points"""
        return ((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2) ** (1 / 2)

    def generateCoordinates(self):
        """Generate random coordinates"""
        return [random.randint(0, 101), random.randint(0, 101)]

    def solver(self):
        number = input("How many cities do you want to generate: ").strip()
        self.coord = {}
        cityList = []
        self.number = int(number)
        for i in range(self.number):
            a = str(i)
            self.coord[a] = self.generateCoordinates()
            cityList.append(a)
        cityList.append("0")
        currentState = cityList[:]

        totalDist = 0
        for i in range(self.number):
            xi = currentState[i]
            yj = currentState[i + 1]
            dist = self.getDistance(self.coord[xi], self.coord[yj])
            totalDist += dist

        currentDist = totalDist
        initialDist = totalDist

        counter = 0
        while counter < 1000:  # Increasing this counter makes the result better
            x = random.randint(1, self.number - 1)
            y = random.randint(1, self.number - 1)
            transState = currentState[:]
            transState[x], transState[y] = transState[y], transState[x]

            totalDist = 0
            dist = 0
            for i in range(self.number):
                xi = transState[i]
                yj = transState[i + 1]
                dist = self.getDistance(self.coord[xi], self.coord[yj])
                totalDist += dist

            if totalDist < currentDist:
                currentState = transState[:]
                currentDist = totalDist
            counter += 1

        print(f"Initial state looked like this: {cityList}\n")
        print(f"Point coordinates were: {self.coord}\n")
        print(f"Initial distance was: {initialDist:.2f} km\n")
        print(f"Final state looks like: {currentState}\n")
        print(f"Optimized distance is: {currentDist:%.2f} km")


def main():
    start = time.time()
    hC = hillClimb()
    hC.solver()
    end = time.time()
    print(f"Time measure: {end - start:.2f} sec")


if __name__ == "__main__":
    main()
