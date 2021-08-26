import heapq as hq
import sys

from item import *

"""
We are planning for a picnic.
There are some items we would like to carry.
Our knapsack is only able to carry 15 pounds of items.
The items are given with some ratings from 1 to 10 to indicates how strongly we want to include the particular item in knapsack for the picnic.
Once the item is included in the knapsack, the same item cannot be carried again.

There are total of 6 items as follows:
1. Ant Repellent,1,2
2. Blanket,4,3
3. Brownies,3,10
4. Frisbee,1,6
5. Salad,5,4
6. Watermelon,10,10

Calculate the maximum rating and total weight that the knapsack can take.
"""


class BranchAndBound:
    """
    >>> item_list = [Item('Ant Repellent',1.0,2.0), Item('Blanket',4.0,3.0), Item('Brownies',3.0,10.0), Item('Frisbee',1.0,6.0), Item('Salad',5.0,4.0), Item('Watermelon',10.0,10.0)]

    Valid Test 1
    ----------
    >>> capacity = 15
    >>> algorithm = BranchAndBound(capacity, item_list)
    >>> algorithm.calc_upper_bound(15,-28.0,1)
    -28.0
    >>> algorithm.calc_cost(15,-28.0,6)
    -28.0
    >>> algorithm.solve_knapsack()
    28.0
    >>> total_weight = 0
    >>> for item in item_list:
    ...      if item.quantity == 1:
    ...          total_weight += item.weight
    >>> total_weight
    15.0

    The result is 28.0 rating with total weight of 15.0 for capacity 15.0
    ---------------------------------------------------------------------

    Valid Test 2
    ----------
    >>> capacity = 20
    >>> algorithm = BranchAndBound(capacity, item_list)
    >>> algorithm.calc_upper_bound(15,-28.0,1)
    -40.0
    >>> algorithm.calc_cost(15,-28.0,6)
    -28.0
    >>> algorithm.solve_knapsack()
    32.0
    >>> for item in item_list:
    ...      if item.quantity == 1:
    ...          total_weight += item.weight
    >>> total_weight
    20.0

    The result is 32.0 rating with total weight of 20.0 for capacity 20.0
    ---------------------------------------------------------------------

    Invalid Test
    ------------
    >>> capacity = -1
    >>> algorithm = BranchAndBound(capacity, item_list)
    Traceback (most recent call last):
        ...
    ValueError: Invalid data. Please enter positive value.
    """

    def __init__(self, capacity: float, item_list: list[Item]) -> None:
        # validation for capacity
        if capacity < 0:
            raise ValueError("Invalid data. Please enter positive value.")

        self.num_item = len(item_list)
        # capacity is the knapsack maximum capacity
        self.capacity = capacity
        # root is the root of the node
        self.root = TreeNode()
        # upper is the upper bound or maximum rating in the subtree of this node
        self.upper = sys.maxsize
        # List of items
        self.item_list = item_list

    def calc_upper_bound(
        self, total_weight: float, total_rating: float, level: int
    ) -> float:
        """
        Function description is as follows-
        :param total_weight: total_weight of the items
        :param total_rating: total_rating  of the items
        :param item: item list containing number of items
        :param level: the current node level
        """
        # weight is the weight of the item
        weight = total_weight
        # rating is also known as profit
        rating = total_rating

        i = level
        while i < self.num_item:
            if self.item_list[i].weight + weight <= self.capacity:
                # Since this algorithm is to solve minimization problem
                # I am converting maximization problem to minimization problem
                # Thus, the rating and upper_bound will be negative
                # Instead of sum up the rating, I deduct the rating

                rating -= self.item_list[i].rating
                weight += self.item_list[i].weight
            # Since this is 0/1 knapsack problem, the fractional part will not be taken
            i += 1
        return rating

    def calc_cost(self, total_weight: float, total_rating: float, level: int) -> float:
        """
        Function description is as follows-
        :param total_weight: total_weight of the items
        :param total_rating: total_rating  of the items
        :param item: item list containing number of items
        :param level: the current node level
        """
        weight = total_weight
        rating = total_rating

        i = level
        while i < self.num_item:
            if self.item_list[i].weight + weight <= self.capacity:
                rating -= self.item_list[i].rating
                weight += self.item_list[i].weight
            else:
                # For the Cost, the rating will take the fractional part of the items
                # so that the capacity is fully utilized
                rating -= (
                    self.item_list[i].weight
                    / self.item_list[i].rating
                    * (self.capacity - weight)
                )
                break
            i += 1
        return rating

    def solve_knapsack(self) -> float:
        """
        Return the maximum rating that can be put in a knapsack of a capacity cap,
        whereby each weight has a specific rating
        """
        # Sort the items based on the ratio of rating over weight
        def compute_ratio(item: Item) -> float:
            return float(item.rating) / float(item.weight)

        self.item_list.sort(key=compute_ratio, reverse=True)

        current = self.root  # Start from root
        # Create priority queue with sorted cost
        priority_queue: list[TreeNode] = []
        hq.heapify(priority_queue)
        hq.heappush(priority_queue, current)

        while priority_queue:
            current = hq.heappop(priority_queue)
            current.left = TreeNode()
            current.right = TreeNode()

            # Since upper store the optimal rating,
            # if the cost of current node is higher than overall upper bound,
            # there is no use to explore the node because the node will
            # not give optimal rating.
            # Remember that the rating is stored as negative rating.
            # The smaller the upper bound, the more optimized rating can be obtained.

            if current.cost > self.upper or current.level == self.num_item:
                continue

            # Left Child TreeNode

            # Check the total weight after the left child node includes the next item
            # If the total weight < capacity, upper bound and cost will be calculated

            total_weight = current.cum_weight + \
                self.item_list[current.level].weight
            total_rating = current.cum_rating - \
                self.item_list[current.level].rating
            # If the next item can be added
            if total_weight <= self.capacity:
                current.left.level = current.level + 1
                self.item_list[current.left.level - 1].quantity += 1
                current.left.cum_weight = total_weight
                current.left.cum_rating = total_rating
                current.left.upper_bound = self.calc_upper_bound(
                    total_weight, total_rating, current.left.level
                )
                current.left.cost = self.calc_cost(
                    total_weight, total_rating, current.left.level
                )
            # If the next item cannot be added
            else:
                # Make the upper_bound and cost become maximum positive number,
                # so that this node will not be added to the priority queue
                # because it is always larger than upper

                current.left.upper_bound = sys.maxsize
                current.left.cost = sys.maxsize

            # Right Child TreeNode

            # Set right child node to not include the next item
            current.right.level = current.level + 1
            current.right.cum_weight = current.cum_weight
            current.right.cum_rating = current.cum_rating
            current.right.upper_bound = self.calc_upper_bound(
                current.cum_weight, current.cum_rating, current.right.level
            )
            current.right.cost = self.calc_cost(
                current.cum_weight, current.cum_rating, current.right.level
            )

            if current.left.upper_bound < self.upper:
                self.upper = current.left.upper_bound
            if current.right.upper_bound < self.upper:
                self.upper = current.right.upper_bound

            # if left child node may result in more optimized rating
            if self.upper >= current.left.cost:
                # Add left child node to priority queue
                hq.heappush(priority_queue, current.left)
            # if right child node may result in more optimized rating
            if self.upper >= current.right.cost:
                # Add right child node to priority queue
                hq.heappush(priority_queue, current.right)

        return -self.upper


# TreeNode class is used to store the information


class TreeNode:
    # cum_weight is the cumulative weight of all items which is selected from root to this node
    # cum_rating is the cumulative rating of all items which is selected from root to this node
    # upper_bound is the possible optimized rating for the node path
    # level us the level of node in the decision tree

    def __init__(self) -> None:
        self.level = 0
        self.cum_weight = 0.0
        self.cum_rating = 0.0
        self.upper_bound = 0.0
        self.cost = 0.0
        self.left = None
        self.right = None

    # Comparator to compare nodes' cost for sorting purpose
    def __lt__(self, other: "TreeNode") -> bool:
        return self.cost < other.cost


if __name__ == "__main__":
    import doctest

    doctest.testmod()
