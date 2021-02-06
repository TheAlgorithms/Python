#!/usr/local/bin/python3
"""
Requirements:
  - sklearn
  - numpy
Python:
  - 3.7
Hierarchical clustering (HC) is a method of cluster analysis which seeks to build
a hierarchy of clusters. The code contains Agglomerative approach for
hierarchical clustering.
Agglomerative: This is a "bottom-up" approach. Each observation starts
in its own cluster, and pairs of clusters are merged as one moves up the hierarchy.
"""

import warnings

import numpy as np
from sklearn import datasets as ds
from sklearn.cluster import AgglomerativeClustering
from sklearn.metrics import homogeneity_score, jaccard_score
from sklearn.metrics.cluster import adjusted_rand_score

warnings.filterwarnings("ignore")


def dist_matrix(data):
    """
    Calculate euclidean distance matrix for the given data.

    Parameters
    ----------
    data : np.array
        contains our dataset in numpy array [NxF]

    Returns
    -------
    dist : np.array
        distance matrix containing euclidean distance between one point
        with all other points [NxN]
    """
    dist = np.zeros(shape=(data.shape[0], data.shape[0]))
    for i in range(data.shape[0]):
        for j in range(data.shape[0]):
            dist[i][j] = np.sqrt(np.sum(pow((data[i] - data[j]), 2)))
    return dist


def inter_cluster_dist_method(data, clusters, dist, a, b, method="max"):
    """
    Min: Distance between two clusters is represented by the
    distance of the closest pair of data objects belonging to
    different clusters.

    Max: Distance between two clusters is represented by the
    distance of the farthest pair of data objects belonging to
    different clusters.

    Avg: Distance between two clusters is represented by the
    average distance of all pairs of data objects belonging to
    different clusters
    """
    dist_list = [dist[i, j] for i in clusters[a] for j in clusters[b]]

    if method == "min":
        res_dist = min(dist_list)
    if method == "max":
        res_dist = max(dist_list)
    if method == "avg":
        res_dist = np.mean(dist_list)
    return res_dist


def hierarchial_clustering(data, dist, method="max", num_clusters=5):
    """
    This function runs hierarchial clustering on given data using given method.

    Parameters
    ----------
    data : np.array
        contains our dataset in numpy array
    dist : np.array
        distance matrix containing euclidean distance between one point
        with all other points [NxN]
    method : str
        Method used for hierarchial clustering ['max', 'min', 'avg']
    num_clusters : int
        Number of clusters

    Returns
    -------
    total_clusters : list
        containing a list of clusters at each hierarchy
    cluster_label : np.array
        Cluster labels
    """

    # Initialise cluster list
    clusters = []
    for i in range(len(data)):
        clusters = clusters + [[i]]

    total_clusters = []
    # Merging clusters based on minimum of their inter cluster distances
    for k in range(data.shape[0] - 1):
        min_dist = 10000
        for i in range(len(clusters)):
            for j in range(len(clusters)):
                if i != j:
                    cur_dist = inter_cluster_dist_method(
                        data, clusters, dist, i, j, method
                    )
                    if cur_dist < min_dist:
                        i_index = i
                        j_index = j
                        min_dist = cur_dist
                        new_cluster = clusters[i_index] + clusters[j_index]

        del clusters[i_index], clusters[j_index - 1]
        clusters.append(new_cluster)
        total_clusters.append(clusters[:])

    final_cluster = total_clusters[len(total_clusters) - num_clusters]
    cluster_label = np.zeros(data.shape[0]).astype(int)
    label = 0
    for cluster in final_cluster:
        for point in cluster:
            cluster_label[point] = label
        label += 1

    return total_clusters, cluster_label


if __name__ == "__main__":
    dataset = ds.load_iris()
    X, clusters = dataset["data"], dataset["target"]
    num_clusters = 3
    X = np.array(X)
    clusters = np.array(clusters)
    print(X.shape, clusters.shape)
    dist = dist_matrix(X)

    # Max distance
    print("\nHierarchial Clustering through Maximum distance")
    max_total_clusters, max_clusters = hierarchial_clustering(
        X, dist, "max", num_clusters
    )
    MaxHclustering = AgglomerativeClustering(
        n_clusters=num_clusters, affinity="euclidean", linkage="complete"
    ).fit(X)
    print(
        "Homogeneity Score between grouth truth and our Max HC implementation: ",
        homogeneity_score(max_clusters, clusters),
    )
    print(
        "Homogeneity Score between grouth truth and Max HC library: ",
        homogeneity_score(MaxHclustering.labels_, clusters),
    )
    print(
        "Homogeneity Score between Max HC library and our Max HC implementation: ",
        homogeneity_score(max_clusters, MaxHclustering.labels_),
    )

    print(
        "Jaccard Score of grouth truth and our Max HC implementation: ",
        jaccard_score(clusters, max_clusters, average="weighted"),
    )
    print(
        "Jaccard Score of grouth truth and Max HC library: ",
        jaccard_score(clusters, MaxHclustering.labels_, average="weighted"),
    )
    print(
        "Jaccard Score of Max HC library and our Max HC implementation: ",
        jaccard_score(MaxHclustering.labels_, max_clusters, average="weighted"),
    )

    print(
        "Rand Score of grouth truth and our Max HC implementation: ",
        adjusted_rand_score(clusters, max_clusters),
    )
    print(
        "Rand Score of grouth truth and Max HC library: ",
        adjusted_rand_score(clusters, MaxHclustering.labels_),
    )
    print(
        "Rand Score of Max HC library and our Max HC implementation: ",
        adjusted_rand_score(MaxHclustering.labels_, max_clusters),
    )

    # Min distance
    print("\nHierarchial Clustering through Minimum distance")
    min_total_clusters, min_clusters = hierarchial_clustering(
        X, dist, "min", num_clusters
    )
    MinHclustering = AgglomerativeClustering(
        n_clusters=num_clusters, affinity="euclidean", linkage="single"
    ).fit(X)

    print(
        "Homogeneity Score between grouth truth and our Min HC implementation: ",
        homogeneity_score(min_clusters, clusters),
    )
    print(
        "Homogeneity Score between grouth truth and Min HC library: ",
        homogeneity_score(MinHclustering.labels_, clusters),
    )
    print(
        "Homogeneity Score between Min HC library and our Min HC implementation: ",
        homogeneity_score(min_clusters, MinHclustering.labels_),
    )

    print(
        "Jaccard Score of grouth truth and our Min HC implementation: ",
        jaccard_score(clusters, min_clusters, average="weighted"),
    )
    print(
        "Jaccard Score of grouth truth and Min HC library: ",
        jaccard_score(clusters, MinHclustering.labels_, average="weighted"),
    )
    print(
        "Jaccard Score of Min HC library and our Min HC implementation: ",
        jaccard_score(MinHclustering.labels_, min_clusters, average="weighted"),
    )

    print(
        "Rand Score of grouth truth and our Min HC implementation: ",
        adjusted_rand_score(clusters, min_clusters),
    )
    print(
        "Rand Score of grouth truth and Min HC library: ",
        adjusted_rand_score(clusters, MinHclustering.labels_),
    )
    print(
        "Rand Score of Min HC library and our Min HC implementation: ",
        adjusted_rand_score(MinHclustering.labels_, min_clusters),
    )
