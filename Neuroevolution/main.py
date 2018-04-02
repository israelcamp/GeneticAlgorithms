import numpy as np 
import data_samples as dt 
from population import Population

X, X_teste, T, T_teste = dt.data_ripley()
input_size = np.shape(X)[1]
hidden_size = 30

p = Population(maxpop=20, hidden_size=20, Xput=X, Target=T)
p.EvolveWorld()

_, best_nn = p.MaxFitness(X, T, p.pop, best=True)

print("TestingAcc: {}".format(best_nn.Fitness(X_teste, T_teste)))