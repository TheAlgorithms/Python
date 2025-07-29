from random import shuffle
import tensorflow as tf
import numpy as np


def tf_k_means_clustering(vectors, noofclusters,max_iterations = 100,tolerance = 1e-4):
    """
    Performs K-means clustering using a fixed and efficient vectorized approach, using Tensorflow 2.x

    Parameters:
    vectors (list): A list of vectors.
    noofclusters (int): The number of clusters (k).
    max_iterations(int): maximum number of iterations or how many times the algorithm will refine its cluster assignments and centroid positions, until convergence.
    tolerance(int): defines a convergence criterion. The K-means algorithm stops when the centroids move less than this tolerance value between consecutive iterations.

    (set same random seed in all examples for reproducibility)
    >>>tf.random.set_seed(42)

    Example 1:
    >>>data2 = np.array([[0.0, 0.0], [0.1, 0.1], [10.0, 10.0]], dtype=np.float32)
    >>>centroids2, assignments2 = tf_k_means_clustering(data2, 2)
    >>>print(centroids2,assignments2)
    [[ 0.05  0.05]
    [10.   10.  ]] [0 0 1]

    Example 2 (Idential data points):
    >>>data_identical = np.array([[1.0, 1.0], [1.0, 1.0], [1.0, 1.0], [1.0, 1.0]], dtype=np.float32)
    >>>centroids, assignments = tf_k_means_clustering(data_identical, 1)
    >>>print(centroids,assignments)

    Example 3 (k>N):
    >>>data = np.array([[0.0, 0.0], [0.9, 0.9], [13.0, 15.0]], dtype=np.float32)
    >>>centroids, assignments = tf_k_means_clustering(data, 5)
    >>>print(centroids,assignments)
    """


    vectors = tf.constant(vectors, dtype=tf.float32)
    noofclusters = int(noofclusters)
    num_data_points = tf.shape(vectors)[0]

    if noofclusters > num_data_points:
      raise ValueError("Number of clusters (k) cannot be greater than the number of data points.")

    # Initialize centroids randomly from first k(no: of clusters) elements from the shuffled data points
    initial_indices = tf.random.shuffle(tf.range(tf.shape(vectors)[0]))[:noofclusters]
    centroids = tf.Variable(tf.gather(vectors, initial_indices))

    @tf.function
    def train_step():
        # Find the closest centroid for each vector
        distances_sq = tf.reduce_sum(
            tf.square(tf.expand_dims(vectors, 1) - tf.expand_dims(centroids, 0)), 2
        )
        assignments = tf.argmin(distances_sq, axis=1)

        #Recalculate centroids efficiently
        sums = tf.math.unsorted_segment_sum(vectors, assignments, num_segments=noofclusters)
        counts = tf.math.unsorted_segment_sum(tf.ones_like(vectors), assignments, num_segments=noofclusters)

        # Avoid division by zero for empty clusters
        new_centroids = sums / tf.maximum(counts, 1e-9)

        # For empty clusters, keep the old centroid to prevent them from moving to the origin
        is_empty = tf.equal(tf.reduce_sum(counts, axis=1), 0)
        new_centroids = tf.where(tf.expand_dims(is_empty, 1), centroids, new_centroids)

        return assignments, new_centroids

    # Main iteration loop
    for i in range(max_iterations):
        old_centroids = tf.identity(centroids)
        assignments, new_centroids_val = train_step()
        centroids.assign(new_centroids_val)

        # Check for convergence
        if tf.reduce_sum(tf.square(old_centroids - centroids)) < tolerance:
            break

    return centroids.numpy(), assignments.numpy()
