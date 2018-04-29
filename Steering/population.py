from random import random
from survivor import Survivor

class Population():
    '''
    Class to handle a population of survivors in the world.

    '''

    def __init__(self, maxpop = 20):
        '''Initiates a population given the size.'''
        self.maxpop = maxpop
        self.debug = True

    def makePopulation(self):
        '''Creates a list of survivors with lenght of maxpop.'''
        self.pop = [Survivor(debug=self.debug) for _ in range(self.maxpop)]

    def popSeek(self, dinner, venom, predator=None):
        '''Makes every survivor search for the food in the world.'''
        for surv in self.pop:
            surv.hunting(dinner, venom)
            surv.update()
            if random() < 0.000001*surv.score:
                self.pop.append(Survivor(surv.perception[:], surv.atraction[:], self.debug))
            if surv.health < 0:
                self.pop.remove(surv)

    def addSurvivor(self):
        '''Adds a new survivor to the population.'''
        self.pop.append(Survivor(debug=self.debug))

    def show(self):
        '''Shows all the survivors.'''
        for surv in self.pop:
            surv.show()

    def Debug(self):
        '''Changes the debug status in every survivor.'''
        self.debug = not self.debug
        for surv in self.pop:
            surv.debug = self.debug