import numpy as np
from random import random
from numpy.linalg import norm
from scipy.interpolate import interp1d
from pyglet.gl import *
import shapes
import algelin

class InfPos():
    def __init__(self):
        self.pos = np.array([10000., 10000.])
        self.goodness = 1
class Survivor():
    maxspeed = 5
    maxforce = 0.3
    xp = [10., 5., 0.]
    fp = [255., 130., 0.]
    f = interp1d(xp, fp)
    def __init__(self, perception=None, atraction=None):
        self.pos = np.random.randint(low=0, high=1000, size=2).astype('float32')
        self.vel = np.random.rand(2)*10
        self.acc = np.array([0., 0.])
        self.size = 15
        self.health = 10.
        if perception is None:
            self.perception = np.random.randint(low=15, high=120, size=2)
        else:
            self.perception = perception
            if random() < 0.01:
                self.perception += np.random.randint(-10, 10)
        if atraction is None:
            self.atraction = 6 * np.random.rand(2) - 3
        else:
            self.atraction = atraction
            if random() < 0.01:
                self.atraction += 0.6 * np.random.rand(2) - 0.3
    '''mostra o survivor'''
    def show(self):
        alpha = int(self.f(self.health))
        angle = algelin.heading(self.vel)
        glPushMatrix()
        glTranslatef(self.pos[0] + self.size/2, self.pos[1] + self.size/3, 0.0)
        glRotatef(angle, 0, 0, 1)
        glTranslatef(-self.pos[0] - self.size/2, -self.pos[1] - self.size/3, 0.)
        shapes.triangle(self.pos[0]-2, self.pos[1]-2, self.size, angle=angle, color=(0, 0, 0, alpha))
        shapes.ring(self.pos[0]+self.size/2, self.pos[1]+self.size/3, self.perception[0], color=(100, 255, 0))
        shapes.ring(self.pos[0]+self.size/2, self.pos[1]+self.size/3, self.perception[1], color=(255, 100, 0))
        shapes.line(self.pos[0]+self.size/3, self.pos[1]+self.size/3, self.atraction[0], color=(100, 255, 0))
        shapes.line(self.pos[0]+self.size/3, self.pos[1]+self.size/3, self.atraction[1], color=(255, 100, 0))
        glPopMatrix()
    '''define o alvo a ser buscado'''
    def hunting(self, dinner, venom):
        if len(dinner) > 0:
            target_food = self.findClosest(dinner, self.perception[0])
            target_poison = self.findClosest(venom, self.perception[1])
            if target_food is not None:
                self.eat(target_food, self.atraction[0], 1.0, dinner)
            if target_poison is not None:
                self.eat(target_poison, self.atraction[1], -1.5, venom)
    '''come a Food, se nao move em direcao'''
    def eat(self, target, target_atraction, health, elements):
        if norm(target.pos - self.pos) < self.maxspeed:
            self.health += health
            elements.remove(target)
            if self.health > 10.:
                self.health = 10.
        else:
            self.seek(target.pos, target_atraction)
    '''encontra Food mais proximo'''
    def findClosest(self, elements, radius):
        target = InfPos()
        for food in elements:
            if norm(food.pos - self.pos) < norm(target.pos - self.pos) and norm(food.pos - self.pos) < radius:
                target = food
        if not isinstance(target, InfPos):            
            return target
    '''move em direcao ao alvo'''
    def seek(self, target_pos, target_atraction):
        desired = target_pos - self.pos
        desired = algelin.setMag(desired, self.maxspeed)
        steer = (desired - self.vel)*target_atraction
        steer = algelin.limit(steer, self.maxforce)
        self.applyFoce(steer)
    '''aplica a forca ao survivor'''
    def applyFoce(self, force):
        self.acc += force
    '''atualiza a velocidade, posicao e saude'''
    def update(self):
        self.vel += self.acc
        self.vel = algelin.limit(self.vel, self.maxspeed)
        self.pos += self.vel
        self.acc = np.zeros(2)
        self.health -= 0.04
        self.keepInside()

    '''makes a force towards the center of screen if survivor goes out'''
    def keepInside(self):
        screen_y = 600
        screen_x = 1000
        if(self.pos[0] > screen_x or self.pos[0] < 0 or self.pos[1] > screen_y or self.pos[1] < 0):
            self.seek(target_pos=[screen_x/2, screen_y/2], target_atraction=1)
