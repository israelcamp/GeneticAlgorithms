
from random import random
from survivor import Survivor

class Population():
    def __init__(self, maxpop = 20):
        self.maxpop = maxpop
    def makePopulation(self):
        self.pop = [Survivor() for _ in range(self.maxpop)]
    def popSeek(self, dinner, venom):
        for surv in self.pop:
            surv.hunting(dinner, venom)
    def addSurvivor(self):
        self.pop.append(Survivor())
    def show(self):
        for surv in self.pop:
            surv.show()
    def popUpdate(self):
        for surv in self.pop:
            surv.update()
            if random() < 0.001:
                self.pop.append(Survivor(surv.perception, surv.atraction))
            if surv.health < 0:
                self.pop.remove(surv)
