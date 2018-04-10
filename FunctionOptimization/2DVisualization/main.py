import numpy as np
import pyglet
from pyglet.window import mouse, key
from pyglet.gl import *
from population import Population
import shapes

def funcao(x):
	return -sum(x**2)

optimal = [0, 0]

dim = 600
delta = 10
pop = Population(pop_size=1000, mutation_rate=0.01, func=funcao, upper_bound_vector=[10., 10.], lower_bound_vector=[-10., -10.0], delta=(dim/2, dim/delta))

#creates window
window = pyglet.window.Window(dim, dim, caption='GA Function Optimization', resizable=True)
pyglet.gl.glClearColor(1.0, 1.0, 1.0, 1.0)

@window.event
def on_key_press(symbol, modifiers):
    if symbol is key.W:
        pop.EvolvePop()

@window.event
def on_draw():
    glPushMatrix()
    glViewport(0, 0, window.width, window.height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0, dim, 0, dim, -1, 1)
    glMatrixMode(GL_MODELVIEW)
    #
    window.clear()
    shapes.cartesian(dim, dim, delta)
    shapes.grid(dim, dim, delta)
    pop.show()
    #prints the optimal point
    shapes.circle(x=optimal[0]*dim/delta + dim/2, y=optimal[1]*dim/delta + dim/2, radius=5, color=(255, 0, 0))
    #
    glPopMatrix()

pyglet.clock.schedule_interval(pop.FindOptimalPop, 0.1)
pyglet.app.run()