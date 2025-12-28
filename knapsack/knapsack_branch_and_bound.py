"""
Branch and Bound solution for the 0/1 Knapsack problem.

This implementation uses a best-first search strategy and prunes
non-promising branches using an upper bound calculated via the
fractional knapsack (greedy) approach.

References:
https://en.wikipedia.org/wiki/Branch_and_bound
https://en.wikipedia.org/wiki/Knapsack_problem
"""

from dataclasses import dataclass
from typing import List
import heapq


@dataclass
class Item:
    weight: int
    value: int


@dataclass
class Node:
    level: int
    profit: int
    weight: int
    bound: float


def calculate_bound(node: Node, capacity: int, items: List[Item]) -> float:
    """
    Calculate the upper bound of profit for a node using
    the fractional knapsack approach.
    """
    if node.weight >= capacity:
        return 0.0

    profit_bound = node.profit
    total_weight = node.weight
    index = node.level + 1

    while index < len(items) and total_weight + items[index].weight <= capacity:
        total_weight += items[index].weight
        profit_bound += items[index].value
        index += 1

    if index < len(items):
        profit_bound += (
            (capacity - total_weight)
            * items[index].value
            / items[index].weight
        )

    return profit_bound


def knapsack_branch_and_bound(
    capacity: int, weights: List[int], values: List[int]
) -> int:
    """
    Solve the 0/1 Knapsack problem using the Branch and Bound technique.

    >>> knapsack_branch_and_bound(50, [10, 20, 30], [60, 100, 120])
    220
    """
    items = [Item(w, v) for w, v in zip(weights, values)]
    items.sort(key=lambda item: item.value / item.weight, reverse=True)

    priority_queue: list[tuple[float, Node]] = []

    root = Node(level=-1, profit=0, weight=0, bound=0.0)
    root.bound = calculate_bound(root, capacity, items)

    heapq.heappush(priority_queue, (-root.bound, root))
    max_profit = 0

    while priority_queue:
        _, current = heapq.heappop(priority_queue)

        if current.bound <= max_profit:
            continue

        next_level = current.level + 1
        if next_level >= len(items):
            continue

        # Include the next item
        include_node = Node(
            level=next_level,
            weight=current.weight + items[next_level].weight,
            profit=current.profit + items[next_level].value,
            bound=0.0,
        )

        if include_node.weight <= capacity:
            max_profit = max(max_profit, include_node.profit)

        include_node.bound = calculate_bound(include_node, capacity, items)
        if include_node.bound > max_profit:
            heapq.heappush(priority_queue, (-include_node.bound, include_node))

        # Exclude the next item
        exclude_node = Node(
            level=next_level,
            weight=current.weight,
            profit=current.profit,
            bound=0.0,
        )

        exclude_node.bound = calculate_bound(exclude_node, capacity, items)
        if exclude_node.bound > max_profit:
            heapq.heappush(priority_queue, (-exclude_node.bound, exclude_node))

    return max_profit


if __name__ == "__main__":
    # Example usage
    capacity_example = 50
    weights_example = [10, 20, 30]
    values_example = [60, 100, 120]

    print(
        knapsack_branch_and_bound(
            capacity_example, weights_example, values_example
        )
    )
