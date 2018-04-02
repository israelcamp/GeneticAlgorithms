## Neuroevolution

In this code I implement the [Ripley's Dataset](http://www.stats.ox.ac.uk/pub/PRNN/) to be solved using Neuroevolution,
a combination of Genetic Algorithms and Neural Networks.

The population contains 20 NNs with 20 hidden layers each. The mutation rate is 10% and I let them evolve for 800 generations.

![screenshot from 2018-04-02 08-31-46](https://user-images.githubusercontent.com/34630228/38194918-05459f40-3651-11e8-8677-7d3d4c027d22.png)

### Fitness Function
The max fitness is shown every 200 generation. Fim do Mundo ("End of the World") gives the fitness for the best member in the last
generation. The fitness is calculated as the accuracy on the training data. TestingAcc gives the accuracy of the best NN on the testing
data.

### Pool Selection

The Mating Pool is created by addind the member a proportional amount of times to its fitness value. For example, if a NN in the
population has a fitness value of 0.824, then it is added 82 times to the mating pool. The parents are chosen randomly from the mating
pool.

### Crossover

The crossover is the trickiest part. Just select input weights from one parent and output weights from the other and pass them to the
child is not good enough, as I saw in previous implementations. The solution that I came up is to pass half of these matrices.
Therefore the child's input weights comes half from the father and half from the mother, the same for the output weights.
