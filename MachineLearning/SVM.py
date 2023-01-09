import numpy as np

"""
Author: Kartikay Chiranjeev Gupta
Last Date of Modification: 2/7/2021
"""


class SVM:
    """
    This is an implementation of the Support Vector Machine (SVM) algorithm for binary classification.
    The __init__ method is the constructor of the class, which initializes the learning rate, lambda parameter,
    number of iterations, and the weights and bias as instance variables.
    """
    def __init__(self, learning_rate=0.001, lambda_param=0.01, n_iters=1000):
        self.lr = learning_rate
        self.lambda_param = lambda_param
        self.n_iters = n_iters
        self.w = None
        self.b = None

    def fit(self, X, y):
        """
        The fit method is used to fit the model on the training data. It receives training data X as input the and
        the corresponding labels y. It converts the labels to 1 and -1 and initializes the weights w and bias b to
        zero. It then iterates for a number of iterations (specified by the n_iters parameter) and for each
        iteration, it loops through all the training samples. For each sample x_i, it checks whether the sample is
        classified correctly by the current model. If it is classified correctly, the weights are updated by
        subtracting a fraction of the regularization term (specified by the lambda_param and learning_rate
        parameters). If it is not classified correctly, the weights are updated by subtracting a fraction of the
        regularization term and the dot product of the sample and its corresponding label. The bias is also updated
        """
        n_samples, n_features = X.shape
        y_ = np.where(y <= 0, -1, 1)
        self.w = np.zeros(n_features)
        self.b = 0
        for _ in range(self.n_iters):
            for id_x, x_i in enumerate(X):
                condition = y_[id_x] * (np.dot(x_i, self.w) - self.b) >= 1
                if condition:
                    self.w -= self.lr * (2 * self.lambda_param * self.w)
                else:
                    self.w -= self.lr * (
                            2 * self.lambda_param * self.w - np.dot(x_i, y_[id_x])
                    )
                    self.b -= self.lr * y_[id_x]

    def predict(self, data_x):
        """
        The predict method is used to predict the labels of new samples. It receives a matrix of samples data_x and
        returns the sign of the dot product of the samples and the weights minus the bias.

        """
        approx = np.dot(data_x, self.w) - self.b
        return np.sign(approx)


# Test code
if __name__ == "__main__":
    _data_x = np.array([[7.12731332, -4.4394424],
                       [6.68873898, -2.44840134],
                       [-1.1004791, -7.78436803],
                       [3.99337867, -4.90451269],
                       [-1.8171622, -9.22909875],
                       [-2.05521901, -10.23141199]])
    _y = np.array([1, 1, -1, 1, -1, -1])
    clf = SVM()
    clf.fit(_data_x, _y)
    predictions = clf.predict(_data_x)
    print(predictions)
