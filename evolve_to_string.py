import random
import string

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
                self.value[i] = self.mutatesChar()
    def mutatesChar(self, chars=string.ascii_letters+' '):
        '''return random char'''
        return random.choice(chars)

class Population():
    def __init__(self, goal, size_pop = 200, mutationRate = 0.01):
        self.goal = self.strArr(goal)
        self.size_pop = size_pop
        self.goal_size = len(self.goal)
        self.mutationRate = mutationRate
    def strArr(self, string):
        '''creates the list from the text'''
        return [char for char in string]
    def strGenerator(self, size, chars=string.ascii_letters+' '):
        '''generate a random string'''
        return [random.choice(chars) for _ in range(size)]
    def make_member(self):
        '''Creates an element of the population, now its DNA'''
        value = self.strGenerator(size=self.goal_size)
        return DNA(self.goal, value, self.mutationRate)
    def make_population(self):
        '''creates the population'''
        return [self.make_member() for _ in range(self.size_pop)]
    def pickParent(self, pop, max_fitness):
        '''picks a parent with accept and reject'''
        while True:
            parent = random.choice(pop)
            prob_parent = parent.fitness()/max_fitness
            if random.random() <= prob_parent:
                return parent
    def calc_max_fitness(self, pop):
        '''calcultes maximum fitness for given population'''
        best_member = pop[0]
        for member in pop:
            if member.fitness() > best_member.fitness():
                best_member = member
        return best_member
    def make_new_population(self, pop, max_fitness):
        '''creates new population'''
        new_pop = []
        for i in range(len(pop)):
            father = self.pickParent(pop, max_fitness)
            mother = self.pickParent(pop, max_fitness)
            child = DNA(self.goal, father.value[0:self.goal_size//2]+mother.value[self.goal_size//2:], self.mutationRate)
            child.mutates()
            new_pop.append(child)
        return new_pop
    def evolve(self):
        '''evolve the populations towards the goal'''
        count = 0
        pop = self.make_population()
        best_member = self.calc_max_fitness(pop)
        while best_member.fitness() < 1:
            count += 1
            pop = self.make_new_population(pop, best_member.fitness())
            best_member = self.calc_max_fitness(pop)
            print('Generation {}: {}'.format(count, ''.join(best_member.value)))
        return best_member

goal = 'Estamos aprendendo AG'
planet = Population(goal, 200, 0.01)
best = planet.evolve()
