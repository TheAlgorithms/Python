"""
This function builds a Directed Acyclic Graph representation of the Knapsack problem.
This allows us to solve knapsack-style problems with Shortest Path algorithms.
See https://github.com/Matti02co/graph-based-scheduling for more details.

The graph consists of n+2 layers:
- Layer 0 contains the source node 's'.
- Layer n+1 contains the sink node 't'.
- Intermediate layers (1..n) correspond to the n items.

Each intermediate layer j has (capacity + 1) nodes: j0, j1, ..., jC,
where jk represents the state of having considered the first j items
with a total weight of k so far.

From each node jk there are at most two outgoing edges:
- Skip item j+1 (weight and cost remain the same).
- Take item j+1 (only if total weight + item's weight ≤ capacity), with a cost
  equal to the negative of the item's value (we solve via shortest path).

All nodes in the last layer are connected to 't' with zero-cost edges.

In this representation, every path from 's' to 't' corresponds to a feasible
Knapsack solution, and the shortest path (negative costs) corresponds to
the maximum total value selection.
"""

from typing import Any


def generate_knapsack_graph(
    capacity: int, weights: list[int], values: list[int]
) -> list[dict[str, Any]]:
    """
    Generate a Directed Acyclic Graph (DAG) representation of the 0/1 Knapsack problem.

    Parameters
    ----------
    capacity : int
        Maximum weight capacity of the knapsack.
    weights : list[int]
        List of item weights.
    values : list[int]
        List of item values.

    Returns
    -------
    list[dict]
        List of edges, each represented as a dictionary with:
        - 'from': start node
        - 'to': end node
        - 'cost': edge cost (negative item value when item is included)
        - 'label': description of the decision

    Test
    --------
    >>> edges = generate_knapsack_graph(5, [2, 3], [10, 20])
    >>> len(edges) > 0
    True
    >>> any(edge['label'].startswith("take_item") for edge in edges)
    True
    >>> any(edge['label'].startswith("skip_item") for edge in edges)
    True
    >>> edges[-1]['to'] == 't'
    True
    >>> # Check a specific edge: first item, weight 2, value 10
    >>> first_take_edge = next(edge for edge in edges if edge['label'] == "take_item_0")
    >>> first_take_edge['from'] == (0, 0)
    True
    >>> first_take_edge['to'] == (1, 2)
    True
    >>> first_take_edge['cost'] == -10
    True
    """

    n = len(weights)
    edges = []

    # Generate a layer for each item, with (capacity + 1) nodes
    for i in range(n):
        for w in range(capacity + 1):
            weight = weights[i]
            value = values[i]

            # Edge for skipping the current item
            edges.append(
                {
                    "from": (i, w),
                    "to": (i + 1, w),
                    "cost": 0,  # no value added
                    "label": f"skip_item_{i}",
                }
            )

            # Edge for taking the item, only if within capacity
            if w + weight <= capacity:
                edges.append(
                    {
                        "from": (i, w),
                        "to": (i + 1, w + weight),
                        "cost": -value,  # negative cost to solve SPP
                        "label": f"take_item_{i}",
                    }
                )

    # Source node and initial edge
    edges.append({"from": "s", "to": (0, 0), "cost": 0, "label": "start"})

    # Edges from all final states to the sink node
    for w in range(capacity + 1):
        edges.append({"from": (n, w), "to": "t", "cost": 0, "label": f"end_{w}"})

    return edges
