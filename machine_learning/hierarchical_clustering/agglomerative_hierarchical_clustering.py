# -*- coding: utf-8 -*-
"""
README, Author - Vedant Jolly(mailto:vedantjolly2001@gmail.com)

Requirements:
  - sklearn
  - numpy
  - matplotlib
  - scipy

The agglomerative clustering is the most common type of hierarchical 
clustering used to group objects in clusters based on their similarity. 
It’s also known as AGNES (Agglomerative Nesting). 
The algorithm starts by treating each object as a singleton cluster. 
Next, pairs of clusters are successively merged until all clusters have
been merged into one big cluster containing all objects. 
The result is a tree-based representation of the objects, named dendrogram.


Steps to be followed:
    Consider we have n data points.
    Step 1: Make each data point a single point cluster.
            That forms n clusters.
    Step 2: Take the 2 closest data points and make them 1 cluster.
            That forms n-1 clusters.
    Step 3: Repeat the steps untill there is only 1 cluster.
    Step 4: Plot the dendogram.
    Step 5: To find the no of clusters we have to choose a dissimilarity ratio
    Step 6: For this we have to find the longest vertical line which does
            not cut any other horizontal line.
            
For the purpose of visualization I have taken a Mall Customer Dataset.
I have added that dataset in the heirarchical clustering folder.

"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def main():
    #Using the pandas library to read the data set
    dataset = pd.read_csv("Mall_Customers.csv")
    
    #Selecting only the required Columns 
    X = dataset.iloc[:,[3,4]].values
    
    # Using the dendrogram to find the optimal number of clusters
    """"
    Here we are using the scipy library to plot our dendrogram
    Like other clustering methods, Ward’s method starts with n clusters, 
    each containing a single object. These n clusters are combined to make
    one cluster containing all objects. At each step, the process makes
    a newcluster that minimizes variance, measured by an index called E (also called the sum of squares index).
    
    At each step, the following calculations are made to find E:

        1.Find the mean of each cluster.
        2.Calculate the distance between each object in a particular cluster, and that cluster’s mean.
        3.Square the differences from Step 2.
        4.Sum (add up) the squared values from Step 3.
        5.Add up all the sums of squares from Step 4.
    
    """
    import scipy.cluster.hierarchy as sch
    dendrogram = sch.dendrogram(sch.linkage(X, method = 'ward'))
    plt.title('Dendrogram')
    plt.xlabel('Customers')
    plt.ylabel('Euclidean distances')
    plt.show()
    
    
    # Training the Hierarchical Clustering model on the dataset
    """
    Here we are considering euclidian distance for combining clusters and 
    linkage method is ward's minimum variance method.
    We have found out the no of clusters by analyzing the dendrogram plot.
    
    """
    from sklearn.cluster import AgglomerativeClustering
    hc = AgglomerativeClustering(n_clusters = 5, affinity = 'euclidean', linkage = 'ward')
    y_hc = hc.fit_predict(X)
    
    # Visualising the clusters
    """
    Using scatter plot to classify customers into different category
    
    """
    plt.scatter(X[y_hc == 0, 0], X[y_hc == 0, 1], s = 100, c = 'red', label = 'Cluster 1')
    plt.scatter(X[y_hc == 1, 0], X[y_hc == 1, 1], s = 100, c = 'blue', label = 'Cluster 2')
    plt.scatter(X[y_hc == 2, 0], X[y_hc == 2, 1], s = 100, c = 'green', label = 'Cluster 3')
    plt.scatter(X[y_hc == 3, 0], X[y_hc == 3, 1], s = 100, c = 'cyan', label = 'Cluster 4')
    plt.scatter(X[y_hc == 4, 0], X[y_hc == 4, 1], s = 100, c = 'magenta', label = 'Cluster 5')
    plt.title('Clusters of customers')
    plt.xlabel('Annual Income (k$)')
    plt.ylabel('Spending Score (1-100)')
    plt.legend()
    plt.show()


if __name__ == "__main__":
    main()


