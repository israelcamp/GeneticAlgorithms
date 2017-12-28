from miner import Miner
from numpy import exp
from random import choice, random
from dna import DNA
class Population():
    def __init__(self, maze, maxpop = 10, mutationRate=0.01):
        self.maxpop, self.mutationRate = maxpop, mutationRate
        #receives the finished maze
        self.maze = maze
    '''creates a population of miners'''
    def createPopulation(self):
        self.miners_pop = [Miner(i, self.maze.size, self.maze.grid) for i in range(self.maxpop)]
    '''shows the population'''
    def show(self):
        for miner in self.miners_pop:
            miner.show()
    '''return sums of exp'''
    def softmax(self):
        return sum([exp(miner.fitness()) for miner in self.miners_pop])
    '''picks a parent'''
    def pickParent(self, pop, soft_max):
        while True:
            parent = choice(pop)
            if exp(parent.fitness())/soft_max >= random():
                return parent 
    '''makes new population'''
    def newPopulation(self, miners_pop):
        new_pop = []
        soft_max = self.softmax()
        for i in range(self.maxpop):
            father = self.pickParent(miners_pop, soft_max)
            mother = self.pickParent(miners_pop, soft_max)
            if father.fitness() >= 1:
                child = Miner(father.id_number,father.size, father.maze_grid, father.path)
            elif mother.fitness() >= 1:
                child = Miner(mother.id_number,mother.size, mother.maze_grid, mother.path)
            else:
                child = Miner.crossover(father, mother)
            new_pop.append(child)
        return new_pop
    '''moves the miners'''
    def run(self):
        count_lost = 0
        for miner in self.miners_pop:
            miner.mutate(self.mutationRate)
            miner.move()
            if miner.lost:
                count_lost += 1
        if count_lost == self.maxpop:
            self.miners_pop = self.newPopulation(self.miners_pop)
    
