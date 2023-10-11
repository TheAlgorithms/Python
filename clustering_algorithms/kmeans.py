# Algorithm to implement k means clustering
import numpy as np
import matplotlib.pyplot as plt

# data points
data = np.array([[2.0, 3.0],
                 [2.5, 5.0],
                 [1.5, 2.5],
                 [4.0, 6.0],
                 [3.5, 4.5],
                 [1.0, 1.0],
                 [1.2, 1.0],
                 [1.5, 1.0],
                 [1.0, 1.5],
                 [2.1, 3.0],
                 [5.0, 7.0],
                 [3.5, 5.0],
                 [4.5, 5.0],
                 [3.5, 4.5],
                 [4.5, 5.0],
                 [5.6, 7.0],
                 [3.0, 5.5],
                 [4.2, 1.0],
                 [4.0, 2.0],])

# plotting the data
plt.scatter(data[:, 0], data[:, 1])

# number of clusters
k = 3

# randomly choosing the centroids
centroids = np.array([[1.0, 1.0],
                      [2.0, 3.0],
                      [5.0, 7.0]])

# plotting the centroids
plt.scatter(centroids[:, 0], centroids[:, 1], c='r')

# calculating the distance between each data point and the centroids and assigning the data point to the closest centroid


def assign_cluster(data, centroids):
    cluster = []
    # looping through each data point
    for i in range(len(data)):
        distances = []
        # looping through each centroid
        for j in range(len(centroids)):
            # calculating the distance between the data point and the centroid
            distances.append(np.linalg.norm(data[i] - centroids[j]))
        # assigning the data point to the closest centroid
        cluster.append(np.argmin(distances))
    print(cluster)
    return cluster

# updating the centroids


def update_centroids(data, cluster, k):
    centroids = []
    # looping through each cluster
    for i in range(k):
        # calculating the new centroid
        centroids.append(np.mean(data[np.array(cluster) == i], axis=0))
    return np.array(centroids)

# plotting the data points and the centroids


def plot(data, centroids, cluster):
    plt.scatter(data[:, 0], data[:, 1], c=cluster)
    plt.scatter(centroids[:, 0], centroids[:, 1], c='r')
    plt.show()


# running the algorithm for 10 iterations
for i in range(10):
    cluster = assign_cluster(data, centroids)
    centroids = update_centroids(data, cluster, k)
plot(data, centroids, cluster)

# final clusters
print(cluster)
