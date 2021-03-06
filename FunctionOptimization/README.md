## Function Optimization with Genetic Algorithm

With this algorithm we can minimize every function f: R^n -> R given an upper and lower bound for every variable in R^n.
The GA takes as input the function to be minimized, the number of members per population, the mutation rate, the upper and lower bound vectors.

### Mating Selection

The mating pool is created by tournament selection. For every member in a population another random one is selected, their fitness are evaluated (value of the function) and the one with the least value is put in the mating pool. Then, from the mating pool we select two random members to produce a child, new member for the new population.

### Example
Here I minimize f(x,y,z) = x^2 + y^2 + z^2

![screenshotfrom2018-04-0710-04-30](https://user-images.githubusercontent.com/34630228/38455323-e416b386-3a4c-11e8-96ba-abee87720d76.png)

### Update 9.04.18

Code changed so that the codes performs maximization of fitness function, staying in the commom sense for GA. The function above can still be minimized, just multiply it by minus one.
