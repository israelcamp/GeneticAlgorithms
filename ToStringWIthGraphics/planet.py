import string
import random
from rStr import strArr, strGenerator
from genes import DNA
class Population():
    def __init__(self, goal, size_pop = 200, mutationRate = 0.01):
        self.goal = strArr(goal)
        self.size_pop = size_pop
        self.goal_size = len(self.goal)
        self.mutationRate = mutationRate

    def make_member(self):
        '''Creates an element of the population, now its DNA'''
        value = strGenerator(size=self.goal_size)
        return DNA(self.goal, value, self.mutationRate)
    
    def make_population(self):
        '''Creates the population'''
        return [self.make_member() for _ in range(self.size_pop)]
    
    def pickParent(self, pop, max_fitness):
        '''Picks a parent with accept and reject'''
        while True:
            parent = random.choice(pop)
            prob_parent = parent.fitness()/max_fitness
            if random.random() <= prob_parent:
                return parent
    
    def calc_max_fitness(self, pop):
        '''Calcultes maximum fitness for given population'''
        best_member = pop[0]
        for member in pop:
            if member.fitness() > best_member.fitness():
                best_member = member
        return best_member
    
    def make_new_population(self, pop, max_fitness):
        '''Creates new population'''
        new_pop = []
        for i in range(len(pop)):
            father = self.pickParent(pop, max_fitness)
            mother = self.pickParent(pop, max_fitness)
            child = DNA(self.goal, father.value[0:self.goal_size//2]+mother.value[self.goal_size//2:], self.mutationRate)
            child.mutates()
            new_pop.append(child)
        return new_pop
    
    def one_step_evolve(self, pop):
        '''Evolves to the next generation'''
        best_member = self.calc_max_fitness(pop)
        n_pop = self.make_new_population(pop, best_member.fitness())
        return n_pop, best_member