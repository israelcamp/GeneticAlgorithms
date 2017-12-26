from spot import Cell
from random import choice
class Maze():
    def __init__(self, rows, cols, size):
        self.rows, self.cols, self.size = rows, cols, size
        self.stack = []
    '''gives the initial state to maze'''
    def beginMaze(self):
        self.grid = []
        for i in range(self.rows):
            for j in range(self.cols):
                self.grid.append(Cell(i, j, self.size))
        self.addBeginEnd()
    '''adds a beginning and a end'''
    def addBeginEnd(self):
        self.current_cell = self.grid[0]
        self.grid[0].walls['bottom'] = False
        self.grid[-1].walls['right'] = False
    '''print the maze'''
    def show(self):
        for cell in self.grid:
            cell.draw() 
    '''cheks if the neighbor was visited'''       
    def checkVisited(self, ng_index):
        if not self.grid[ng_index].status['visited']:
            return self.grid[ng_index]
        else:
            return None
    '''checks if the neighbor is available'''
    def checkNeighbor(self, current_cell, way):
        if way is 'top':
            ng_index = (current_cell.row+1)*self.rows + current_cell.col
        if way is 'bottom':
            ng_index = (current_cell.row-1)*self.rows + current_cell.col
        if way is 'left':
            ng_index = current_cell.row*self.rows + current_cell.col-1
            if ng_index < current_cell.row*self.rows:
                return None
        if way is 'right':
            ng_index = current_cell.row*self.rows + current_cell.col+1
            if ng_index >= (current_cell.row+1)*self.rows:
                return None    
        if ng_index < 0 or ng_index >= self.rows*self.cols:
            return None
        return self.checkVisited(ng_index) 
    '''finds the next cell'''        
    def find_next_cell(self, current_cell):
        neighbors = []
        for d  in ['top', 'bottom', 'left', 'right']:
            ng = self.checkNeighbor(self.current_cell, d)
            if ng != None:
                neighbors.append((ng, d))
        if len(neighbors) > 0:
            return choice(neighbors)
        else:
            return None, None
    '''removes wall between two cells'''
    def removeWalls(self, way, current_cell, next_cell):
        if way is 'top':
            current_cell.walls['top'] = False
            next_cell.walls['bottom'] = False
        if way is 'bottom':
            current_cell.walls['bottom'] = False
            next_cell.walls['top'] = False
        if way is 'left':
            current_cell.walls['left'] = False
            next_cell.walls['right'] = False
        if way is 'right':
            current_cell.walls['right'] = False
            next_cell.walls['left'] = False
    '''updates current cell'''
    def updates_grid(self, dt): 
        next_cell, way = self.find_next_cell(self.current_cell)
        if next_cell is not None:
            Cell.changeStatus(self.current_cell.status, 'visited', 'current', 'in_stack')
            self.removeWalls(way, self.current_cell, next_cell)
            self.stack.append(self.current_cell)
            self.current_cell = next_cell
            Cell.changeStatus(self.current_cell.status, 'current')
        elif next_cell is None and len(self.stack) > 0:
            Cell.changeStatus(self.current_cell.status, 'visited', 'current')
            next_cell = self.stack[-1]
            self.stack.remove(next_cell)
            self.current_cell = next_cell
            Cell.changeStatus(self.current_cell.status, 'in_stack', 'current')
        else:
            #Cell.changeStatus(self.current_cell.status, 'current')
            self.current_cell.status['current'] = False              