"""
Author: Kartikay Chiranjeev Gupta
Last Date of Modification: 2/7/2021
"""


class Perceptron:
    """
    This perceptron class has three methods:

    __init__(self, num_inputs): This method is called when you create an instance of the class. It initializes the
    weights and bias with zero. The num_inputs argument specifies the number of inputs the perceptron will accept.

    fit(self, inputs, label): Given a list of inputs and a label (either 0 or 1), this method updates the weights and
    bias to reduce the error between the prediction and the label.

    predict(self, inputs): Given a list of inputs, this method returns a binary prediction (either 0 or 1). It does this
    by calculating the dot product of the weights and inputs, adding the bias, and applying a step function.
    """
    def __init__(self, num_inputs):
        self.weights = [0.0 for _ in range(num_inputs)]
        self.bias = 0.0

    def fit(self, inputs, label):
        prediction = self.predict(inputs)
        error = label - prediction
        self.bias += error
        for i, weight in enumerate(self.weights):
            self.weights[i] += error * inputs[i]

    def predict(self, inputs):
        activation = self.bias
        for i, weight in enumerate(self.weights):
            activation += weight * inputs[i]
        return 1.0 if activation > 0.0 else 0.0


"""
Test the perceptron:
This code creates a perceptron with 2 inputs, trains it on the XOR function using the input-label pairs [[0, 0], 
[0, 1], [1, 0], [1, 1]] and [0, 0, 0, 1], and then makes predictions on the same input. It prints the predictions.
"""
if __name__ == '__main__':
    perceptron = Perceptron(2)
    _inputs = [[0, 0], [0, 1], [1, 0], [1, 1]]
    _labels = [0, 0, 0, 1]

    for epoch in range(10):
        for e in range(4):
            perceptron.fit(_inputs[e], _labels[e])

    predictions = [perceptron.predict(x) for x in _inputs]
    print(predictions)
