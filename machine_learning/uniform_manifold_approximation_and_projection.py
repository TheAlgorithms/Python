"""
Uniform Manifold Approximation and Projection (UMAP)
=====================================================

UMAP is a dimensionality reduction technique — it takes high-dimensional data
(e.g. 4 features in Iris) and compresses it into 2D or 3D so we can visualize
and understand it.

Think of it like this:
  - Imagine 150 students, each described by 4 exam scores.
  - UMAP "maps" them onto a 2D sheet of paper so that students who scored
    similarly end up near each other on the sheet.

How UMAP works (simplified, educational version):
  Step 1 — Compute pairwise distances between all data points.
  Step 2 — For each point, find its k nearest neighbours.
  Step 3 — Build a "fuzzy" graph: nearby neighbours get high membership
            strength, faraway points get low strength.
  Step 4 — Start with a random 2D layout, then iteratively pull neighbours
            closer and push non-neighbours further apart.

This implementation is intentionally simplified for learning purposes.
It does NOT replicate the full UMAP paper math, but faithfully captures
the core ideas using only NumPy and scikit-learn.

References:
    https://umap-learn.readthedocs.io/en/latest/how_umap_works.html
    https://en.wikipedia.org/wiki/Nonlinear_dimensionality_reduction
    McInnes, L., Healy, J., & Melville, J. (2018). UMAP: Uniform Manifold
    Approximation and Projection for Dimension Reduction. arXiv:1802.03426.
"""

import doctest

import numpy as np
from numpy import ndarray
from sklearn.datasets import load_iris

# ---------------------------------------------------------------------------
# Step 0 — Load dataset
# ---------------------------------------------------------------------------


def collect_dataset() -> tuple[ndarray, ndarray]:
    """
    Load the Iris dataset and return features and class labels.

    The Iris dataset has 150 flowers, each described by 4 measurements:
    sepal length, sepal width, petal length, petal width.

    Returns:
        tuple[ndarray, ndarray]:
            - features : shape (150, 4)  — the 4 measurements per flower
            - targets  : shape (150,)    — flower species (0, 1, or 2)

    >>> features, targets = collect_dataset()
    >>> features.shape
    (150, 4)
    >>> targets.shape
    (150,)
    >>> int(targets.min()), int(targets.max())
    (0, 2)
    """
    iris = load_iris()
    return np.array(iris.data), np.array(iris.target)


# ---------------------------------------------------------------------------
# Step 1 — Pairwise Euclidean distances
# ---------------------------------------------------------------------------


def compute_pairwise_distances(data: ndarray) -> ndarray:
    """
    Compute the Euclidean distance between every pair of data points.

    For n points in d-dimensional space this returns an (n x n) matrix
    where entry [i, j] is the straight-line distance between point i and j.

    The diagonal is 0 because a point has zero distance to itself.

    Args:
        data: Array of shape (n_samples, n_features).

    Returns:
        ndarray: Symmetric distance matrix of shape (n_samples, n_samples).

    >>> pts = np.array([[0.0, 0.0], [3.0, 4.0]])
    >>> d = compute_pairwise_distances(pts)
    >>> float(round(d[0, 1], 4))
    5.0
    >>> float(d[0, 0])
    0.0
    """
    # ||a - b||^2 = ||a||^2 + ||b||^2 - 2*a·b
    squared_norms = np.sum(data**2, axis=1)  # shape (n,)
    squared_dists = (
        squared_norms[:, np.newaxis]
        - 2.0 * data @ data.T
        + squared_norms[np.newaxis, :]
    )
    # Numerical noise can make tiny values negative — clamp to 0
    squared_dists = np.maximum(squared_dists, 0.0)
    return np.sqrt(squared_dists)


# ---------------------------------------------------------------------------
# Step 2 — k-Nearest Neighbours
# ---------------------------------------------------------------------------


def find_nearest_neighbors(distance_matrix: ndarray, n_neighbors: int) -> ndarray:
    """
    For every point, find the indices of its k closest neighbours.

    UMAP's core idea: the structure of the data is captured by *who is
    close to whom*, not the exact distances.

    Args:
        distance_matrix: Symmetric (n x n) distance matrix.
        n_neighbors:     How many neighbours to keep per point (k).

    Returns:
        ndarray: Integer array of shape (n_samples, n_neighbors).
                 Row i contains the indices of point i's k nearest neighbours
                 (not including itself).

    >>> dist = np.array([[0., 1., 2.], [1., 0., 3.], [2., 3., 0.]])
    >>> nn = find_nearest_neighbors(dist, n_neighbors=1)
    >>> nn.tolist()
    [[1], [0], [0]]
    """
    n_samples = distance_matrix.shape[0]
    neighbor_indices = np.zeros((n_samples, n_neighbors), dtype=int)

    for i in range(n_samples):
        # argsort gives indices that would sort the row (ascending)
        # skip index 0 because that is the point itself (distance = 0)
        sorted_indices = np.argsort(distance_matrix[i])
        neighbor_indices[i] = sorted_indices[1 : n_neighbors + 1]

    return neighbor_indices


# ---------------------------------------------------------------------------
# Step 3 — Fuzzy membership strengths (the "fuzzy graph")
# ---------------------------------------------------------------------------


def compute_membership_strengths(
    distance_matrix: ndarray,
    neighbor_indices: ndarray,
) -> ndarray:
    """
    Assign a "how strongly connected?" weight to every (point, neighbour) pair.

    In the original UMAP paper this comes from constructing a fuzzy simplicial
    set.  Here we use a simpler but conceptually equivalent idea:

        strength(i, j) = exp( -(dist(i,j) - rho_i) / sigma_i )

    where
        rho_i   = distance to the nearest neighbour of i  (local scale)
        sigma_i = mean distance to all k neighbours of i  (bandwidth)

    Points that are very close get strength ≈ 1.
    Points that are far apart get strength ≈ 0.

    The result is a sparse (n x n) weight matrix.  Only neighbour entries
    are non-zero; the rest stay 0.

    Args:
        distance_matrix:  (n x n) Euclidean distance matrix.
        neighbor_indices: (n x k) nearest-neighbour index array.

    Returns:
        ndarray: Weight matrix of shape (n_samples, n_samples).

    >>> dist = np.array([[0., 1., 2.], [1., 0., 3.], [2., 3., 0.]])
    >>> nn = find_nearest_neighbors(dist, n_neighbors=1)
    >>> W = compute_membership_strengths(dist, nn)
    >>> W.shape
    (3, 3)
    >>> float(round(W[0, 1], 4))  # nearest neighbour → strength = 1.0
    1.0
    """
    n_samples = distance_matrix.shape[0]
    weights = np.zeros((n_samples, n_samples))

    for i in range(n_samples):
        nbr_idx = neighbor_indices[i]  # indices of k neighbours
        nbr_dists = distance_matrix[i, nbr_idx]  # distances to those neighbours

        rho_i = nbr_dists.min()  # nearest-neighbour distance
        sigma_i = nbr_dists.mean() + 1e-10  # average distance (bandwidth)

        for j_pos, j in enumerate(nbr_idx):
            d = nbr_dists[j_pos]
            strength = np.exp(-(d - rho_i) / sigma_i)
            weights[i, j] = strength

    # Symmetrise: if i→j OR j→i has an edge, keep the max weight
    weights = np.maximum(weights, weights.T)
    return weights


# ---------------------------------------------------------------------------
# Step 4 — Optimise the 2-D layout (attractive + repulsive forces)
# ---------------------------------------------------------------------------


def optimize_embedding(
    weight_matrix: ndarray,
    n_components: int = 2,
    n_epochs: int = 200,
    learning_rate: float = 1.0,
    repulsion_strength: float = 1.0,
    random_state: int = 42,
) -> ndarray:
    """
    Place points in low-dimensional space so that the fuzzy graph structure
    is preserved as faithfully as possible.

    Optimisation idea (force-directed layout):
      • Connected pairs  → attract each other  (pull together)
      • All other pairs  → repel each other    (push apart)

    Each iteration nudges every point slightly in the direction that makes
    connected neighbours closer and disconnected points further away.

    Args:
        weight_matrix:     (n x n) fuzzy membership strengths.
        n_components:      Target number of output dimensions (usually 2).
        n_epochs:          Number of optimisation passes.
        learning_rate:     Step size for each gradient update.
        repulsion_strength: How strongly non-neighbours are pushed apart.
        random_state:      Seed for reproducibility.

    Returns:
        ndarray: Embedding of shape (n_samples, n_components).

    >>> rng = np.random.default_rng(0)
    >>> W = rng.random((5, 5))
    >>> W = (W + W.T) / 2          # make symmetric
    >>> emb = optimize_embedding(W, n_components=2, n_epochs=5)
    >>> emb.shape
    (5, 2)
    """
    rng = np.random.default_rng(random_state)
    n_samples = weight_matrix.shape[0]

    # Initialise embedding randomly in a small range
    embedding = rng.uniform(low=-10.0, high=10.0, size=(n_samples, n_components))

    for epoch in range(n_epochs):
        # Decay learning rate gently over time
        alpha = learning_rate * (1.0 - epoch / n_epochs)

        for i in range(n_samples):
            for j in range(n_samples):
                if i == j:
                    continue

                diff = embedding[i] - embedding[j]
                dist2 = np.dot(diff, diff) + 1e-6  # squared distance + epsilon

                w = weight_matrix[i, j]

                if w > 0:
                    # --- Attractive force ---
                    # Pull i toward j proportional to edge weight
                    grad = -2.0 * w * diff / (dist2 + 1.0)
                else:
                    # --- Repulsive force ---
                    # Push i away from j
                    grad = 2.0 * repulsion_strength * diff / (dist2 * (0.1 + dist2))

                embedding[i] += alpha * grad

    return embedding


# ---------------------------------------------------------------------------
# Public API — apply_umap()
# ---------------------------------------------------------------------------


def apply_umap(
    data: ndarray,
    n_components: int = 2,
    n_neighbors: int = 15,
    n_epochs: int = 200,
    learning_rate: float = 0.01,
    random_state: int = 42,
) -> ndarray:
    """
    Apply the full (educational) UMAP pipeline to reduce data dimensionality.

    This chains all four steps:
        collect distances → find neighbours → build fuzzy graph → optimise layout

    Args:
        data:          Input data of shape (n_samples, n_features).
        n_components:  Number of output dimensions (default 2).
        n_neighbors:   Number of nearest neighbours to consider (default 15).
                       Smaller k → more local structure.
                       Larger k  → more global structure.
        n_epochs:      Optimisation iterations (more = better but slower).
        learning_rate: Step size for embedding updates.
        random_state:  Seed for reproducibility.

    Returns:
        ndarray: Reduced embedding of shape (n_samples, n_components).

    >>> features, _ = collect_dataset()
    >>> embedding = apply_umap(features, n_components=2, n_epochs=5)
    >>> embedding.shape
    (150, 2)
    """
    if n_components < 1:
        raise ValueError("n_components must be >= 1")
    if n_neighbors < 1:
        raise ValueError("n_neighbors must be >= 1")
    if n_epochs < 1:
        raise ValueError("n_epochs must be >= 1")

    # Step 1 — Distances
    dist_matrix = compute_pairwise_distances(data)

    # Step 2 — Nearest neighbours
    nn_indices = find_nearest_neighbors(dist_matrix, n_neighbors)

    # Step 3 — Fuzzy graph
    weights = compute_membership_strengths(dist_matrix, nn_indices)

    # Step 4 — Optimise layout
    embedding = optimize_embedding(
        weights,
        n_components=n_components,
        n_epochs=n_epochs,
        learning_rate=learning_rate,
        random_state=random_state,
    )

    return embedding


# ---------------------------------------------------------------------------
# main()
# ---------------------------------------------------------------------------


def main() -> None:
    """
    Run educational UMAP on the Iris dataset and print the first 5 embeddings.

    >>> main()  # doctest: +ELLIPSIS
    === Educational UMAP on the Iris Dataset ===
    ...
    """
    print("=== Educational UMAP on the Iris Dataset ===")
    print()
    print("Loading Iris dataset …")
    features, labels = collect_dataset()
    print(f"  Input shape  : {features.shape}  ((150 flowers x 2 dimensions))")
    print()

    print("Running UMAP (n_neighbors=5, n_epochs=50) …")
    print("  (Using reduced epochs for speed — increase for better results)")
    embedding = apply_umap(
        features,
        n_components=2,
        n_neighbors=5,
        n_epochs=50,
        random_state=0,
    )

    print(f"  Output shape : {embedding.shape}  ((150 flowers x 2 dimensions))")
    print()

    print("First 5 embedded points (each flower is now a 2-D coordinate):")
    print(f"  {'Point':>5}  {'Species':>10}  {'Dim-1':>10}  {'Dim-2':>10}")
    species_names = {0: "Setosa", 1: "Versicolor", 2: "Virginica"}
    for idx in range(5):
        name = species_names[int(labels[idx])]
        x, y = embedding[idx]
        print(f"  {idx:>5}  {name:>10}  {x:>10.4f}  {y:>10.4f}")

    print()
    print("Interpretation:")
    print("  Points belonging to the same species should cluster together.")
    print("  UMAP has compressed 4-D information into 2-D while preserving")
    print("  neighbourhood structure — similar flowers stay near each other.")

    # ── Optional visualisation ──────────────────────────────────────────────
    # Uncomment the block below if matplotlib is available:
    #
    # import matplotlib.pyplot as plt
    # colours = ["red", "green", "blue"]
    # for species_id in range(3):
    #     mask = labels == species_id
    #     plt.scatter(
    #         embedding[mask, 0],
    #         embedding[mask, 1],
    #         c=colours[species_id],
    #         label=species_names[species_id],
    #         alpha=0.7,
    #     )
    # plt.title("Educational UMAP — Iris Dataset")
    # plt.xlabel("UMAP Dimension 1")
    # plt.ylabel("UMAP Dimension 2")
    # plt.legend()
    # plt.tight_layout()
    # plt.show()


if __name__ == "__main__":
    doctest.testmod(verbose=False)
    main()
