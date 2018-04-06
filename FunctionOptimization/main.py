import numpy as np
# from solver import Solver
from population import Population

def funcao(x):
    return sum(x**2)

pop = Population(pop_size=1000, mutation_rate=0.01, func=funcao, upper_bound_vector=[10., 10., 10.], lower_bound_vector=[-10., -10., -10.])
pop.EvolvePop()
