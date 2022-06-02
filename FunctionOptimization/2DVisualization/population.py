import numpy as np 
from random import choice
from dna import DNA

class Population():
    def __init__(self, pop_size, mutation_rate, delta, func=None, upper_bound_vector=None, lower_bound_vector=None):
        self.pop_size, self.mutation_rate = pop_size, mutation_rate
        self.func = func
        self.upper_bound, self.lower_bound = upper_bound_vector, lower_bound_vector
        self.delta = delta
        self._CreatesPop()
        self.count_gen = 0
        self.previous_max_fit = 0
        self.number_gen_btw = 0
        self.end, self.print = False, True

    #creates the population
    def _CreatesPop(self):
        self.members = [DNA(func=self.func, upper_bound_vector=self.upper_bound, lower_bound_vector=self.lower_bound, size=len(self.upper_bound), delta=self.delta)
                        for _ in range(self.pop_size)]

    #performs tournament selection with 2 parents
    def _TournamentSelection(self):
        father = choice(self.members)
        while True:
            mother = choice(self.members)
            if mother != father:
                break
        if father.Fitness() > mother.Fitness():
            return father
        return mother

    #creates mating pool
    def _MatingPool(self):
        pool = []
        for _ in range(self.pop_size):
            pool.append(self._TournamentSelection())
        return pool

    #makes new population
    def _NewPop(self):
        new_pop = []
        #creates mating pool
        pool = self._MatingPool()
        for i in range(self.pop_size):
            #select a father from pool
            father = choice(pool)
            #creates a child
            child = father.CrossOver(choice(pool))
            child.Mutation(self.mutation_rate)
            new_pop.append(child)
        return new_pop


    #calculates the maximum fitness and the best member
    def MaxFitness(self):
        #for minimizing
        max_fit = -10000000
        for solver in self.members:
            if solver.Fitness() > max_fit:
                max_fit = solver.Fitness()
                best_member = solver
        return max_fit, best_member

    def _TotalFitness(self):
        return sum([solver.Fitness() for solver in self.members])

    #checks if the population still has room to improve by some factor E
    def _Evolving(self):
        max_fit, _ = self.MaxFitness()
        E = 0.005
        soma = sum([abs(solver.Fitness() - max_fit) for solver in self.members])/self.pop_size
        return soma > E

    #check if the best value is changing for some  generations
    def _Changing(self, previous_max_fit, number_gen_btw):
        max_fit, _ = self.MaxFitness()
        if abs(max_fit - previous_max_fit) > 0.0001:
            self.previous_max_fit = max_fit
            self.number_gen_btw = 0
        else:
            self.number_gen_btw += 1
        return self.number_gen_btw

    def EvolvePop(self, *args, **kwargs):
        self.members = self._NewPop()

    def FindOptimalPop(self, dt):
        if self._Evolving() and self._Changing(self.previous_max_fit, self.number_gen_btw) < 100:
            self.EvolvePop()
            self.count_gen += 1
        else:
            self.end = True

    def show(self):
        for solver in self.members:
            solver.show(self.delta)
        max_fit, best_member = self.MaxFitness()
        if not self.end:
            best_member.best = True
            if self.number_gen_btw == 0:
                print("Function Evaluation: {} -- Point {} -- Gen {}".format(self.func(best_member.genes), best_member.genes, self.count_gen))
        if self.end and self.print:
            print("---FIM---")
            print("Function Evaluation: {} -- Point {}-- Gen {}".format(self.func(best_member.genes), best_member.genes, self.count_gen))
            self.print = False
        best_member.show(self.delta)
