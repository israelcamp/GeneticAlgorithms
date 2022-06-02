import string
import random
from rStr import mutatesChar
class DNA():
    def __init__(self, goal, value, mutationRate):
        '''initiates the object'''
        self.value = value 
        self.goal = goal
        self.mutationRate = mutationRate
    def fitness(self):
        '''calculates fitness'''
        fit = 0
        for i in range(len(self.goal)):
            if self.value[i] == self.goal[i]:
                fit += 1
        return (fit/(len(self.goal)))**2
    def mutates(self):            
        '''mutates'''
        for i in range(len(self.value)):
            if random.randint(1, 100) <= self.mutationRate*100:
                self.value[i] = mutatesChar()
