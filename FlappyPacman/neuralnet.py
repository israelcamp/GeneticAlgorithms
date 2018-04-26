import numpy as np
from random import uniform, random
import copy

class NN():

    
    def __init__(self, input_size, hidden_size, output_size=1, generate_weights=True):
        """Class for neural network of one hidden layer. Missing some methods."""
        self.input_size, self.hidden_size, self.output_size = input_size, hidden_size, output_size
        if generate_weights:
            self.input_weights = self._random_matrix(self.input_size, self.hidden_size)
            self.output_weights = self._random_matrix(self.hidden_size, self.output_size)
            
    def _random_matrix(self, m, n, delta=1):
        """Generates random matrix of size m x n with random numbers."""    
        return 2*delta*np.random.rand(m,n) - delta

    def activation_function(self, x):
        """Applies activation function to given number or matrix."""
        return np.tanh(x)
    
    def predict(self, Inputs):
        """Given matrix of inputs predicts the outputs. Returns matrix."""
        IH = np.dot(Inputs, self.input_weights)
        IH = self.activation_function(IH)
        return np.dot(IH, self.output_weights)

    def to_binary(self, Y):
        """Transforms vector to binary using threshold 0.5."""
        if np.shape(Y)[1] > 1:
            L = np.argmax(Y, axis=1)
        else: 
            L = np.zeros(len(Y))
            for i in range(len(Y)):
                if Y[i] >= 0.5:
                    L[i] = 1
        return L 
    def binary_acc(self, T, Y):
        """Calculates the accuracy for binary case."""
        Tl = copy.deepcopy(T)
        if np.shape(T)[1] > 1:
            Tl = np.argmax(T, axis=1)
        ac = 0.0
        for i in range(len(T)):
            if Tl[i] == Y[i]:
                ac += 1.0
        return ac/len(Tl)

    @staticmethod
    def mix_matrix(A, B):
        """Given two matrices mix them, return a concatenation of half the columns."""
        n = int(len(A)/2)
        return np.hstack((A[:,0:n+1], B[:,n+1:]))
