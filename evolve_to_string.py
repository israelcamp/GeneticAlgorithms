import random
import string

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
        return fit/(len(self.goal))
    '''mutates'''
    def mutates(self):            
        for i in range(len(self.value)):
            if random.randint(1, 100) <= self.mutationRate*100:
                self.value[i] = self.mutatesChar()
    '''return random char'''
    def mutatesChar(self, chars=string.ascii_letters+' '):
        return random.choice(chars)

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
    def evolve(self):
        count = 0
        pop = self.make_population()
        best_member = self.calc_max_fitness(pop)
        while best_member.fitness() < 1:
            count += 1
            pop = self.make_new_population(pop, best_member.fitness())
            best_member = self.calc_max_fitness(pop)
            print('Generation {}: {}'.format(count, ''.join(best_member.value)))
        return best_member

goal = 'Natalia Goska'
planet = Population(goal, 200, 0.01)
best = planet.evolve()
