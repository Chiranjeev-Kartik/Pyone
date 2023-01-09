import numpy as np
import random
import matplotlib.pyplot as plt
"""
Author: Kartikay Chiranjeev Gupta
"""


class LinearRegression:
    def __init__(self, learning_rate=0.01, n_iter=1000, show_graph=False):
        self.__show__graph = show_graph
        self.learning_rate = learning_rate
        self.n_iter = n_iter
        self.train_X = []
        self.train_y = []
        self.bias = 0
        self._coefficients = []
        self.n_rows = 0
        self.n_col = 0
        self.data = ()

    def fit(self, train_x, train_y):
        self.train_X = train_x
        self.train_y = train_y
        self.n_rows = len(train_x)
        self.n_col = len(train_x[0])
        self._coefficients = [round(random.random(), 3) for _ in range(self.n_col)]
        self.data = (self._coefficients, self.bias)
        temp = np.dot(train_x, self._coefficients) + self.bias
        cost = (1/(2*self.n_rows))*np.sum((temp - train_y)**2)+1
        x_axis = []
        y_axis = []
        termination_count = 0
        for _ in range(self.n_iter):
            if termination_count == 3:
                print("Premature termination at {}th iteration".format(_))
                break
            y_predicts = np.dot(train_x, self._coefficients) + self.bias
            '''
            In this line we use numpy dot product for X(shape: m x n) and y(shape: 1 x m) which return a numpy array
            of shape (1 x m) and we add bias to each and every element of that numpy array.
            '''
            difference = (y_predicts - train_y)
            avg_errs = (1/self.n_rows)*np.dot(train_x.T, difference)
            bias_err = (1/self.n_rows)*np.sum(difference)
            self._coefficients -= self.learning_rate*avg_errs
            self.bias -= self.learning_rate*bias_err
            new_cost = (1/(2*self.n_rows))*np.sum(difference**2)
            if cost > new_cost:
                cost = new_cost
                self.data = (self._coefficients, self.bias)
            elif cost == new_cost:
                termination_count += 1
            else:
                pass
            x_axis.append(_)
            y_axis.append(new_cost)
        self._coefficients, self.bias = self.data
        if self.__show__graph:
            plt.scatter(x_axis, y_axis)
            plt.show()

    def __predict__(self, test_x):
        y_predicts = np.dot(test_x, self._coefficients) + self.bias
        if self.__show__graph:
            plt.scatter(self.train_X, self.train_y)
            plt.plot(test_x, y_predicts, color="black")
            plt.show()
        return y_predicts

    def predict(self, train_x):
        return self.__predict__(train_x)


# Testing
if __name__ == '__main__':
    # Generate some synthetic data
    _x = 2 * np.random.rand(100, 1)
    _y = 4 + 3 * _x + np.random.rand(100, 1)

    # Fit the model to the data
    model = LinearRegression()
    model.fit(_x, _y)

    # Make predictions on a new set of inputs
    x_new = np.array([[0], [2]])
    y__predict = model.predict(x_new)

    # Plot the data and the model predictions
    plt.scatter(_x, _y, s=10)
    plt.plot(x_new, y__predict, 'r-', linewidth=2)
    plt.show()
