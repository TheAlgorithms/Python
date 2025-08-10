"""
Von Neumann cellular automaton with multi-state fading "heatmap" effect.

This implementation demonstrates a Von Neumann cellular automaton where cells
follow custom birth/survive rules and dead cells fade gradually through multiple
visual states, creating a heatmap-like effect.

Based on Von Neumann cellular automata architecture:
https://en.wikipedia.org/wiki/Von_Neumann_cellular_automaton

Von Neumann neighborhood reference:
https://en.wikipedia.org/wiki/Von_Neumann_neighborhood

Requirements: numpy
"""

import numpy as np


def create_random_grid(
    rows: int, columns: int, alive_probability: float, seed: int | None = None
) -> np.ndarray:
    """
    Create initial grid with randomly distributed alive cells.

    Args:
        rows: Number of grid rows
        columns: Number of grid columns
        alive_probability: Probability (0.0-1.0) of each cell being initially alive
        seed: Random seed for reproducibility

    Returns:
        2D numpy array where 1 represents alive cells, 0 represents dead cells

    Raises:
        ValueError: If alive_probability is not between 0 and 1
        ValueError: If rows or columns are not positive integers

    Examples:
        >>> grid = create_random_grid(3, 3, 0.5, seed=42)
        >>> grid.shape
        (3, 3)
        >>> bool(np.all((grid == 0) | (grid == 1)))
        True
        >>> grid.dtype
        dtype('uint8')

        >>> create_random_grid(0, 3, 0.5)  # doctest: +IGNORE_EXCEPTION_DETAIL
        Traceback (most recent call last):
        ValueError: Rows and columns must be positive integers

        >>> create_random_grid(3, 3, 1.5)  # doctest: +IGNORE_EXCEPTION_DETAIL
        Traceback (most recent call last):
        ValueError: alive_probability must be between 0.0 and 1.0
    """
    if rows <= 0 or columns <= 0:
        raise ValueError("Rows and columns must be positive integers")
    if not 0.0 <= alive_probability <= 1.0:
        raise ValueError("alive_probability must be between 0.0 and 1.0")

    rng = np.random.default_rng(seed)
    alive_cells = (rng.random((rows, columns)) < alive_probability).astype(
        np.uint8
    )
    return alive_cells


def count_von_neumann_neighbors(
    alive_mask: np.ndarray, use_wraparound: bool = True
) -> np.ndarray:
    """
    Count Von Neumann neighbors for each cell (4-directional neighborhood).

    The Von Neumann neighborhood consists of the four orthogonally adjacent cells
    (up, down, left, right) but excludes diagonal neighbors.

    Args:
        alive_mask: Binary 2D array where 1 represents alive cells
        use_wraparound: If True, edges wrap around (toroidal topology)

    Returns:
        2D array with neighbor counts (0-4) for each cell

    Raises:
        ValueError: If alive_mask is not 2D or contains invalid values

    Examples:
        >>> mask = np.array([[1, 0, 1], [0, 1, 0], [1, 0, 1]], dtype=np.uint8)
        >>> counts = count_von_neumann_neighbors(mask, use_wraparound=False)
        >>> int(counts[1, 1])  # center cell has 0 neighbors (all adjacent are 0)
        0
        >>> int(counts[0, 1])  # top middle has 3 neighbors (down, left, right)
        3

        >>> mask_simple = np.array([[1, 1], [1, 0]], dtype=np.uint8)
        >>> counts_simple = count_von_neumann_neighbors(
        ...     mask_simple, use_wraparound=False
        ... )
        >>> int(counts_simple[0, 0])  # top-left has 2 neighbors (right and down)
        2

        >>> invalid_mask = np.array([1, 2, 3])  # doctest: +IGNORE_EXCEPTION_DETAIL
        >>> count_von_neumann_neighbors(invalid_mask)
        Traceback (most recent call last):
        ValueError: alive_mask must be a 2D array
    """
    if alive_mask.ndim != 2:
        raise ValueError("alive_mask must be a 2D array")
    if not np.all((alive_mask == 0) | (alive_mask == 1)):
        raise ValueError("alive_mask must contain only 0s and 1s")

    rows, cols = alive_mask.shape
    neighbor_counts = np.zeros((rows, cols), dtype=np.uint8)

    if use_wraparound:
        # Use rolling for wraparound
        up_neighbors = np.roll(alive_mask, -1, axis=0)
        down_neighbors = np.roll(alive_mask, 1, axis=0)
        left_neighbors = np.roll(alive_mask, -1, axis=1)
        right_neighbors = np.roll(alive_mask, 1, axis=1)
        neighbor_counts = (
            up_neighbors + down_neighbors + left_neighbors + right_neighbors
        )
    else:
        # Manually count neighbors without wraparound
        for r in range(rows):
            for c in range(cols):
                count = 0
                # Check up
                if r > 0 and alive_mask[r - 1, c]:
                    count += 1
                # Check down
                if r < rows - 1 and alive_mask[r + 1, c]:
                    count += 1
                # Check left
                if c > 0 and alive_mask[r, c - 1]:
                    count += 1
                # Check right
                if c < cols - 1 and alive_mask[r, c + 1]:
                    count += 1
                neighbor_counts[r, c] = count

    return neighbor_counts


def apply_cellular_automaton_rules(
    current_ages: np.ndarray,
    birth_neighbor_counts: set[int],
    survival_neighbor_counts: set[int],
    maximum_age: int = 5,
    use_wraparound: bool = True,
) -> np.ndarray:
    """
    Apply cellular automaton rules to advance the grid by one generation.

    Cells are born when they have a neighbor count in birth_neighbor_counts.
    Living cells survive when they have a neighbor count in survival_neighbor_counts.
    Dead cells age and eventually disappear completely.

    Args:
        current_ages: 2D array where values represent cell ages (0 = dead, >0 = alive)
        birth_neighbor_counts: Set of neighbor counts that cause cell birth
        survival_neighbor_counts: Set of neighbor counts that allow cell survival
        maximum_age: Maximum age before cell disappears completely
        use_wraparound: Whether to use wraparound boundaries

    Returns:
        New 2D array with updated cell ages after applying rules

    Raises:
        ValueError: If inputs are invalid

    Examples:
        >>> ages = np.array([[0, 1, 0], [1, 1, 1], [0, 1, 0]], dtype=np.uint8)
        >>> new_ages = apply_cellular_automaton_rules(
        ...     ages, birth_neighbor_counts={2},
        ...     survival_neighbor_counts={2, 3}, use_wraparound=False
        ... )
        >>> # corner should be born (2 neighbors: right and down)
        >>> bool(new_ages[0, 0] > 0)
        True

        >>> # Test aging of dead cells
        >>> dead_aging = np.array([[2, 0, 0]], dtype=np.uint8)  # age 2, no survival
        >>> result = apply_cellular_automaton_rules(
        ...     dead_aging, birth_neighbor_counts=set(),
        ...     survival_neighbor_counts=set(), maximum_age=3
        ... )
        >>> bool(result[0, 0] == 3)  # should age from 2 to 3
        True

        >>> apply_cellular_automaton_rules(
        ...     np.array([1, 2]), {1}, {1}
        ... )  # doctest: +IGNORE_EXCEPTION_DETAIL
        Traceback (most recent call last):
        ValueError: current_ages must be a 2D array
    """
    if current_ages.ndim != 2:
        raise ValueError("current_ages must be a 2D array")
    if maximum_age < 1:
        raise ValueError("maximum_age must be at least 1")

    alive_cells_mask = current_ages > 0
    neighbor_counts = count_von_neumann_neighbors(
        alive_cells_mask.astype(np.uint8), use_wraparound
    )

    # Determine which cells are born or survive
    birth_mask = (~alive_cells_mask) & np.isin(
        neighbor_counts, list(birth_neighbor_counts)
    )
    survival_mask = alive_cells_mask & np.isin(
        neighbor_counts, list(survival_neighbor_counts)
    )

    new_ages = current_ages.copy()

    # Set ages for newly born cells
    new_ages[birth_mask] = 1

    # Reset age for surviving cells (keeps them visually fresh)
    new_ages[survival_mask] = 1

    # Age cells that neither survive nor get born
    fade_mask = (~birth_mask) & (~survival_mask)
    new_ages[fade_mask & (new_ages > 0)] += 1

    # Remove cells that have exceeded maximum age
    new_ages[new_ages > maximum_age] = 0

    return new_ages


def simulate_von_neumann_cellular_automaton(
    grid_rows: int = 20,
    grid_columns: int = 40,
    initial_alive_probability: float = 0.25,
    birth_rules: set[int] | None = None,
    survival_rules: set[int] | None = None,
    maximum_cell_age: int = 5,
    generations: int = 100,
    random_seed: int | None = None,
    use_wraparound_edges: bool = True,
) -> list[np.ndarray]:
    """
    Run a complete Von Neumann cellular automaton simulation.

    This function creates an initial random grid and evolves it through multiple
    generations according to the specified birth and survival rules.

    Args:
        grid_rows: Number of rows in the grid
        grid_columns: Number of columns in the grid
        initial_alive_probability: Initial probability of cells being alive
        birth_rules: Set of neighbor counts that cause birth (default: {3})
        survival_rules: Set of neighbor counts that allow survival (default: {1, 2})
        maximum_cell_age: Maximum age before cells disappear (default: 5)
        generations: Number of generations to simulate
        random_seed: Seed for random number generation
        use_wraparound_edges: Whether to use toroidal topology

    Returns:
        List of 2D numpy arrays representing each generation

    Raises:
        ValueError: If parameters are invalid

    Examples:
        >>> result = simulate_von_neumann_cellular_automaton(
        ...     grid_rows=5, grid_columns=5, generations=3, random_seed=42
        ... )
        >>> len(result) == 3
        True
        >>> all(grid.shape == (5, 5) for grid in result)
        True

        >>> simulate_von_neumann_cellular_automaton(
        ...     generations=0
        ... )  # doctest: +IGNORE_EXCEPTION_DETAIL
        Traceback (most recent call last):
        ValueError: generations must be positive
    """
    if birth_rules is None:
        birth_rules = {3}
    if survival_rules is None:
        survival_rules = {1, 2}

    if generations <= 0:
        raise ValueError("generations must be positive")
    if grid_rows <= 0 or grid_columns <= 0:
        raise ValueError("grid dimensions must be positive")

    # Initialize grid
    current_grid = create_random_grid(
        grid_rows, grid_columns, initial_alive_probability, random_seed
    )

    generation_history = []

    # Run simulation for specified number of generations
    for _ in range(generations):
        generation_history.append(current_grid.copy())
        current_grid = apply_cellular_automaton_rules(
            current_grid,
            birth_rules,
            survival_rules,
            maximum_cell_age,
            use_wraparound_edges,
        )

    return generation_history


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
