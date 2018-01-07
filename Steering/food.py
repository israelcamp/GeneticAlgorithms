import numpy as np
from numpy.random import randint 
import shapes

class Food():
    def __init__(self, goodness):
        self.pos = np.array([randint(0, 1000), randint(0, 600)])
        self.size = 6
        self.goodness = goodness
    def show(self):
        if self.goodness == 1:
            shapes.circle(self.pos[0], self.pos[1], self.size, color=(100, 200, 0))
        else:
            shapes.circle(self.pos[0], self.pos[1], self.size, color=(200, 100, 0))