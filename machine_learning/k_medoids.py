"""
README, Author - Rohit Kumar Bansal (mailto:rohitbansal.dev@gmail.com)

Requirements:
  - numpy
  - matplotlib
Python:
  - 3.5+
Inputs:
  - X: 2D numpy array of features
  - k: number of clusters
Usage:
  1. Define k and X
  2. Create initial medoids:
        initial_medoids = get_initial_medoids(X, k, seed=0)
  3. Run kmedoids:
        medoids, cluster_assignment = kmedoids(
            X, k, initial_medoids, maxiter=100, verbose=True
        )
"""

import numpy as np
from matplotlib import pyplot as plt
from sklearn.metrics import pairwise_distances

def get_initial_medoids(data, k, seed=None):
    rng = np.random.default_rng(seed)
    n = data.shape[0]
    indices = rng.choice(n, k, replace=False)
    medoids = data[indices, :]
    return medoids

def assign_clusters(data, medoids):
    distances = pairwise_distances(data, medoids, metric='euclidean')
    cluster_assignment = np.argmin(distances, axis=1)
    return cluster_assignment

def revise_medoids(data, k, cluster_assignment):
    new_medoids = []
    for i in range(k):
        members = data[cluster_assignment == i]
        if len(members) == 0:
            continue
        # Compute total distance from each point to all others in cluster
        total_distances = np.sum(pairwise_distances(members, members), axis=1)
        medoid_index = np.argmin(total_distances)
        new_medoids.append(members[medoid_index])
    return np.array(new_medoids)

def compute_heterogeneity(data, k, medoids, cluster_assignment):
    heterogeneity = 0.0
    for i in range(k):
        members = data[cluster_assignment == i]
        if len(members) == 0:
            continue
        distances = pairwise_distances(members, [medoids[i]])
        heterogeneity += np.sum(distances**2)
    return heterogeneity

def kmedoids(data, k, initial_medoids, maxiter=100, verbose=False):
    medoids = initial_medoids.copy()
    prev_assignment = None
    for itr in range(maxiter):
        cluster_assignment = assign_clusters(data, medoids)
        medoids = revise_medoids(data, k, cluster_assignment)

        if prev_assignment is not None and (prev_assignment == cluster_assignment).all():
            break

        if verbose and prev_assignment is not None:
            changed = np.sum(prev_assignment != cluster_assignment)
            print(f"Iteration {itr}: {changed} points changed clusters")

        prev_assignment = cluster_assignment.copy()

    return medoids, cluster_assignment

# Optional plotting
def plot_clusters(data, medoids, cluster_assignment):
    ax = plt.axes(projection='3d')
    ax.scatter(data[:,0], data[:,1], data[:,2], c=cluster_assignment, cmap='viridis')
    ax.scatter(medoids[:,0], medoids[:,1], medoids[:,2], c='red', s=100, marker='x')
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")
    ax.set_title("3D K-Medoids Clustering")
    plt.show()

# Optional test
if __name__ == "__main__":
    from sklearn import datasets
    X = datasets.load_iris()['data']
    k = 3
    medoids = get_initial_medoids(X, k, seed=0)
    medoids, clusters = kmedoids(X, k, medoids, maxiter=50, verbose=True)
    plot_clusters(X, medoids, clusters)
