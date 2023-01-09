import numpy as np
from collections import Counter
"""
Author: Kartikay Chiranjeev Gupta
"""


class KNN:
    """
    This KNN class has three methods:
    
    __init__(self, k, distance_fn=None): This method is called when you create an instance of the class. It initializes 
    the number of nearest neighbors (k).
    
    fit(self, X, y): Given a list of input features X and labels y, this method stores the data internally so,
    it can be used for prediction later.

    predict(self, x): Given a single input feature x, this method returns the predicted label by finding the k nearest
    neighbors, selecting the most common label among them, and returning that label.
    """
    def __init__(self, k=3):
        self.k = k
        self.train_X = []
        self.train_y = []
        self.n = 0
        self.N = 0

    def fit(self, x, y):
        self.train_X = x
        self.train_y = y
        self.n = len(x[0])
        self.N = len(x)

    def predict(self, X):
        result = []
        for i in X:
            result.append(self._predict(i)[0][0])
        return result

    def _predict(self, x):
        """
        Calculate Euclidean distance between all training data w.r.t one sample 'x'.
        :param x: One sample
        :return: target label with minimum distance from 'x'.
        """
        distances = []
        for i in range(0, self.N):
            distances.append(sum((x[j] - self.train_X[i][j])**2 for j in range(0, self.n)))
        y_label = np.argsort(distances)
        y_label = self.train_y[y_label[0:self.k]]
        return Counter(y_label).most_common(1)


if __name__ == '__main__':
    # Create a test dataset
    _x = np.array([[0, 0], [1, 1], [1, 0], [0, 1]])
    # f(x, y) = (2**x + 2**y)
    _y = np.array([2, 6, 4, 2])

    # Create an instance of the KNN classifier
    knn = KNN(k=3)
    # Fit the classifier with the test dataset
    knn.fit(_x, _y)
    # Make predictions on the test dataset
    predictions = knn.predict(_x)
    print(predictions)
