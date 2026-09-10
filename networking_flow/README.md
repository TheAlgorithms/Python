# Networking Flow

This directory collects algorithms for the **maximum-flow problem**: given a
directed graph whose edges have capacities, a `source`, and a `sink`, how
much flow can be pushed from `source` to `sink` without exceeding any edge's
capacity?

Maximum flow turns up all over the place — routing traffic through a network,
matching people to jobs, scheduling, image segmentation, and any problem that can
be phrased as "move as much as possible from here to there through a shared
network." Its close relative, the **minimum cut**, finds the cheapest set of
edges whose removal disconnects the sink from the source, and the
[max-flow min-cut theorem](https://en.wikipedia.org/wiki/Max-flow_min-cut_theorem)
says the two always have the same value.

New to the topic? These are good starting points:

* <https://en.wikipedia.org/wiki/Maximum_flow_problem>
* <https://en.wikipedia.org/wiki/Flow_network>
* <https://en.wikipedia.org/wiki/Max-flow_min-cut_theorem>

## What's in this directory

| File | Description |
| ---- | ----------- |
| [`ford_fulkerson.py`](ford_fulkerson.py) | The [Ford-Fulkerson](https://en.wikipedia.org/wiki/Ford%E2%80%93Fulkerson_algorithm) method, finding augmenting paths with a breadth-first search (the [Edmonds-Karp](https://en.wikipedia.org/wiki/Edmonds%E2%80%93Karp_algorithm) refinement). Uses an adjacency-matrix representation. Runs in `O(V * E^2)`. |
| [`minimum_cut.py`](minimum_cut.py) | Finds the edges of a [minimum s-t cut](https://en.wikipedia.org/wiki/Minimum_cut) from the residual graph left behind by Ford-Fulkerson, illustrating the max-flow min-cut theorem. |
| [`dinic.py`](dinic.py) | [Dinic's algorithm](https://en.wikipedia.org/wiki/Dinic%27s_algorithm): repeatedly build a BFS *level graph* and saturate a *blocking flow* on it. Adjacency-list based, so it handles parallel edges and sparse graphs well. Runs in `O(V^2 * E)`, or `O(E * sqrt(V))` on unit-capacity networks. |
| [`push_relabel.py`](push_relabel.py) | The [push-relabel](https://en.wikipedia.org/wiki/Push%E2%80%93relabel_maximum_flow_algorithm) (Goldberg-Tarjan) method: instead of augmenting whole paths, it maintains a *preflow* and locally pushes excess towards the sink. With highest-label selection it runs in `O(V^2 * sqrt(E))`, and is a strong choice on dense graphs. |

## Which one should I use?

All four compute the same maximum-flow value; they differ in speed and in how
the graph is represented.

* **Just learning the idea?** Start with `ford_fulkerson.py` and
  `minimum_cut.py` — the augmenting-path picture is the most intuitive.
* **Sparse graph, or parallel edges?** Reach for `dinic.py`; the adjacency-list
  representation and level-graph batching make it fast in practice.
* **Dense graph?** `push_relabel.py` tends to win, because it avoids
  re-scanning long augmenting paths.

Each file is self-contained, fully type-hinted, and verified with doctests — run
any of them directly (for example `python networking_flow/dinic.py`) to execute
the tests.
