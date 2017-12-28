import pyglet
import shapes
'''to work with 1D array'''
class Cell():
    def __init__(self, rowI, colJ, size, N):
        #saves the index at the array -- i know this is bad
        self.index = rowI*N + colJ
        self.N = N
        self.row, self.col = rowI, colJ
        #this saves the size of the square cell
        self.size = size
        #here we save the coordinates at the window
        self.y = rowI*size
        self.x = colJ*size
        #here we define initial state of the walls
        self.walls = {'top':True, 'bottom': True, 'left': True, 'right': True}
        #keeps track if this cell was visited and if it is the current cell
        self.status = {'visited': False, 'current': False, 'in_stack': False}
        self.visited, self.current, self.in_stack = False, False, False
    @staticmethod
    def changeStatus(obj, *args):
        for key in args:
            if key is not 'visited':
                obj[key] = not obj[key]
            elif key is 'visited' and obj[key] is False:
                obj[key] = not obj[key]
    '''draws the cell'''
    def draw(self):
        if self.status['current']:
            vertex_list = shapes.square_list(self.x, self.y, self.size, color=(255, 0, 0))
            vertex_list.draw(pyglet.gl.GL_POLYGON)
        elif self.status['in_stack']:
            vertex_list = shapes.square_list(self.x, self.y, self.size, color=(246, 93, 4))
            vertex_list.draw(pyglet.gl.GL_POLYGON)    
        elif self.status['visited']:
            vertex_list = shapes.square_list(self.x, self.y, self.size)
            vertex_list.draw(pyglet.gl.GL_POLYGON)
        if self.walls['top']:
            pyglet.graphics.draw(2, pyglet.gl.GL_LINES,
            ('v2i',(self.x, self.y+self.size, self.x+self.size, self.y+self.size)))
        if self.walls['bottom']:
            pyglet.graphics.draw(2, pyglet.gl.GL_LINES,
            ('v2i',(self.x, self.y, self.x+self.size, self.y)))
        #we say x+1 to see the line at the screen   
        if self.walls['left']:
            pyglet.graphics.draw(2, pyglet.gl.GL_LINES,
            ('v2i',(self.x+1, self.y, self.x+1, self.y+self.size)))   
        if self.walls['right']:
            pyglet.graphics.draw(2, pyglet.gl.GL_LINES,
            ('v2i',(self.x+self.size, self.y, self.x+self.size, self.y+self.size)))