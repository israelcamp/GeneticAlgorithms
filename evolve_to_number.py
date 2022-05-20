import numpy as np 
from random import shuffle
'''
    Very basic code using genetic algorithm.
    Given goal number a population starts with random values between 0 and 1
    and evolve to the goal
    
    I could change somethings:
        - The way I put things into pool
        - I could allow negative numbers
        
    The purpose of this code is just to get an idea of how genetic algorithms work.
    Next I will try to implement on text.
'''
class Item():
    def __init__(self, goal, value):
        '''initiates the class object'''
        self.value = value
        self.goal = goal

    def calc_fitness(self):
        '''calculate the fitness'''
        #self.fitness = self.value/self.goal
        return self.value/self.goal

def make_child(goal, father, mother):
    '''Given two items from pop returns a baby'''   
    #make baby using the sum of the values from mather and father plus a minor mutation
    baby = Item(goal, father.value + mother.value + .01*np.random.rand())
    return baby

def make_new_gen(size_pop, goal, pop):
    '''Given a population returns its children'''
    #now we sum all the fitness using the exp to apply the softmax later
    exp_total_fitness = 0
    for item in pop:
        exp_total_fitness += np.exp(item.calc_fitness())
    #now we insert on a pool the sofmax of the integer values
    pool = []
    for item in pop:
        #we calculate how many times our item goes into the pool
        prob = int(np.exp(item.calc_fitness())/exp_total_fitness * 1000)
        #we insert the item prob times in the pool
        for i in range(prob):
            pool.append(item)
    #lets shuffle the list
    shuffle(pool)
    #lets take and index randonly from the list and make babys!!
    new_pop = []
    for i in range(size_pop):
        father = pool[np.random.randint(1, len(pool))]
        mother = pool[np.random.randint(1, len(pool))]
        new_pop.append(make_child(goal, father, mother))
    #lets compute the maximum fitness    
    best_item = new_pop[0]
    for item in new_pop:
        if item.calc_fitness() > best_item.calc_fitness():
            best_item = item
    return new_pop, best_item

'''Lets write the main program'''
#I want to have a population of 200 Items
size_pop = 200
#They have to reach the value of 20
goal = 20
#I want to create my pop
pop = [Item(goal, np.random.rand()) for i in range(size_pop)]
#lets create this best item only for pratical purposes
best_item = Item(goal, 0)
#lets count how many new populations we had to generate
count_gen = 0
#lets evolve our population
while best_item.calc_fitness() < 1:
    count_gen += 1
    pop, best_item = make_new_gen(size_pop, goal, pop)
    print('Generation {} has fitness of {} and value of {}'.format(count_gen,\
    best_item.calc_fitness(), best_item.value))
#print the results
print('Our population achieved a value of: {}.\n\
And fitness of: {}\nIn {} generations'.format(best_item.value,\
    best_item.calc_fitness(), count_gen))
