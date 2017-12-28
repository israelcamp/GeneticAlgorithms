import pyglet
from maze import Maze
from population import Population

width, height, size = 600, 600, 50
rows, cols = width//size, height//size
window = pyglet.window.Window(height=height+1, width=width+1)

maze = Maze(rows, cols, size)
maze.beginMaze()

pop = Population(maze, maxpop=10)
pop.createPopulation()

def updates(dt):
    if not maze.finished:
        maze.updates_grid()
    else:
        pop.run()
@window.event
def on_draw():
    window.clear()
    maze.show()
    pop.show()
pyglet.clock.schedule_interval(updates, 0.05)
pyglet.app.run()

print('Finish')