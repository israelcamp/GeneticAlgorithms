import string
import random
class DNA():
    '''initiates the object'''
    def __init__(self, goal, value, mutationRate):
        self.value = value 
        self.goal = goal
        self.mutationRate = mutationRate
    '''calculates fitness'''
    def fitness(self):
        fit = 0
        for i in range(len(self.goal)):
            if self.value[i] == self.goal[i]:
                fit += 1
        return (fit/(len(self.goal)))**2
    '''mutates'''
    def mutates(self):            
        for i in range(len(self.value)):
            if random.randint(1, 100) <= self.mutationRate*100:
                self.value[i] = self.mutatesChar()
    '''return random char'''
    def mutatesChar(self, chars=string.ascii_letters+' '):
        return random.choice(chars)