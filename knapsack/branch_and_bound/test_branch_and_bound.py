import sys

from branch_and_bound import BranchAndBound
from item import *


class TestBranchAndBound:
    def main():
        item_list = []
        item = [
            Item("Ant Repellent", 1.0, 2.0),
            Item("Blanket", 4.0, 3.0),
            Item("Brownies", 3.0, 10.0),
            Item("Frisbee", 1.0, 6.0),
            Item("Salad", 5.0, 4.0),
            Item("Watermelon", 10.0, 10.0),
        ]
        try:
            file = open("item_list.txt")
        except FileNotFoundError:
            print("Could not open 'item_list.txt'")
            sys.exit()

        with file:
            for line in file:
                content = line.split(",")
                # Add name, weight , rating and quantity into Item object
                item_list.append(Item(content[0], float(content[1]), float(content[2])))
            file.close()

        while True:
            try:
                capacity = int(input("Enter Maximum Knapsack Capacity: ").strip())
                break
            except ValueError:
                print("Please enter valid number.")

        # Branch and Bounce algorithm implementation
        algorithm = BranchAndBound(capacity, item_list)
        upper = algorithm.solve_knapsack()
        # Output
        print("\nKnapsack Items")
        print(
            "----------------------------------------------------------------------------------------------"
        )
        print("Name\t\t\tWeight\t\tRating\t\tRating-Weight ratio\tQuantity")
        for item in item_list:
            ratio = item.rating / item.weight
            print(
                "{0:<20}\t{1:<5}\t\t{2:<5}\t\t\t{3:<8.2f}\t{4}".format(
                    item.name, item.weight, item.rating, ratio, item.quantity
                )
            )
        print(
            "----------------------------------------------------------------------------------------------"
        )
        print("Item Selected: | ", end="")
        total_weight = 0
        for item in item_list:
            if item.quantity == 1:
                total_weight += item.weight
                print(item.name, " | ", end="")

        print("\nTotal Weight: ", total_weight)
        print("Maximum Rating: ", upper)

    if __name__ == "__main__":
        import doctest

        doctest.testmod()
        main()
