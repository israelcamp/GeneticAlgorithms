import numpy as np
from random import uniform, random
import copy

class NN():
    def __init__(self, input_size, hidden_size, output_size=1, generate_weights=True):
        self.input_size, self.hidden_size, self.output_size = input_size+1, hidden_size, output_size
        if generate_weights is True:
            self.input_weights = self.RandomMatrix(self.input_size, self.hidden_size)
            self.output_weights = self.RandomMatrix(self.hidden_size, self.output_size)
    #generates random matrix of size m x n with random numbers    
    def RandomMatrix(self, m, n, delta=2):
        A = np.zeros((m,n))
        for i in range(m):
            for j in range(n):
                # A[i][j] = uniform(-delta, delta)
                A[i][j] = 2*delta*random() - delta
                # A[i][j] = 1
        return A
    #applies activation function to given number or matrix
    def ActivationFunction(self, x):
        return np.tanh(x)
    #uses the network
    def AppliesNN(self, Inputs):
        # OH = np.hstack((Inputs, np.ones((len(Inputs), 1))))
        IH = np.dot(np.hstack((Inputs, np.ones((len(Inputs), 1)))), self.input_weights)
        IH = self.ActivationFunction(IH)
        HO = np.dot(IH, self.output_weights)
        return HO
    #transforms vector to binary using threshold 0.5
    def ToBinary(self, Y):
        assert np.size(Y, axis=1) == 1, 'ToBinary dim size' 
        L = np.zeros(len(Y))
        for i in range(len(Y)):
            if Y[i] >= 0.5:
                L[i] = 1
        return L 
    #calculates the accuracy for binary case
    def BinaryAcc(self, T, Y):
        assert len(T) == len(Y), 'BinaryAcc dim size'
        ac = 0.0
        for i in range(len(T)):
            if T[i] == Y[i]:
                ac += 1.0
        return ac/len(T)
    '''DNA STUFF'''
    #calculate fitness
    def Fitness(self, X, T):
        HO = self.AppliesNN(X)
        Y = self.ToBinary(HO)
        acc = self.BinaryAcc(T, Y)
        return acc
    #mutates matrices
    def Mutates(self):
        if random() <= 0.1:
            self.input_weights += self.RandomMatrix(self.input_size, self.hidden_size, delta=.050)
            self.output_weights += self.RandomMatrix(self.hidden_size, self.output_size, delta=.050)

    @staticmethod
    def MixMatrix(A, B):
        n = int(len(A)/2)
        return np.hstack((A[:,0:n+1], B[:,n+1:]))
    @staticmethod
    def CrossOver(father, mother):
        child = NN(input_size=father.input_size-1, hidden_size=father.hidden_size, generate_weights=False)
        child.input_weights = NN.MixMatrix(father.input_weights, mother.input_weights)
        child.output_weights = NN.MixMatrix(father.output_weights.T, mother.output_weights.T).T
        return child