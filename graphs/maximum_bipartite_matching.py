class MaximalBipartiteMatching:
    """
    This class implements finding maximal Bipartite matching using DFS.
    Usage:
    >>> bipartite_graph_1 = [
    ...     [0, 1, 1, 0, 0, 0],
    ...     [1, 0, 0, 1, 0, 0],
    ...     [0, 0, 1, 0, 0, 0],
    ...     [0, 0, 1, 1, 0, 0],
    ...     [0, 0, 0, 0, 0, 0],
    ...     [0, 0, 0, 0, 0, 1]
    ... ]
    >>> matching_1 = MaximalBipartiteMatching(bipartite_graph_1)
    >>> matching_1.find_maximal_matching()
    5
    >>> bipartite_graph_2 = [
    ...     [1, 1, 1, 0, 0, 0],
    ...     [1, 0, 0, 0, 0, 0],
    ...     [0, 1, 0, 0, 0, 0],
    ...     [0, 0, 0, 0, 1, 0],
    ...     [0, 0, 0, 1, 1, 0],
    ...     [0, 0, 0, 0, 0, 1]
    ... ]
    >>> matching_2 = MaximalBipartiteMatching(bipartite_graph_2)
    >>> matching_2.find_maximal_matching()
    6
    >>> bipartite_graph_3 = [
    ...     [1, 0, 0, 0],
    ...     [0, 1, 1, 1],
    ...     [1, 0, 0, 0],
    ...     [0, 0, 1, 0],
    ... ]
    >>> matching_3 = MaximalBipartiteMatching(bipartite_graph_3)
    >>> matching_3.find_maximal_matching()
    3
    >>> bipartite_graph_4 = [
    ...     [1, 0, 1],
    ...     [1, 1, 0],
    ...     [0, 1, 0],
    ... ]
    >>> matching_4 = MaximalBipartiteMatching(bipartite_graph_4)
    >>> matching_4.find_maximal_matching()
    3
    """

    def __init__(self, graph: list) -> None:
        # The given bipartite graph
        self.graph = graph
        self.num_applicants = len(graph)
        self.num_jobs = len(graph[0])

    def _dfs(self, applicant: int, job_match: list, seen: list) -> bool:
        """
        Depth-First Search to find maximal matching for an applicant.

        Args:
        - applicant (int): The current applicant under consideration.
        - job_match (list): The array indicating job assignments.
        - seen (list): Array to track job availability.

        Returns:
        - Boolean: True if a matching for the applicant is possible.
        """
        for job in range(self.num_jobs):
            if self.graph[applicant][job] and not seen[job]:
                seen[job] = True
                if job_match[job] == -1 or self._dfs(job_match[job], job_match, seen):
                    job_match[job] = applicant
                    return True
        return False

    def find_maximal_matching(self) -> int:
        """
        Finds the maximal number of applicants matched to jobs.

        Returns:
        - Integer: Maximum number of matching applicants to jobs.
        """
        job_match = [-1] * self.num_jobs
        matching_count = 0
        for applicant in range(self.num_applicants):
            seen_jobs = [False] * self.num_jobs
            if self._dfs(applicant, job_match, seen_jobs):
                matching_count += 1
        return matching_count


if __name__ == "__main__":
    import doctest

    doctest.testmod()
