import numpy as np

"""
Citation:

***************************************************************************************
*    Title: Neural Network from Numpy
*    Author: Kartikay Chiranjeev Gupta
*    Date: 08/01/2023
*    Code version: 1.0.0
*    Availability: https://github.com/Chiranjeev-Kartik
***************************************************************************************
"""

np.random.seed(23)


def sigmoid(z):
    """
    Calculates the sigmoid of z.
    """
    z = np.clip(z, -500, 500)  # prevent overflow
    return 1 / (1 + np.exp(-z))


def output_func(z):
    return z


class Layer:
    def __init__(self, n_input, n_output, eta=0.1, activation_func=sigmoid):
        """
        Iniialize important parameters like weights(bias included), activation function, and learning rate (eta).
        :param n_input: Number of input nodes
        :param n_output: Number of output nodes
        :param eta: Learning rate
        :param activation_func: activation function to be applied after weighted sum.
        """
        self.weights = 2*np.random.random((n_input + 1, n_output)) - 1
        self.func = activation_func
        self.x = None
        self.activation = None
        self.eta = eta

    def forward(self, x):
        """
        Adds column of 1s (for bias) and calculates the weighted sum.
        """
        self.x = x
        self.x = np.hstack((np.ones((self.x.shape[0], 1)), self.x))
        self.activation = self.func(np.dot(self.x, self.weights))
        return self.activation

    def backward(self, error):
        """
        Update weights using the error caused by activation.
        :param error: (activation - true value)
        :return: error for previous layer.
        """
        p_error = self.x[:, 1:] * (1 - self.x[:, 1:]) * np.dot(error, self.weights.T[:, 1:])
        gradient = np.average(self.x[:, :, np.newaxis] * error[:, np.newaxis, :], axis=0)
        self.weights += -self.eta * gradient
        return p_error


class NeuralNetwork:
    def __init__(self, n_input, n_hidden, n_neurons, n_output, eta=0.1):
        self.eta = eta
        self.n_hidden = n_hidden
        self.input_layer = Layer(n_input, n_neurons, eta)
        self.output_layer = Layer(n_neurons, n_output, eta, output_func)
        self.hidden_layers = np.array([Layer(n_neurons, n_neurons, eta) for _ in range(n_hidden - 1)])

    def forward_propagation(self, x):
        activation = self.input_layer.forward(x)
        for i in range(self.n_hidden - 1):
            activation = self.hidden_layers[i].forward(activation)
        output = self.output_layer.forward(activation)
        return output

    def backward_propagation(self, y):
        error = self.output_layer.backward(self.output_layer.activation - y)
        for i in range(self.n_hidden - 1)[::-1]:
            error = self.hidden_layers[i].backward(error)
        self.input_layer.backward(error)

    def fit(self, x, y, iterations):
        for _ in range(iterations):
            self.forward_propagation(x)
            self.backward_propagation(y)

    def predict(self, x):
        return self.forward_propagation(x)

    def info(self):
        """
        Prints information like weights and activation for each layer.
        """
        print('=================Input Layer=================')
        print("Input:\n", self.input_layer.x)
        print("Weights:\n", self.input_layer.weights)
        print("Activations:\n", self.input_layer.activation)
        if not self.n_hidden == 1:
            for i in range(self.n_hidden - 1):
                print("=================Hidden layer=================: ")
                print("Input:\n", self.hidden_layers[i].x)
                print("Weights:\n", self.hidden_layers[i].weights)
                print("Activations:\n", self.hidden_layers[i].activation)
        print("=================Output Layers=================")
        print("Input:\n", self.output_layer.x)
        print("Weights:\n", self.output_layer.weights)
        print("Activations:\n", self.output_layer.activation)


# Test code
X = np.array([
    [0, 0],
    [0, 1],
    [1, 1],
    [1, 0]
])
_y = np.array([[1, 2, 6, 4]]).T
nn = NeuralNetwork(2, 5, 10, 1, eta=.1)
nn.fit(X, _y, 5000)
# nn.info()
print(nn.predict(X))
# Expected Output: [[1 2 6 4]]
