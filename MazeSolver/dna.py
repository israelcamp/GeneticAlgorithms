class DNA():
    @staticmethod
    def calcFitness(path, idx, maze_grid, N):
        # return (path[idx].x - maze_grid[-1].x) ** 2 + (path[idx].y - maze_grid[-1].y) ** 2
        d = (path[idx].x + path[idx].y)/(maze_grid[-1].x + maze_grid[-1].y)
        if len(path)/(N**2) != 1:
            d /= 5
        return d**2
