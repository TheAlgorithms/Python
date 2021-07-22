from item import *
import sys
import heapq as hq


class BranchAndBound:

    def __init__(self, numItem, capacity):
        self.numItem = numItem
        # capacity is the knapsack maximum capacity
        self.capacity = capacity
        # root is the root of the node
        self.root = self.TreeNode()
        # upper is the upper bound or maximum rating in the subtree of this node
        self.upper = sys.maxsize

    def CalcUpperBound(self, totalWeight, totalRating, item, level):
        # weight is the weight of the item
        weight = totalWeight
        # rating is also known as profit
        rating = totalRating

        i = level
        while i < self.numItem:
            if (float(item[i].weight) + float(weight)) <= float(self.capacity):
                # Since this algorithm is to solve minimization problem
                # I am converting maximization problem to minimization problem
                # Thus, the rating and upperBound will be negative
                # Instead of sum up the rating, I deduct the rating

                rating -= float(item[i].rating)
                weight += float(item[i].weight)
            # Since this is 0/1 knapsack problem, the fractional part will not be taken
            i += 1
        return rating

    def CalcCost(self, totalWeight, totalRating, item, level):

        weight = totalWeight
        rating = totalRating

        i = level
        while i < self.numItem:
            if (float(item[i].weight) + float(weight)) <= float(self.capacity):
                rating -= float(item[i].rating)
                weight += float(item[i].weight)
            else:
                # For the Cost, the rating will take the fractional part of the items
                # so that the capacity is fully utilized
                rating -= float(item[i].weight) / \
                    float(item[i].rating) * (float(self.capacity) - weight)
                break
            i += 1
        return rating

    def SolveKnapsack(self, item):
        # Sort the items based on the ratio of rating over weight
        def ComputeRatio(item):
            return float(item.rating) / float(item.weight)
        item.sort(key=ComputeRatio, reverse=True)

        current = self.root  # Start from root
        # Create priority queue with sorted cost
        prioQueue = []
        hq.heapify(prioQueue)
        hq.heappush(prioQueue, current)

        while prioQueue:
            current = hq.heappop(prioQueue)
            current.left = self.TreeNode()
            current.right = self.TreeNode()

            # Since upper store the optimal rating,
            # if the cost of current node is higher than overall upper bound,
            # there is no use to explore the node because the node will
            # not give optimal rating.
            # Remember that the rating is stored as negative rating.
            # The smaller the upper bound, the more optimized rating can be obtained.

            if current.cost > self.upper or current.level == self.numItem:
                continue

            # Left Child TreeNode

            # Check the total weight after the left child node includes the next item
            # If the total weight < capacity, upper bound and cost will be calculated

            totalWeight = current.cumWeight + \
                float(item[current.level].weight)
            totalRating = current.cumRating - \
                float(item[current.level].rating)
            # If the next item can be added
            if totalWeight <= float(self.capacity):
                current.left.level = current.level + 1
                item[current.left.level - 1].quantity += 1
                current.left.cumWeight = totalWeight
                current.left.cumRating = totalRating
                current.left.upperBound = self.CalcUpperBound(
                    totalWeight, totalRating, item, current.left.level)
                current.left.cost = self.CalcCost(
                    totalWeight, totalRating, item, current.left.level)
            # If the next item cannot be added
            else:
                # Make the upperBound and cost become maximum positive number,
                # so that this node will not be added to the priority queue
                # because it is always larger than upper

                current.left.upperBound = sys.maxsize
                current.left.cost = sys.maxsize

            # Right Child TreeNode

            # Set right child node to not include the next item
            current.right.level = current.level + 1
            current.right.cumWeight = current.cumWeight
            current.right.cumRating = current.cumRating
            current.right.upperBound = self.CalcUpperBound(
                current.cumWeight, current.cumRating, item, current.right.level)
            current.right.cost = self.CalcCost(
                current.cumWeight, current.cumRating, item, current.right.level)

            if current.left.upperBound < self.upper:
                self.upper = current.left.upperBound
            if current.right.upperBound < self.upper:
                self.upper = current.right.upperBound

            # if left child node may result in more optimized rating
            if self.upper >= current.left.cost:
                # Add left child node to priority queue
                hq.heappush(prioQueue, current.left)
            # if right child node may result in more optimized rating
            if self.upper >= current.right.cost:
                # Add right child node to priority queue
                hq.heappush(prioQueue, current.right)

        return -self.upper

    # TreeNode class is used to store the information
    class TreeNode:
        # cumWeight is the cumulative weight of all items which is selected from root to this node
        # cumRating is the cumulative rating of all items which is selected from root to this node
        # upperBound is the possible optimized rating for the node path
        # level us the level of node in the decision tree
        def __init__(self):
            self.level = 0
            self.cumWeight = 0
            self.cumRating = 0
            self.upperBound = 0
            self.cost = 0

        # Comparator to compare nodes' cost for sorting purpose
        def __lt__(self, other):
            return self.cost < other.cost
