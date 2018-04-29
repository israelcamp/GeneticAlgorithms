import numpy as np
from random import random
from numpy.linalg import norm
from scipy.interpolate import interp1d
from pyglet.gl import *
from pyglet.text import Label
import shapes
import algelin

class InfPos():
    '''Auxiliar class, cause I did not find a better solution'''

    def __init__(self):
        self.pos = np.array([10000., 10000.])

class Survivor():
    '''
    Class for the survivor on my genetic algorithm example.
    They try to evolve towards eating the food and avoiding the posion on the best way possible.

    '''
    size = 15
    maxspeed = 6.
    maxforce = 0.5
    maxhealth = 20.
    xp = [20., 10., 0.]
    fp = [255., 130., 0.]
    f = interp1d(xp, fp)
    def __init__(self, perception=None, atraction=None, debug=False):
        '''
        Initiates the survivor.
        If perception and atraction are not given then a random vector is generated.

        '''
        self.pos = np.random.randint(low=0, high=1000, size=2).astype('float32')
        self.vel = np.random.rand(2)*10
        self.acc = np.array([0., 0.])
        # self.size = 15
        self.health = 10.
        self.debug = debug
        self.count = 0
        if perception is None:
            self.perception = np.random.randint(low=15, high=120, size=2)
        else:
            self.perception = perception
            if random() < 0.1:
                self.perception += np.random.randint(-10, 10, size=2)
        if atraction is None:
            self.atraction = 6 * np.random.rand(2) - 3
        else:
            self.atraction = atraction
            if random() < 0.1:
                self.atraction += 0.6 * np.random.rand(2) - 0.3
        self.label = Label(text='0', font_size=12, x=self.pos[0]+self.size, y=self.pos[1]++self.size, color=(0,0,0,255))

    @property
    def score(self):
        '''Property to keep track of how long the survivor is alive and updates the position of this information.'''
        self.count += 1
        self.label.x = self.pos[0] + self.size
        self.label.y = self.pos[1] + self.size
        return self.count

    def show(self):
        '''Shows the survivor.'''
        self.label.text = '{}'.format(self.score)
        self.label.draw()
        alpha = int(self.f(self.health))
        angle = algelin.heading(self.vel)
        glPushMatrix()
        glTranslatef(self.pos[0] + self.size/2, self.pos[1] + self.size/3, 0.0)
        glRotatef(angle, 0, 0, 1)
        glTranslatef(-self.pos[0] - self.size/2, -self.pos[1] - self.size/3, 0.)
        shapes.triangle(self.pos[0]-2, self.pos[1]-2, self.size, angle=angle, color=(0, 0, 0, alpha+30))
        if self.debug:
            shapes.ring(self.pos[0]+self.size/2, self.pos[1]+self.size/3, self.perception[0], color=(100, 255, 0, alpha))
            shapes.ring(self.pos[0]+self.size/2, self.pos[1]+self.size/3, self.perception[1], color=(255, 100, 0, alpha))
            shapes.line(self.pos[0]+self.size/3, self.pos[1]+self.size/3, self.atraction[0], color=(100, 255, 0, alpha))
            shapes.line(self.pos[0]+self.size/3, self.pos[1]+self.size/3, self.atraction[1], color=(255, 100, 0, alpha))
        glPopMatrix()

    def hunting(self, dinner, venom):
        '''Defines how it should move based on the food or poison noticed.'''
        if len(dinner) > 0:
            target_food = self.findClosest(dinner, self.perception[0])
            target_poison = self.findClosest(venom, self.perception[1])
            if target_food is not None:
                self.eat(target_food, self.atraction[0], 2.0, dinner)
            if target_poison is not None:
                self.eat(target_poison, self.atraction[1], -6.0, venom)

    def eat(self, target, target_atraction, health, elements):
        '''Eats the target if its close enough, moves towards it otherwise by seek.'''
        if norm(target.pos - self.pos) < self.maxspeed + 5.:
            self.health += health
            elements.remove(target)
            if self.health > self.maxhealth:
                self.health = self.maxhealth
        else:
            self.seek(target.pos, target_atraction)

    def findClosest(self, elements, radius):
        '''Given an list of elements and a radius of perception returns the closes member in the list.'''
        target = InfPos()
        for food in elements:
            if radius > norm(food.pos - self.pos) < norm(target.pos - self.pos):
                target = food
        if not isinstance(target, InfPos):            
            return target
    def seek(self, target_pos, target_atraction):
        '''Moves towards or away from the target depending on the atraction.'''
        desired = target_pos - self.pos
        desired = algelin.setMag(desired, self.maxspeed)
        steer = desired - self.vel
        steer = algelin.limit(steer, self.maxforce)
        self.applyFoce(steer*target_atraction)

    def applyFoce(self, force):
        '''Applies a force to the movement of the survivor.'''
        self.acc += force

    def update(self):
        '''Updates velocity, position and health.'''
        self.vel += self.acc
        self.vel = algelin.limit(self.vel, self.maxspeed)
        self.pos += self.vel
        self.acc = np.zeros(2)
        self.health -= 0.04
        self.keepInside()

    def keepInside(self):
        '''Makes a force towards the center of screen if survivor goes out.'''
        if(self.pos[0] > 1000 or self.pos[0] < 0 or self.pos[1] > 600 or self.pos[1] < 0):
            self.seek(target_pos=[500, 300], target_atraction=1)
