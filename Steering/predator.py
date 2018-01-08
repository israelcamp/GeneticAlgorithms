import numpy as np
from math import pi
from pyglet.gl import *
from survivor import Survivor
import shapes, algelin
class Predator(Survivor):
    maxspeed = 6.
    def __init__(self):
        self.pos = np.random.randint(low=0, high=1000, size=2).astype('float32')
        self.vel = np.random.rand(2)*10
        self.acc = np.array([0., 0.])
        self.size = 30
        self.health = 10.
        self.perception = 150
        self.atraction = 10.
    def show(self):
        angle = algelin.heading(self.vel, add_radians=0)
        glPushMatrix()
        glTranslatef(self.pos[0], self.pos[1], 0.0)
        glRotatef(angle, 0, 0, 1)
        glTranslatef(-self.pos[0], -self.pos[1], 0.)
        shapes.pacman(self.pos[0], self.pos[1], self.size)
        shapes.ring(self.pos[0], self.pos[1], self.perception, color=(0, 0, 0))
        # shapes.line(self.pos[0], self.pos[1], 0.5*self.atraction, color=(0, 0, 0))
        glPopMatrix()
    def hunting(self, survivors):
        if len(survivors) > 0:
            target = self.findClosest(survivors, self.perception)
            if target is not None:
                self.eat(target, self.atraction, 1.0, survivors)