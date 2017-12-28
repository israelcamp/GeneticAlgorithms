# from miner import Miner
class DNA():
    @staticmethod
    def calcFitness(path, idx, maze_grid, N):
        d = (path[idx].x + path[idx].y)/(maze_grid[-1].x + maze_grid[-1].y)
        # if len(path)/(N**2) != 1:
        #     d /= 5
        return d**2
    @staticmethod
    def crossover(father, mother):
        bpath = []
        if len(father.path) > len(mother.path):
            n = len(mother.path)
        else:
            n = len(father.path)
        i = 0
        print(n)
        while (father.path[i].index is mother.path[i].index) and i < n - 1:
            bpath.append(father.path[i])
            i += 1
        return Miner(father.id_number, father.size, father.maze_grid, bpath)