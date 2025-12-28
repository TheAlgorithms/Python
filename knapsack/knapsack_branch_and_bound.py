"""
Branch and Bound solution for the 0/1 Knapsack problem.

This implementation uses a best-first search strategy and prunes
non-promising branches using an upper bound calculated via the
fractional knapsack (greedy) approach.

References:
https://en.wikipedia.org/wiki/Branch_and_bound
https://en.wikipedia.org/wiki/Knapsack_problem
"""

import heapq
from dataclasses import dataclass


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


def calculate_bound(node: Node, capacity: int, items: list[Item]) -> float:
    """
    Calculate the upper bound of profit for a node using
    the fractional knapsack approach.
    """
    if node.weight >= capacity:
        return 0.0

    profit_bound = float(node.profit)
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
    capacity: int, weights: list[int], values: list[int]
) -> int:
    """
    Solve the 0/1 Knapsack problem using the Branch and Bound technique.

    >>> knapsack_branch_and_bound(50, [10, 20, 30], [60, 100, 120])
    220
    """
    items = [Item(weight=w, value=v) for w, v in zip(weights, values)]
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

        # Include next item
        include_node = Node(
            level=next_level,
            profit=current.profit + items[next_level].value,
            weight=current.weight + items[next_level].weight,
            bound=0.0,
        )

        if include_node.weight <= capacity:
            max_profit = max(max_profit, include_node.profit)

        include_node.bound = calculate_bound(include_node, capacity, items)
        if include_node.bound > max_profit:
            heapq.heappush(
                priority_queue, (-include_node.bound, include_node)
            )

        # Exclude next item
        exclude_node = Node(
            level=next_level,
            profit=current.profit,
            weight=current.weight,
            bound=0.0,
        )

        exclude_node.bound = calculate_bound(exclude_node, capacity, items)
        if exclude_node.bound > max_profit:
            heapq.heappush(
                priority_queue, (-exclude_node.bound, exclude_node)
            )

    return max_profit
