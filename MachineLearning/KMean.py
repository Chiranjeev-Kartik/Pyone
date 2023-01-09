import random
import numpy as np
import matplotlib.pyplot as plt

"""
Author: Kartikay Chiranjeev Gupta
Last Date of Modification: 2/7/2021
"""


class KMeans:
    """
    This KMeans class has two methods:

    __init__(self, k, max_iter=100): This method is called when you create an instance of the class. It initializes the
    number of clusters (k) and the maximum number of iterations (max_iter).

    fit(self, X): Given a list of input features X, this method performs the K-Means clustering algorithm to
    partition the data into k clusters. It initializes k centroids randomly, and then iteratively assigns each point
    to the closest centroid and updates the centroids to the mean of their clusters.
    """
    def __init__(self, k, max_iter=100):
        self.centroids = None
        self.k = k
        self.max_iter = max_iter

    def fit(self, x):
        # Initialize k centroids randomly
        self.centroids = [x[i] for i in random.sample(range(len(x)), self.k)]

        for _ in range(self.max_iter):
            # Assign each point to the closest centroid
            clusters = [[] for _ in range(self.k)]
            for e in x:
                distances = [np.linalg.norm(e - centroid) for centroid in self.centroids]
                cluster_index = np.argmin(distances)
                clusters[cluster_index].append(e)

            # Update the centroids to the mean of their clusters
            for i, cluster in enumerate(clusters):
                self.centroids[i] = np.mean(cluster, axis=0)


if __name__ == '__main__':

    # Create a test dataset
    X = np.array([[0, 0], [0.5, 0.5], [0.5, 0], [0, 1], [3, 3], [2.5, 2.5], [2.5, 3]])

    # Create an instance of the KMeans classifier
    kmeans = KMeans(k=2)

    # Fit the classifier with the test dataset
    kmeans.fit(X)

    # Visualize the results
    for d in X:
        plt.scatter(d[0], d[1], color='g')
    for _centroid in kmeans.centroids:
        plt.scatter(_centroid[0], _centroid[1], color='k', marker='x')

    plt.show()
