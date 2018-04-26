from random import choice

def make_new_gen(pop):
    """Given a population returns a new population."""
    mating_pool = make_mating_pool(pop)
    new_pop = []
    for _ in range(len(pop)):
        father = choice(pop)
        mother = choice(pop)
        child = father.crossover(mother)
        child.mutates()
        new_pop.append(child)
    return new_pop

def make_mating_pool(pop):
    """Given the population returns a mating pool created using tournament selection."""
    mating_pool = []
    # total_fitness = calc_total_fitness(pop)
    for member in pop:
        mating_pool.append(tournament_selection(member, pop, 5))
    return mating_pool

def calc_total_fitness(pop):
    """Calculates total fitness of given population."""
    return sum([member.fitness for member in pop])   

def tournament_selection(member, pop, n):
    """Performs tournament selection."""
    winner = member
    i = 0
    while i < n:
        other = choice(pop)
        if other.fitness > winner.fitness:
            winner = other
        i += 1
    return winner
                