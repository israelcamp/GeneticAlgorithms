import numpy as np
import math
import shapes

class Survivor():
    maxspeed = 4
    maxforce = 0.1
    def __init__(self):
        self.pos = np.array([200., 200.])
        self.vel = np.array([0., 0.])
        self.acc = np.array([0., 0.])
        self.size = 30

    def show(self):
        angle = self.heading(self.vel)
        shapes.triangle(self.pos[0], self.pos[1], self.size, angle=angle)

    def seek(self, target):
        desired = target.pos - self.pos
        desired = self.setMag(desired, self.maxspeed)
        steer = desired - self.vel
        steer = self.limit(steer, self.maxforce)
        self.applyFoce(steer)
    def applyFoce(self, force):
        self.acc += force
    def update(self):
        self.vel += self.acc
        self.vel = self.limit(self.vel, self.maxspeed)
        self.pos += self.vel
        self.acc = np.zeros(2)

    def setMag(self, vector, lim):
        m = np.linalg.norm(vector)
        return lim*vector/m
    def limit(self, vector, lim):
        if(np.linalg.norm(vector) > lim):
            return self.setMag(vector, lim)
        else:
            return vector
    def heading(self, vector):
        return math.degrees(math.atan2(vector[1], vector[0]) + 3*math.pi/2)