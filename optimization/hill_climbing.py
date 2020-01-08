import math
import matplotlib.pyplot as plt


class SearchProblem:
    """
    A interface to define search problems. The interface will be illustrated using
        the example of mathematical function.
    """

    def __init__(
        self, x_coordinate: int, y_coordinate: int, step: int, function_to_optimize
    ):
        """
        The constructor of the search problem.
            x_coordinate: an integer representing the current x co-ordinate of the current search state.
            y_coordinate: an integer representing the current y co-ordinate of the current search state.
            step: an integer representing the size of the step to take when looking for neighbors.
            function_to_optimize: a function to optimize having the signature f(x,y).
        """
        self.x = x_coordinate
        self.y = y_coordinate
        self.step_size = step
        self.function = function_to_optimize

    def score(self) -> int:
        """
        Returns the function output at the current x and y co-ordinates.
        >>> def test_function(x,y): return x + y
        >>> SearchProblem(0, 0, 1, test_function).score() #should return 0 as 0 + 0 = 0
        0

        >>> SearchProblem(5, 7, 1, test_function).score() #should 12 as 5 + 7 = 12
        12
        """
        return self.function(self.x, self.y)

    def get_neighbors(self):
        """
        Returns a list of neighbors. Neighbors are co_ordinates adjacent to the current co_ordinates.
        """
        current_x = self.x
        current_y = self.y
        neighbors = [None for i in range(8)]  # creating an empty list of size 8.
        neighbors[0] = SearchProblem(
            current_x + self.step_size, current_y, self.step_size, self.function
        )
        neighbors[1] = SearchProblem(
            current_x + self.step_size,
            current_y + self.step_size,
            self.step_size,
            self.function,
        )
        neighbors[2] = SearchProblem(
            current_x, current_y + self.step_size, self.step_size, self.function
        )
        neighbors[3] = SearchProblem(
            current_x - self.step_size,
            current_y + self.step_size,
            self.step_size,
            self.function,
        )
        neighbors[4] = SearchProblem(
            current_x - self.step_size, current_y, self.step_size, self.function
        )
        neighbors[5] = SearchProblem(
            current_x - self.step_size,
            current_y - self.step_size,
            self.step_size,
            self.function,
        )
        neighbors[6] = SearchProblem(
            current_x, current_y - self.step_size, self.step_size, self.function
        )
        neighbors[7] = SearchProblem(
            current_x + self.step_size,
            current_y - self.step_size,
            self.step_size,
            self.function,
        )
        return neighbors

    def __hash__(self):
        """
        utility function to hash the current search state.
        """
        return hash(
            str(self)
        )  # hashing the string represetation of the current search state.

    def __str__(self):
        """
        utility function for the string representation of the current search state.
        >>> str(SearchProblem(0, 0, 1, None))
        'x: 0 y: 0'

        >>> str(SearchProblem(2, 5, 1, None))
        'x: 2 y: 5'
        """
        return "x: " + str(self.x) + " y: " + str(self.y)


def hill_climbing(
    search_prob,
    find_max: bool = True,
    max_x: float = math.inf,
    min_x: float = -math.inf,
    max_y: float = math.inf,
    min_y: float = -math.inf,
    visualization: bool = False,
    max_iter: int = 10000,
) -> SearchProblem:
    """
    implementation of the hill climbling algorithm. We start with a given state, find all its neighbors, move towards
        the neighbor which provides the maximum (or minimum) change. We keep doing this untill we are at a state where
        we do not have any neighbors which can improve the solution.
        Args:
            search_prob: The search state at the start.
            find_max: Whether to find the maximum or not. If False, the algorithm finds the minimum.
            max_x, min_x, max_y, min_y: integers representing the maximum and minimum bounds of x and y.
            visualization: a flag to switch visualization off. If True, provides a matplotlib graph at the end of execution.
            max_iter: number of times to run the iteration.
        Returns a search state having the maximum (or minimum) score.
    """
    current_state = search_prob
    scores = []  # list to store the current score at each iteration
    iterations = 0
    solution_found = False
    visited = set()
    while not solution_found and iterations < max_iter:
        visited.add(current_state)
        iterations += 1
        current_score = current_state.score()
        scores.append(current_score)
        neighbors = current_state.get_neighbors()
        max_change = -math.inf
        min_change = math.inf
        next_state = None  # to hold the next best neighbor
        for neighbor in neighbors:
            if neighbor in visited:
                continue  # do not want to visit the same state again
            if (
                neighbor.x > max_x
                or neighbor.x < min_x
                or neighbor.y > max_y
                or neighbor.y < min_y
            ):
                continue  # neighbor outside our bounds
            change = neighbor.score() - current_score
            if find_max:  # finding max
                if (
                    change > max_change and change > 0
                ):  # going to direction with greatest ascent
                    max_change = change
                    next_state = neighbor
            else:  # finding min
                if (
                    change < min_change and change < 0
                ):  # to direction with greatest descent
                    min_change = change
                    next_state = neighbor
        if (
            next_state is not None
        ):  # we found atleast one neighbor which improved the current state
            current_state = next_state
        else:
            solution_found = True  # since we have no neighbor that improves the solution we stop the search

    if visualization:
        plt.plot(range(iterations), scores)
        plt.xlabel("Iterations")
        plt.ylabel("Funcation values")
        plt.show()

    return current_state


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    def test_f1(x, y):
        return (x ** 2) + (y ** 2)

    prob = SearchProblem(
        x_coordinate=3, y_coordinate=4, step=1, function_to_optimize=test_f1
    )  # starting the problem with initial co_ordinates (3,4)
    local_min = hill_climbing(prob, find_max=False)
    print(
        f"The minimum score for f(x,y) = x^2 + y^2 found via hill climbing: {local_min.score()}"
    )

    prob = SearchProblem(
        x_coordinate=12, y_coordinate=47, step=1, function_to_optimize=test_f1
    )  # starting the problem with initial co_ordinates (3,4)
    local_min = hill_climbing(
        prob, find_max=False, max_x=100, min_x=5, max_y=50, min_y=-5, visualization=True
    )
    print(
        f"The minimum score for f(x,y) = x^2 + y^2 with the domain 100 > x > 5 and 50 > y > - 5 found via hill climbing: {local_min.score()}"
    )

    def test_f2(x, y):
        return (3 * x ** 2) - (6 * y)

    prob = SearchProblem(
        x_coordinate=3, y_coordinate=4, step=1, function_to_optimize=test_f1
    )
    local_min = hill_climbing(prob, find_max=True)
    print(
        f"The maximum score for f(x,y) = x^2 + y^2 found via hill climbing: {local_min.score()}"
    )
