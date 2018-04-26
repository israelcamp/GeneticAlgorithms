from numpy import array, zeros, tanh
from random import random
from bird import Bird
from neuralnet import NN

class Pacman(Bird):
    
    def __init__(self, **kwargs):
        """Initializes a object of the class Pacman."""
        super().__init__(kwargs['x'],kwargs['y'], kwargs['radius'], kwargs['height'])
        self.brain = NN(5, 20, 2, generate_weights=True)
        self.brain_inputs = zeros((1, 5))
        self.fitness = 0
        self.lost = False

    def decides_jump(self, inputs):
        """Given some inputs decides if the pacman should jump."""
        self.brain_inputs[0,:] = array(inputs + [self.y / self.height, tanh(self.velocity)], dtype='float32')
        y = self.brain.predict(self.brain_inputs)
        if y[0,0] >= y[0,1]:
            self.apply_force(5)

    def increase_score(self):
        """Increases the current score for the pacman."""
        self.fitness += 1

    def crossover(self, pac_woman):
        """Given a partner performs crossover returning a child."""
        child = Pacman(x=self.x, y=self.height/2., radius=self.radius, height=self.height)
        child.input_weights = NN.mix_matrix(self.brain.input_weights, pac_woman.brain.input_weights)
        child.output_weights = NN.mix_matrix(self.brain.output_weights.T, pac_woman.brain.output_weights.T).T
        return child

    def mutates(self):
        """Mutates the brain input and outputs weights."""
        if random() <= 0.02:
            self.brain.input_weights += self.brain._random_matrix(self.brain.input_size, self.brain.hidden_size, delta=.050)
            self.brain.output_weights += self.brain._random_matrix(self.brain.hidden_size, self.brain.output_size, delta=.050)
