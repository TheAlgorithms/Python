class TwoSatisfiability:
    """
    This class implements a solution to the 2-SAT (2-Satisfiability) problem
    using Kosaraju's algorithm to find strongly connected components (SCCs)
    in the implication graph.

    Brief Idea:
    -----------
    1. From each clause (a v b), we can derive implications:
         (¬a → b) and (¬b → a)

    2. We construct an implication graph using these implications.

    3. For each variable x, its negation ¬x is also represented as a node.
       If x and ¬x belong to the same SCC, the expression is unsatisfiable.

    4. Otherwise, we assign truth values based on the SCC order:
       If SCC(x) > SCC(¬x), then x = true; otherwise, x = false.

    Complexities:
    -------------
    - Time Complexity: O(n + m)
    - Space Complexity: O(n + m)

    where n is the number of variables and m is the number of clauses.

    Examples:
    ---------
    >>> # Example 1: Simple satisfiable formula
    >>> two_sat = TwoSatisfiability(3)
    >>> two_sat.add_clause(1, False, 2, False)  # (x1 v x2)
    >>> two_sat.add_clause(2, True, 3, False)   # (¬x2 v x3)
    >>> two_sat.solve()
    >>> two_sat.is_solution_exists()
    True
    >>> solution = two_sat.get_solutions()
    >>> solution
    [False, True, True, True]

    >>> # Example 2: Unsatisfiable formula
    >>> two_sat = TwoSatisfiability(1)
    >>> two_sat.add_clause(1, False, 1, False)  # (x1 v x1)
    >>> two_sat.add_clause(1, True, 1, True)    # (¬x1 v ¬x1)
    >>> two_sat.solve()
    >>> two_sat.is_solution_exists()
    False

    >>> # Example 3: Testing error handling
    >>> two_sat = TwoSatisfiability(2)
    >>> try:
    ...     two_sat.is_solution_exists()
    ... except RuntimeError as e:
    ...     print("Error caught")
    Error caught


    Reference:
    ----------
    - CP Algorithm: https://cp-algorithms.com/graph/2SAT.html
    - Wikipedia: https://en.wikipedia.org/wiki/2-satisfiability

    Author: Shoyeb Ansari (https://github.com/Shoyeb45)

    See Also:
    ---------
    Kosaraju's algorithm for finding strongly connected components
    """

    def __init__(self, number_of_variables: int) -> None:
        """
        Initializes the TwoSat solver with the given number of variables.

        Args:
            number_of_variables (int): The number of boolean variables

        Raises:
            ValueError: If the number of variables is negative
        """
        if number_of_variables < 0:
            raise ValueError("Number of variables cannot be negative.")

        self.__number_of_variables = number_of_variables
        n = 2 * number_of_variables + 1

        # Implication graph built from the boolean clauses
        self.__graph: list[list[int]] = [[] for _ in range(n)]

        # Transposed implication graph used in Kosaraju's algorithm
        self.__graph_transpose: list[list[int]] = [[] for _ in range(n)]

        # Stores one valid truth assignment for all variables (1-indexed)
        self.__variable_assignments: list[bool] = [False] * (number_of_variables + 1)

        # Indicates whether a valid solution exists
        self.__has_solution: bool = True

        # Tracks whether the solve() method has been called
        self.__is_solved: bool = False

    def add_clause(
        self,
        first_var: int,
        is_negate_first_var: bool,
        second_var: int,
        is_negate_second_var: bool,
    ) -> None:
        """
        Adds a clause of the form (a v b) to the boolean expression.

        Args:
            first_var (int): The first variable (1 ≤ a ≤ number_of_variables)
            is_negate_first_var (bool): True if variable a is negated
            second_var (int): The second variable (1 ≤ b ≤ number_of_variables)
            is_negate_second_var (bool): True if variable b is negated

        For example::

            # To add (¬x₁ v x₂), call:
            two_sat.add_clause(1, True, 2, False)

        Raises:
            ValueError: If a or b are out of range
        """
        exception_message = f"Variable number must be \
            between 1 and {self.__number_of_variables}"
        if first_var <= 0 or first_var > self.__number_of_variables:
            raise ValueError(exception_message)
        if second_var <= 0 or second_var > self.__number_of_variables:
            raise ValueError(exception_message)

        first_var = self.__negate(first_var) if is_negate_first_var else first_var
        second_var = self.__negate(second_var) if is_negate_second_var else second_var
        not_of_first_var = self.__negate(first_var)
        not_of_second_var = self.__negate(second_var)

        # Add implications: (¬first_var → second_var) and (¬second_var → first_var)
        self.__graph[not_of_first_var].append(second_var)
        self.__graph[not_of_second_var].append(first_var)

        # Build transpose graph
        self.__graph_transpose[second_var].append(not_of_first_var)
        self.__graph_transpose[first_var].append(not_of_second_var)

    def solve(self) -> None:
        """
        Solves the 2-SAT problem using Kosaraju's algorithm to find SCCs
        and determines whether a satisfying assignment exists.
        """
        self.__is_solved = True
        number_of_nodes = 2 * self.__number_of_variables + 1

        visited = [False] * number_of_nodes
        component = [0] * number_of_nodes
        topological_order: list[int] = []

        # Step 1: Perform DFS to get topological order
        for i in range(1, number_of_nodes):
            if not visited[i]:
                self.__depth_first_search_for_topological_order(
                    i, visited, topological_order
                )

        visited = [False] * number_of_nodes
        scc_id = 0

        # Step 2: Find SCCs on transposed graph
        while topological_order:
            node = topological_order.pop()
            if not visited[node]:
                self.__depth_first_search_for_scc(node, visited, component, scc_id)
                scc_id += 1

        # Step 3: Check for contradictions and assign values
        for i in range(1, self.__number_of_variables + 1):
            not_i = self.__negate(i)
            if component[i] == component[not_i]:
                self.__has_solution = False
                return
            # If SCC(i) > SCC(¬i), then variable i is true
            self.__variable_assignments[i] = component[i] > component[not_i]

    def is_solution_exists(self) -> bool:
        """
        Returns whether the given boolean formula is satisfiable.

        Returns:
            bool: True if a solution exists; False otherwise

        Raises:
            RuntimeError: If called before solve()
        """
        if not self.__is_solved:
            raise RuntimeError("Please call solve() before checking for a solution.")
        return self.__has_solution

    def get_solutions(self) -> list[bool]:
        """
        Returns one valid assignment of variables that satisfies the boolean formula.

        Returns:
            list[bool]: A boolean list where result[i] represents the truth value
                        of variable xᵢ

        Raises:
            RuntimeError: If called before solve() or if no solution exists
        """
        if not self.__is_solved:
            raise RuntimeError("Please call solve() before fetching the solution.")
        if not self.__has_solution:
            raise RuntimeError(
                "No satisfying assignment exists for the given expression."
            )
        return self.__variable_assignments.copy()

    def __depth_first_search_for_topological_order(
        self, node: int, visited: list[bool], topological_order: list[int]
    ) -> None:
        """
        Performs DFS to compute topological order.

        Args:
            node (int): Current node
            visited (list[bool]): Visited array
            topological_order (list[int]): list to store topological order
        """
        visited[node] = True
        for neighbour_node in self.__graph[node]:
            if not visited[neighbour_node]:
                self.__depth_first_search_for_topological_order(
                    neighbour_node, visited, topological_order
                )
        topological_order.append(node)

    def __depth_first_search_for_scc(
        self, node: int, visited: list[bool], component: list[int], scc_id: int
    ) -> None:
        """
        Performs DFS on the transposed graph to identify SCCs.

        Args:
            node (int): Current node
            visited (list[bool]): Visited array
            component (list[int]): Array to store component IDs
            scc_id (int): Current SCC identifier
        """
        visited[node] = True
        component[node] = scc_id
        for neighbour_node in self.__graph_transpose[node]:
            if not visited[neighbour_node]:
                self.__depth_first_search_for_scc(
                    neighbour_node, visited, component, scc_id
                )

    def __negate(self, variable_index: int) -> int:
        """
        Returns the index representing the negation of the given variable index.

        Args:
            variable_index (int): The variable index

        Mapping rule:
        -------------
        For a variable i:
            negate(i) = i + n
        For a negated variable (i + n):
            negate(i + n) = i
        where n = number_of_variables


        Returns:
            int:
                The index representing its negation
        """
        return (
            variable_index + self.__number_of_variables
            if variable_index <= self.__number_of_variables
            else variable_index - self.__number_of_variables
        )
