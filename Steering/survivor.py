import numpy as np
from numpy.linalg import norm
from scipy.interpolate import interp1d
import math
import shapes

class InfPos():
    def __init__(self):
        self.pos = np.array([10000., 10000.])
        self.goodness = 1
class Survivor():
    maxspeed = 6
    maxforce = 0.4
    xp = [10., 5., 0.]
    fp = [255., 130., 0.]
    f = interp1d(xp, fp)
    def __init__(self, dna=None):
        self.pos = np.random.randint(low=0, high=600, size=2).astype('float32')
        # self.vel = np.array([0., 0.])
        self.vel = np.random.rand(2)*10
        self.acc = np.array([0., 0.])
        self.size = 15
        self.health = 10.
        if dna is None:
            self.dna = np.random.randint(low=15, high=200, size=2)
        else:
            self.dna = dna
    def show(self):
        alpha = int(self.f(self.health))
        angle = self.heading(self.vel)
        shapes.triangle(self.pos[0]-2, self.pos[1]-2, self.size, angle=angle,
                        color=(0, 0, 0, alpha))
        shapes.ring(self.pos[0]+self.size/2, self.pos[1]+self.size/3, self.dna[0], color=(100, 255, 0))
        shapes.ring(self.pos[0]+self.size/2, self.pos[1]+self.size/3, self.dna[1], color=(255, 100, 0))
    def hunting(self, dinner):
        target = None
        if len(dinner) > 0:
            target = self.findClosest(dinner)
            if norm(target.pos - self.pos) < self.dna[0] and target.goodness == 1:
                    self.eat(target, dinner)
            elif target.goodness == -1 and norm(target.pos - self.pos) < self.dna[1]:
                    self.eat(target, dinner)
    def keepInside(self):
        screen_dim = 600
        if(self.pos[0] > screen_dim or self.pos[0] < 0 or self.pos[1] > screen_dim or self.pos[1] < 0):
            self.seek(target_pos=[screen_dim/2, screen_dim/2], target_goodness=1)
    def eat(self, target, dinner):
        if norm(target.pos - self.pos) < 5:
            self.health += target.goodness
            dinner.remove(target)
            if self.health > 10.:
                self.health = 10.
        else:
            self.seek(target.pos, target.goodness)
    def findClosest(self, dinner):
        target = InfPos()
        for food in dinner:
            if norm(food.pos - self.pos) < norm(target.pos - self.pos):
                target = food
        return target
    def seek(self, target_pos, target_goodness):
        desired = (target_pos - self.pos)*target_goodness
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
        self.health -= 0.02
        self.keepInside()

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