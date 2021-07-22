from branch_and_bound import BranchAndBound
from item import *
import sys


class TestBranchAndBound():
    def main():
        itemList = []

        try:
            file = open("item_list.txt")
        except FileNotFoundError:
            print("Could not open 'item_list.txt'")
            sys.exit()

        with file:
            for line in file:
                content = line.split(",")
                # Add name, weight , rating and quantity into Item object
                itemList.append(Item(content[0], content[1], content[2]))
            file.close()

        while True:
            try:
                capacity = int(
                    input("Enter Maximum Knapsack Capacity: ").strip())
                if capacity < 0:
                    raise ValueError
                break
            except ValueError:
                print("Please enter valid number.")

        # Branch and Bounce algorithm implementation
        algorithm = BranchAndBound(len(itemList), capacity)
        upper = algorithm.SolveKnapsack(itemList)

        # Output
        print("\nKnapsack Items")
        print("----------------------------------------------------------------------------------------------")
        print("Name\t\t\tWeight\t\tRating\t\tRating-Weight ratio\tQuantity")
        for item in itemList:
            ratio = float(item.rating) / float(item.weight)
            print("{0:<20}\t{1:<5}\t\t{2:<5}\t\t\t{3:<8.2f}\t{4}".format(
                item.name, float(item.weight), int(item.rating), float(ratio), int(item.quantity)))
        print("----------------------------------------------------------------------------------------------")
        print("Item Selected: | ", end="")
        totalWeight = 0
        for item in itemList:
            if item.quantity == 1:
                totalWeight += float(item.weight)
                print(item.name, " | ", end="")

        print("\nTotal Weight: ", totalWeight)
        print("Maximum Rating: ", upper)

    if __name__ == "__main__":
        main()
