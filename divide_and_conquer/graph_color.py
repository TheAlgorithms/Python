from __future__ import annotations

from collections import defaultdict

students = {
    "Math": ["Alice", "Bob", "Charlie"],
    "Physics": ["Alice", "Charlie", "David"],
    "Chemistry": ["Bob", "Charlie", "Eve"],
    "Biology": ["Alice", "David", "Eve"],
}


class Graph:
    """
    A graph data structure, undirected by default.
    """

    def __init__(self, subjects: list[str]) -> None:
        """
        Initialize a Graph instance with a list of subjects.

        :param subjects: A list of subjects to be represented in the graph.

        >>> graph = Graph(list(students))
        >>> graph.subjects  # doctest: +ELLIPSIS
        ['Math', 'Physics', 'Chemistry', 'Biology']
        >>> graph.graph
        defaultdict(<class 'list'>, {})
        """
        self.subjects = subjects
        self.graph: defaultdict[str, list[str]] = defaultdict(list)

    def add_edge(self, subject1: str, subject2: str) -> None:
        """
        Add an edge between two subjects in the graph.

        :param subject1: The first subject to connect.
        :param subject2: The second subject to connect.

        >>> graph = Graph(list(students))
        >>> dict(graph.graph)
        {}
        >>> graph.add_edge("Math", "Physics")
        >>> dict(graph.graph)
        {'Math': ['Physics'], 'Physics': ['Math']}
        """
        self.graph[subject1].append(subject2)
        self.graph[subject2].append(subject1)

    def graph_coloring(self) -> dict[str, int]:
        """
        Color the graph using the minimum number of colors.
        >>> Graph(list(students)).graph_coloring()
        {'Math': 1, 'Physics': 1, 'Chemistry': 1, 'Biology': 1}
        >>> graph = Graph(list(students))
        >>> graph.add_edge("Math", "Physics")
        >>> graph.graph_coloring()
        {'Math': 1, 'Physics': 2, 'Chemistry': 1, 'Biology': 1}
        >>> graph.add_edge("Physics", "Chemistry")
        >>> graph.graph_coloring()  # Is this correct?!?
        {'Math': 1, 'Physics': 2, 'Chemistry': 1, 'Biology': 1}
        """
        color_map: dict[str, int] = {}
        available_colors = set(range(1, len(self.subjects) + 1))
        for subject in self.subjects:
            used_colors = set()

            for neighbor in self.graph[subject]:
                if neighbor in color_map:
                    used_colors.add(color_map[neighbor])

            available_color = available_colors - used_colors
            if available_color:
                color_map[subject] = min(available_color)
            else:
                # If no available color, assign a new color
                color_map[subject] = len(available_colors) + 1
                available_colors.add(color_map[subject])
        return color_map

    def get_minimum_time_slots(self) -> int:
        """
        Get the minimum number of time slots needed to schedule all subjects.
        >>> Graph(list(students)).get_minimum_time_slots()
        1
        >>> graph = Graph(list(students))
        >>> graph.add_edge("Math", "Physics")
        >>> graph.get_minimum_time_slots()
        2
        >>> graph.add_edge("Physics", "Chemistry")
        >>> graph.get_minimum_time_slots()  # Is this correct?!?
        2
        """
        return max(self.graph_coloring().values())


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    graph = Graph(list(students))
    graph.add_edge("Math", "Physics")
    graph.add_edge("Math", "Chemistry")
    graph.add_edge("Physics", "Chemistry")
    graph.add_edge("Physics", "Biology")
    print(f"{graph.subjects = }")
    print(f"{dict(graph.graph) = }")
    print(f"{graph.graph_coloring() = }")
    print(f"{graph.get_minimum_time_slots() = }")
