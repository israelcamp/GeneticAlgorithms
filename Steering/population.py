
from survivor import Survivor

class Population():
    def __init__(self, maxpop = 20):
        self.maxpop = maxpop
    def makePopulation(self):
        self.pop = [Survivor() for _ in range(self.maxpop)]
        # return [Survivor() for _ in range(self.maxpop)]
    def popSeek(self, dinner):
        for surv in self.pop:
            surv.hunting(dinner)
    def show(self):
        for surv in self.pop:
            surv.show()
    def popUpdate(self):
        for surv in self.pop:
            surv.update()
            if surv.health < 0:
                self.pop.remove(surv)