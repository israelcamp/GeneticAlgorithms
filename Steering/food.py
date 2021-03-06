import numpy as np
from numpy.random import randint 
import shapes

class Food():
    '''
    Class for the food or poison of the world.
    A goodness of 1 defines a food, -1 defines a poison

    '''
    size = 6
    def __init__(self, goodness):
        '''Initiates a food or posion to random position.'''
        self.pos = np.array([randint(0, 1000), randint(0, 600)])
        self.goodness = goodness

    def show(self):
        '''Shows the food or poison.'''
        if self.goodness == 1:
            shapes.circle(self.pos[0], self.pos[1], self.size, color=(100, 200, 0))
        else:
            shapes.circle(self.pos[0], self.pos[1], self.size, color=(200, 100, 0))