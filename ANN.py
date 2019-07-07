from numpy import *

class ANN(object):
    def __init__(self):

        random.seed(1)
        self.weight = 2 * random.random((3, 1)) - 1

    def sigmoid(self, x):
        return 1 / (1 + exp(-x))

    def sigmoid_derivative(self, x):
        return x * (1 - x)

    def train(self, inputs, outputs, training_iterations):
        for iteration in range(training_iterations):


            output = self.learn(inputs)
            error = outputs - output
            factor = dot(inputs.T, error * self.sigmoid_derivative(output))
            self.weight += factor

    def learn(self, inputs):
        return self.sigmoid(dot(inputs, self.weight))

if __name__ == "__main__":


    neural_network = ANN()
    inputs = array([[0, 1, 1], [1, 0, 0], [1, 0, 1]])
    outputs = array([[1, 0, 1]]).T
    neural_network.train(inputs, outputs, 10000)
    print (neural_network.learn(array([1, 0, 1]))) 
