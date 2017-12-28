import shapes
from random import choice, seed, random
from time import time
from dna import DNA
class Miner():
    def __init__(self, id_number, size, maze_grid, path=None):
        self.id_number = id_number
        self.size = size
        self.maze_grid = maze_grid
        if path is None:
            self.path = [self.maze_grid[0]]
        else:
            self.path = path
        self.path_idx = 0
        self.N = self.maze_grid[0].N
        self.lost = False
        # self.current_cell = self.path[self.current_idx]
    '''shows the miner'''
    def show(self):
        shapes.circle(self.path[self.path_idx].x+self.size/2,
                    self.path[self.path_idx].y+self.size/2, self.size/3)
        shapes.text(str(self.id_number), self.path[self.path_idx].x+self.size/2,
                    self.path[self.path_idx].y+self.size/2, self.size/3)
    '''calculates fitness'''
    def fitness(self):
        return DNA.calcFitness(self.path, self.path_idx, self.maze_grid, self.N)
    '''move the miner'''
    def move(self):
        if not self.lost and self.fitness() < 1:
            if self.path_idx + 1 < len(self.path):
                self.path_idx += 1
            else:
                has = self.findNewPath(self.path_idx)
                if not has:
                    self.lost = True
                else:
                    self.path_idx += 1
        #only to stop it from walking moreif len(path)/(N**2) != 1:
        #     d /= 5 but create new population
        elif self.fitness() >= 1 and not self.lost:
            self.lost = True
    '''checks if the neighbor is available'''
    def checkNeighbor(self, current_idx):
        place = self.path[self.path_idx].index
        n_rows = self.path[self.path_idx].row
        neighbors = []
        #check top neighbor
        if place + self.N < len(self.maze_grid) and not self.maze_grid[place + self.N].walls['bottom']:
            if self.maze_grid[place + self.N] not in self.path:
                neighbors.append(self.maze_grid[place + self.N])
        #checks bottom neighbor
        if place - self.N > 0 and not self.maze_grid[place - self.N].walls['top']:
            if self.maze_grid[place - self.N] not in self.path:
                neighbors.append(self.maze_grid[place - self.N])
        #check right neighbor
        if place + 1 < self.N*(n_rows + 1) and not self.maze_grid[place + 1].walls['left']:
            if self.maze_grid[place + 1] not in self.path:
                neighbors.append(self.maze_grid[place + 1])
        #checks left neighbor
        if place > self.N*n_rows and not self.maze_grid[place - 1].walls['right']:
            if self.maze_grid[place - 1] not in self.path:
                neighbors.append(self.maze_grid[place - 1])
        return neighbors
    '''finds the next cell'''        
    def findNewPath(self, path_idx):
        ng = self.checkNeighbor(path_idx)
        seed(time() + self.id_number)
        if len(ng) > 0:
            self.path.append(choice(ng))
            return True
        else: 
            return False
    def mutate(self, mutationRate):
        if random() <= mutationRate and self.fitness() < 1:
            self.path = self.path[0:self.path_idx+1]
    @staticmethod
    def crossover(father, mother):
        bpath = []
        if len(father.path) > len(mother.path):
            n = len(mother.path)
        else:
            n = len(father.path)
        i = 0
        while (father.path[i].index is mother.path[i].index) and i < n - 1:
            bpath.append(father.path[i])
            i += 1
        return Miner(father.id_number, father.size, father.maze_grid, bpath)
