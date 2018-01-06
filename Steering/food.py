import numpy as np
import shapes

class Food():
    def __init__(self, goodness=1):
        self.pos = np.random.randint(low=0, high=600, size=2).astype('float32')
        self.size = 10
        self.goodness = goodness
    def show(self):
        if self.goodness == 1:
            shapes.circle(self.pos[0], self.pos[1], self.size, color=(100, 200, 0))
        else:
            shapes.circle(self.pos[0], self.pos[1], self.size, color=(200, 100, 0))