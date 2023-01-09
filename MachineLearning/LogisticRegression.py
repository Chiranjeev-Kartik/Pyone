import numpy as np

"""
Author: Kartikay Chiranjeev Gupta
Last Date of Modification: 2/7/2021
"""


def _sigmoid(x):
    return 1 / (1 + np.exp(-x))


class LogisticRegression:
    """
    This class has three method:

    __init__(self, learning_rate=0.1, max_iter=1000): This method is called when you create an instance of the class.
    It initializes the learning rate (learning_rate) and the maximum number of iterations (max_iter).

    fit(self, X, y): Given a list of input features X and labels y, this method fits the logistic regression model to
    the data by minimizing the cross-entropy loss. It initializes the weights and bias to 0, and then iteratively
    updates the weights and bias to minimize the loss.

    predict(self, X): Given a list of input features X, this method returns the predicted probability of the positive
    class (class 1) for each input feature.
    """
    def __init__(self, learning_rate=0.1, max_iter=1000):
        self.bias = None
        self.weights = None
        self.n_features = None
        self.n_samples = None
        self.y = None
        self.X = None
        self.learning_rate = learning_rate
        self.max_iter = max_iter

    def fit(self, X, y):
        self.X = X
        self.y = y
        self.n_samples, self.n_features = X.shape
        self.weights = np.zeros(self.n_features)
        self.bias = 0

        for _ in range(self.max_iter):
            linear_output = np.dot(self.X, self.weights) + self.bias
            probabilities = _sigmoid(linear_output)
            gradients_w = np.dot(self.X.T, probabilities - self.y) / self.n_samples
            gradients_b = np.sum(probabilities - self.y) / self.n_samples
            self.weights -= self.learning_rate * gradients_w
            self.bias -= self.learning_rate * gradients_b

    def predict(self, X):
        linear_output = np.dot(X, self.weights) + self.bias
        probabilities = _sigmoid(linear_output)
        return probabilities


if __name__ == '__main__':

    from sklearn.linear_model import LogisticRegression
    from sklearn.metrics import accuracy_score

    # Create a test dataset
    _X = np.array([[0, 0], [1, 1], [1, 0], [0, 1]])
    _y = np.array([0, 0, 1, 1])

    # Create an instance of the scikit-learn LogisticRegression classifier and our LogisticRegression classifier
    sklearn_logreg = LogisticRegression()
    logreg = LogisticRegression()
    # Fit the classifiers with the test dataset
    sklearn_logreg.fit(_X, _y)
    logreg.fit(_X, _y)

    # Make predictions on the test dataset
    predictions_sklearn = sklearn_logreg.predict(_X)
    predictions_ours = logreg.predict(_X)

    # Calculate the accuracy of the predictions
    accuracy_sklearn = accuracy_score(_y, predictions_sklearn)
    accuracy_ours = accuracy_score(_y, predictions_ours)
    print(f'Accuracy of Sklearn Model: {accuracy_sklearn}')
    print(f'Accuracy of Pyone Model: {accuracy_ours}')
