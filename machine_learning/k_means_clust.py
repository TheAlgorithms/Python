"""
Utilities for a minimal K-Means clustering workflow.

The implementation uses Euclidean distance, stops once assignments stabilize, and
offers helpers for plotting as well as a small reporting utility for clustered
DataFrames.

Time complexity: O(maxiter * n_samples * k * n_features)
Space complexity: O(n_samples * n_features + k * n_features)
"""

import os
import tempfile
import warnings
from collections.abc import Sequence

import numpy as np
import pandas as pd
from numpy.typing import NDArray
from sklearn.metrics import pairwise_distances

warnings.filterwarnings("ignore")

TAG = "K-MEANS-CLUST/ "


def get_initial_centroids(
    data: NDArray[np.floating], k: int, seed: int | None = None
) -> NDArray[np.floating]:
    """Randomly choose ``k`` rows as initial centroids.

    >>> data = np.arange(12).reshape(6, 2)
    >>> centroids = get_initial_centroids(data, k=2, seed=0)
    >>> centroids.shape
    (2, 2)
    >>> set(map(tuple, centroids.tolist())).issubset(
    ...     set(map(tuple, data.tolist()))
    ... )
    True
    """
    if k <= 0:
        raise ValueError("k must be positive")
    if k > len(data):
        raise ValueError("k cannot exceed the number of data points")

    # useful for obtaining consistent results
    rng = np.random.default_rng(seed)
    n = data.shape[0]  # number of data points

    # Pick K indices from range [0, N).
    rand_indices = rng.integers(0, n, k)

    # Keep centroids as dense format, as many entries will be nonzero due to averaging.
    # As long as at least one document in a cluster contains a word,
    # it will carry a nonzero weight in the TF-IDF vector of the centroid.
    centroids = data[rand_indices, :]

    return np.asarray(centroids)


def centroid_pairwise_dist(
    x: NDArray[np.floating], centroids: NDArray[np.floating]
) -> NDArray[np.floating]:
    """Compute Euclidean distances between every row in ``x`` and each centroid."""
    return pairwise_distances(x, centroids, metric="euclidean")


def assign_clusters(
    data: NDArray[np.floating], centroids: NDArray[np.floating]
) -> np.ndarray:
    """Assign each row to its closest centroid.

    >>> data = np.array([[0.0, 0.0], [0.0, 1.0], [5.0, 5.0]])
    >>> assign_clusters(data, np.array([[0.0, 0.0], [4.0, 4.0]])).tolist()
    [0, 0, 1]
    """
    distances_from_centroids = centroid_pairwise_dist(data, centroids)

    cluster_assignment = np.argmin(distances_from_centroids, axis=1)

    return cluster_assignment


def revise_centroids(
    data: NDArray[np.floating], k: int, cluster_assignment: np.ndarray
) -> NDArray[np.floating]:
    """Recompute centroids as the mean of the assigned samples.

    >>> data = np.array([[0.0, 0.0], [0.0, 1.0], [5.0, 5.0]])
    >>> revise_centroids(data, 2, np.array([0, 0, 1]))
    array([[0. , 0.5],\n       [5. , 5. ]])
    """
    new_centroids: list[NDArray[np.floating]] = []
    for i in range(k):
        member_data_points = data[cluster_assignment == i]
        centroid = member_data_points.mean(axis=0)
        new_centroids.append(centroid)
    new_centroids = np.array(new_centroids)

    return new_centroids


def compute_heterogeneity(
    data: NDArray[np.floating],
    k: int,
    centroids: NDArray[np.floating],
    cluster_assignment: np.ndarray,
) -> float:
    """Return the within-cluster sum of squared distances.

    >>> data = np.array([[0.0, 0.0], [0.0, 1.0], [5.0, 5.0]])
    >>> centroids = np.array([[0.0, 0.5], [5.0, 5.0]])
    >>> compute_heterogeneity(data, 2, centroids, np.array([0, 0, 1]))
    0.5
    """
    heterogeneity = 0.0
    for i in range(k):
        member_data_points = data[cluster_assignment == i, :]

        if member_data_points.shape[0] > 0:  # check if i-th cluster is non-empty
            distances = pairwise_distances(
                member_data_points, [centroids[i]], metric="euclidean"
            )
            squared_distances = distances**2
            heterogeneity += np.sum(squared_distances)

    return heterogeneity


def plot_heterogeneity(heterogeneity, k):
    from matplotlib import pyplot as plt

    # Matplotlib tries to create a config directory on import; fall back to a
    # temporary location when the default is not writable (e.g. CI sandboxes).
    os.environ.setdefault("MPLCONFIGDIR", tempfile.gettempdir())

    plt.figure(figsize=(7, 4))
    plt.plot(heterogeneity, linewidth=4)
    plt.xlabel("# Iterations")
    plt.ylabel("Heterogeneity")
    plt.title(f"Heterogeneity of clustering over time, K={k:d}")
    plt.rcParams.update({"font.size": 16})
    plt.show()


def plot_kmeans(data, centroids, cluster_assignment):
    from matplotlib import pyplot as plt

    os.environ.setdefault("MPLCONFIGDIR", tempfile.gettempdir())

    ax = plt.axes(projection="3d")
    ax.scatter(data[:, 0], data[:, 1], data[:, 2], c=cluster_assignment, cmap="viridis")
    ax.scatter(
        centroids[:, 0], centroids[:, 1], centroids[:, 2], c="red", s=100, marker="x"
    )
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")
    ax.set_title("3D K-Means Clustering Visualization")
    plt.show()


def kmeans(
    data: NDArray[np.floating],
    k: int,
    initial_centroids: NDArray[np.floating],
    maxiter: int = 500,
    record_heterogeneity: list[float] | None = None,
    verbose: bool = False,
) -> tuple[NDArray[np.floating], np.ndarray]:
    """Run k-means on ``data`` starting from ``initial_centroids``.

    The algorithm stops early once all assignments stabilize. Heterogeneity values
    are appended to ``record_heterogeneity`` when provided.

    >>> dataset = np.array([[0.0, 0.0], [0.0, 1.0], [5.0, 5.0]])
    >>> heterogeneity: list[float] = []
    >>> centroids, labels = kmeans(
    ...     dataset,
    ...     k=2,
    ...     initial_centroids=np.array([[0.0, 0.0], [5.0, 5.0]]),
    ...     maxiter=10,
    ...     record_heterogeneity=heterogeneity,
    ... )
    >>> labels.tolist()
    [0, 0, 1]
    >>> [round(value, 3) for value in heterogeneity]
    [0.5]
    >>> np.allclose(centroids, np.array([[0.0, 0.5], [5.0, 5.0]]))
    True
    """
    centroids = initial_centroids[:]
    prev_cluster_assignment = None

    for itr in range(maxiter):
        if verbose:
            print(itr, end="")

        # 1. Make cluster assignments using nearest centroids
        cluster_assignment = assign_clusters(data, centroids)

        # 2. Compute a new centroid for each of the k clusters, averaging all data
        #    points assigned to that cluster.
        centroids = revise_centroids(data, k, cluster_assignment)

        # Check for convergence: if none of the assignments changed, stop
        if (
            prev_cluster_assignment is not None
            and (prev_cluster_assignment == cluster_assignment).all()
        ):
            break

        # Print number of new assignments
        if prev_cluster_assignment is not None:
            num_changed = np.sum(prev_cluster_assignment != cluster_assignment)
            if verbose:
                print(
                    f"    {num_changed:5d} elements changed their cluster assignment."
                )

        # Record heterogeneity convergence metric
        if record_heterogeneity is not None:
            # YOUR CODE HERE
            score = compute_heterogeneity(data, k, centroids, cluster_assignment)
            record_heterogeneity.append(score)

        prev_cluster_assignment = cluster_assignment[:]

    return centroids, cluster_assignment


# Mock test below
if False:  # change to true to run this test case.
    from sklearn import datasets as ds

    dataset = ds.load_iris()
    k = 3
    heterogeneity = []
    initial_centroids = get_initial_centroids(dataset["data"], k, seed=0)
    centroids, cluster_assignment = kmeans(
        dataset["data"],
        k,
        initial_centroids,
        maxiter=400,
        record_heterogeneity=heterogeneity,
        verbose=True,
    )
    plot_heterogeneity(heterogeneity, k)
    plot_kmeans(dataset["data"], centroids, cluster_assignment)


def report_generator(
    predicted: pd.DataFrame,
    clustering_variables: Sequence[str],
    fill_missing_report: dict[str, float] | None = None,
) -> pd.DataFrame:
    """
    Generate a clustering summary report for a labelled ``predicted`` DataFrame.

    This helper groups numeric columns by the ``Cluster`` label, computes summary
    statistics, and marks the columns listed in ``clustering_variables``.

    >>> predicted = pd.DataFrame(
    ...     {'spend': [0.0, 50.0, 100.0], 'Cluster': [0, 0, 1]}
    ... )
    >>> report = report_generator(predicted, clustering_variables=['spend'])
    >>> report.loc[report['Features'] == '# of Customers', 0].iloc[0]
    2.0
    >>> float(report.loc[report['Features'] == '% of Customers', 1])
    0.3333333333333333
    >>> bool(report.loc[report['Features'] == 'spend', 'Mark'].iloc[0])
    True
    """
    # Fill missing values with given rules
    if fill_missing_report is not None:
        predicted = predicted.fillna(value=fill_missing_report)
    predicted["dummy"] = 1
    numeric_cols = predicted.select_dtypes(np.number).columns
    report = (
        predicted.groupby(["Cluster"])[  # construct report dataframe
            numeric_cols
        ]  # group by cluster number
        .agg(
            [
                ("sum", "sum"),
                ("mean_with_zeros", lambda x: np.mean(np.nan_to_num(x))),
                ("mean_without_zeros", lambda x: x.replace(0, np.nan).mean()),
                (
                    "mean_25-75",
                    lambda x: np.mean(
                        np.nan_to_num(
                            sorted(x)[
                                round(len(x) * 25 / 100) : round(len(x) * 75 / 100)
                            ]
                        )
                    ),
                ),
                ("mean_with_na", "mean"),
                ("min", lambda x: x.min()),
                ("5%", lambda x: x.quantile(0.05)),
                ("25%", lambda x: x.quantile(0.25)),
                ("50%", lambda x: x.quantile(0.50)),
                ("75%", lambda x: x.quantile(0.75)),
                ("95%", lambda x: x.quantile(0.95)),
                ("max", lambda x: x.max()),
                ("count", lambda x: x.count()),
                ("stdev", lambda x: x.std()),
                ("mode", lambda x: x.mode()[0]),
                ("median", lambda x: x.median()),
                ("# > 0", lambda x: (x > 0).sum()),
            ]
        )
        .T.reset_index()
        .rename(index=str, columns={"level_0": "Features", "level_1": "Type"})
    )  # rename columns
    # calculate the size of cluster(count of clientID's)
    # avoid SettingWithCopyWarning
    clustersize = report[
        (report["Features"] == "dummy") & (report["Type"] == "count")
    ].copy()
    # rename created predicted cluster to match report column names
    clustersize.Type = "ClusterSize"
    clustersize.Features = "# of Customers"
    # calculating the proportion of cluster
    clusterproportion = pd.DataFrame(
        clustersize.iloc[:, 2:].to_numpy() / clustersize.iloc[:, 2:].to_numpy().sum()
    )
    # rename created predicted cluster to match report column names
    clusterproportion["Type"] = "% of Customers"
    clusterproportion["Features"] = "ClusterProportion"
    cols = clusterproportion.columns.tolist()
    cols = cols[-2:] + cols[:-2]
    clusterproportion = clusterproportion[cols]  # rearrange columns to match report
    clusterproportion.columns = report.columns
    # generating dataframe with count of nan values
    a = pd.DataFrame(
        abs(
            report[report["Type"] == "count"].iloc[:, 2:].to_numpy()
            - clustersize.iloc[:, 2:].to_numpy()
        )
    )
    a["Features"] = 0
    a["Type"] = "# of nan"
    # filling values in order to match report
    a.Features = report[report["Type"] == "count"].Features.tolist()
    cols = a.columns.tolist()
    cols = cols[-2:] + cols[:-2]
    a = a[cols]  # rearrange columns to match report
    a.columns = report.columns  # rename columns to match report
    # drop count values except for cluster size
    report = report.drop(report[report.Type == "count"].index)
    # concat report with cluster size and nan values
    report = pd.concat([report, a, clustersize, clusterproportion], axis=0)
    report["Mark"] = report["Features"].isin(clustering_variables)
    cols = report.columns.tolist()
    cols = cols[0:2] + cols[-1:] + cols[2:-1]
    report = report[cols]
    sorter1 = {
        "ClusterSize": 9,
        "ClusterProportion": 8,
        "mean_with_zeros": 7,
        "mean_with_na": 6,
        "max": 5,
        "50%": 4,
        "min": 3,
        "25%": 2,
        "75%": 1,
        "# of nan": 0,
        "# > 0": -1,
        "sum_with_na": -2,
    }
    report = (
        report.assign(
            Sorter1=lambda x: x.Type.map(sorter1),
            Sorter2=lambda x: list(reversed(range(len(x)))),
        )
        .sort_values(["Sorter1", "Mark", "Sorter2"], ascending=False)
        .drop(["Sorter1", "Sorter2"], axis=1)
    )
    report.columns.name = ""
    report = report.reset_index()
    report = report.drop(columns=["index"])
    return report


if __name__ == "__main__":
    import doctest

    doctest.testmod()
