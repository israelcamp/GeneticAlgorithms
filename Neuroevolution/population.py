import numpy as np 
import random, copy
from neuralnet import NN as Network

class Population():
    def __init__(self, maxpop=20, input_size=2, hidden_size=10, output_size=1,
                generate_weights=True, Xput=None, Target=None):
        self.maxpop = maxpop
        self.X, self.Target = Xput, Target
        self.pop = self.CreatesPopulation(self.maxpop, input_size, hidden_size, output_size)

    def CreatesPopulation(self, maxpop, input_size, hidden_size, output_size):
        return [Network(input_size, hidden_size, output_size) for _ in range(maxpop)]
    
    def MaxFitness(self, X, T, pop, best=False):
        maxfit = 0.0
        for Net in pop:
            fitness = Net.Fitness(X, T)
            if fitness > maxfit:
                maxfit = fitness
                best_member = Net
        if best:
            return maxfit, best_member
        return maxfit

    def MakeNewPopulation(self, pop):
        new_pop = []
        pool = []
        for net in self.pop:
            entries = np.floor(100*net.Fitness(self.X, self.Target))
            for _ in range(int(entries)):
                pool.append(net)
        for _ in range(self.maxpop):
            father = random.choice(pool)
            mother = random.choice(pool)
            child = copy.deepcopy(Network.CrossOver(father, mother))
            child.Mutates()
            new_pop.append(child)
        return new_pop

    def EvolvePop(self):
        newpop = self.MakeNewPopulation(self.pop)
        if self.MaxFitness(self.X, self.Target, newpop) > self.MaxFitness(self.X, self.Target, self.pop):
            self.pop = newpop

    def EvolveWorld(self):
        i = 0
        while i <= 800:
            self.EvolvePop()
            if i % 200 == 0:
                print("Max Fitness {}".format(self.MaxFitness(self.X, self.Target, self.pop)))
            i += 1
        print("Fim do Mundo {}".format(self.MaxFitness(self.X, self.Target, self.pop)))