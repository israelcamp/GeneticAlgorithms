import pyglet
from spot import Cell
from maze import Maze

width, height, size = 600, 600, 50
rows, cols = width//size, height//size
window = pyglet.window.Window(height=height+1, width=width+1)
'''initiates our maze object'''
maze = Maze(rows, cols, size)
maze.beginMaze()

@window.event
def on_draw():
    window.clear()
    #cur.draw()
    maze.show()
pyglet.clock.schedule_interval(maze.updates_grid,0.1)
pyglet.app.run()
