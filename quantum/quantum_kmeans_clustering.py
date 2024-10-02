import cirq
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
from sklearn.preprocessing import MinMaxScaler

def generate_data(n_samples: int = 100, n_features: int = 2, n_clusters: int = 2) -> tuple[np.ndarray, np.ndarray]:
    """
    Generates synthetic data using the make_blobs function and normalizes it.

    :param n_samples: Number of samples to generate.
    :param n_features: Number of features for each sample.
    :param n_clusters: Number of clusters to generate.
    :return: A tuple containing normalized data and labels.

    >>> data, labels = generate_data(10, 2, 2)
    >>> assert data.shape == (10, 2)
    >>> assert len(labels) == 10
    """
    data, labels = make_blobs(n_samples=n_samples, centers=n_clusters, n_features=n_features, random_state=42)
    return MinMaxScaler().fit_transform(data), labels

def quantum_distance(point1: np.ndarray, point2: np.ndarray) -> float:
    """
    Computes the quantum distance between two points.

    :param point1: First point as a numpy array.
    :param point2: Second point as a numpy array.
    :return: Quantum distance between the two points.

    >>> point_a = np.array([1.0, 2.0])
    >>> point_b = np.array([1.5, 2.5])
    >>> result = quantum_distance(point_a, point_b)
    >>> assert isinstance(result, float)
    """
    qubit = cirq.LineQubit(0)
    diff = np.clip(np.linalg.norm(point1 - point2), 0, 1)
    theta = 2 * np.arcsin(diff)
    
    circuit = cirq.Circuit(
        cirq.ry(theta)(qubit),
        cirq.measure(qubit, key='result')
    )
    
    result = cirq.Simulator().run(circuit, repetitions=1000)
    return result.histogram(key='result').get(1, 0) / 1000

def initialize_centroids(data: np.ndarray, k: int) -> np.ndarray:
    """
    Initializes centroids for k-means clustering.

    :param data: The dataset from which to initialize centroids.
    :param k: The number of centroids to initialize.
    :return: An array of initialized centroids.

    >>> data = np.array([[1, 2], [3, 4], [5, 6]])
    >>> centroids = initialize_centroids(data, 2)
    >>> assert centroids.shape == (2, 2)
    """
    return data[np.random.choice(len(data), k, replace=False)]

def assign_clusters(data: np.ndarray, centroids: np.ndarray) -> list[list[np.ndarray]]:
    """
    Assigns data points to the nearest centroid.

    :param data: The dataset to cluster.
    :param centroids: The current centroids.
    :return: A list of clusters, each containing points assigned to it.

    >>> data = np.array([[1, 2], [3, 4], [5, 6]])
    >>> centroids = np.array([[1, 2], [5, 6]])
    >>> clusters = assign_clusters(data, centroids)
    >>> assert len(clusters) == 2
    """
    clusters = [[] for _ in range(len(centroids))]
    for point in data:
        closest = min(range(len(centroids)), key=lambda i: quantum_distance(point, centroids[i]))
        clusters[closest].append(point)
    return clusters

def recompute_centroids(clusters: list[list[np.ndarray]]) -> np.ndarray:
    """
    Recomputes the centroids based on the assigned clusters.

    :param clusters: A list of clusters, each containing points assigned to it.
    :return: An array of newly computed centroids.

    >>> clusters = [[np.array([1, 2]), np.array([1, 3])], [np.array([5, 6]), np.array([5, 7])]]
    >>> centroids = recompute_centroids(clusters)
    >>> assert centroids.shape == (2, 2)
    """
    return np.array([np.mean(cluster, axis=0) for cluster in clusters if cluster])

def quantum_kmeans(data: np.ndarray, k: int, max_iters: int = 10) -> tuple[np.ndarray, list[list[np.ndarray]]]:
    """
    Applies the quantum k-means clustering algorithm.

    :param data: The dataset to cluster.
    :param k: The number of clusters.
    :param max_iters: The maximum number of iterations.
    :return: A tuple containing final centroids and clusters.

    >>> data = np.array([[1, 2], [3, 4], [5, 6]])
    >>> centroids, clusters = quantum_kmeans(data, 2)
    >>> assert centroids.shape[0] == 2
    """
    centroids = initialize_centroids(data, k)
    
    for _ in range(max_iters):
        clusters = assign_clusters(data, centroids)
        new_centroids = recompute_centroids(clusters)
        if np.allclose(new_centroids, centroids):
            break
        centroids = new_centroids
    
    return centroids, clusters

# Main execution
n_samples, n_clusters = 10, 2
data, labels = generate_data(n_samples, n_clusters=n_clusters)

plt.figure(figsize=(12, 5))

plt.subplot(121)
plt.scatter(data[:, 0], data[:, 1], c=labels)
plt.title("Generated Data")

final_centroids, final_clusters = quantum_kmeans(data, n_clusters)

plt.subplot(122)
for i, cluster in enumerate(final_clusters):
    cluster = np.array(cluster)
    plt.scatter(cluster[:, 0], cluster[:, 1], label=f'Cluster {i+1}')
plt.scatter(final_centroids[:, 0], final_centroids[:, 1], color='red', marker='x', s=200, linewidths=3, label='Centroids')
plt.title("Quantum k-Means Clustering with Cirq")
plt.legend()

plt.tight_layout()
plt.show()

print(f"Final Centroids:\n{final_centroids}") 
