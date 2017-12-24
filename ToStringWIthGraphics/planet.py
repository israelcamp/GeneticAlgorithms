import string
import random
from genes import DNA
class Population():
    def __init__(self, goal, size_pop = 200, mutationRate = 0.01):
        self.goal = self.strArr(goal)
        self.size_pop = size_pop
        self.goal_size = len(self.goal)
        self.mutationRate = mutationRate
    '''creates the list from the text'''
    def strArr(self, string):
        return [char for char in string]
    '''generate a random string'''
    def strGenerator(self, size, chars=string.ascii_letters+' '):
        return [random.choice(chars) for _ in range(size)]
    '''Creates an element of the population, now its DNA'''
    def make_member(self):
        value = self.strGenerator(size=self.goal_size)
        return DNA(self.goal, value, self.mutationRate)
    '''creates the population'''
    def make_population(self):
        return [self.make_member() for _ in range(self.size_pop)]
    '''picks a parent with accept and reject'''
    def pickParent(self, pop, max_fitness):
        while True:
            parent = random.choice(pop)
            prob_parent = parent.fitness()/max_fitness
            if random.random() <= prob_parent:
                return parent
    '''calcultes maximum fitness for given population'''
    def calc_max_fitness(self, pop):
        best_member = pop[0]
        for member in pop:
            if member.fitness() > best_member.fitness():
                best_member = member
        return best_member
    '''creates new population'''
    def make_new_population(self, pop, max_fitness):
        new_pop = []
        for i in range(len(pop)):
            father = self.pickParent(pop, max_fitness)
            mother = self.pickParent(pop, max_fitness)
            child = DNA(self.goal, father.value[0:self.goal_size//2]+mother.value[self.goal_size//2:], self.mutationRate)
            child.mutates()
            new_pop.append(child)
        return new_pop
    '''evolves to the next generation'''
    def one_step_evolve(self, pop):
        best_member = self.calc_max_fitness(pop)
        n_pop = self.make_new_population(pop, best_member.fitness())
        return n_pop, best_member