import numpy as np
import shapes

class Food():
    def __init__(self):
        self.pos = np.array([400., 300.])
        self.size = 20
    def show(self):
        shapes.circle(self.pos[0], self.pos[1], self.size)