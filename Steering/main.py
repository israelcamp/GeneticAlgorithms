import pyglet
import numpy as np
import shapes
from survivor import Survivor
from food import Food
'''creates window and enable alpha'''
window = pyglet.window.Window(800, 600, caption='Evolutionary Steering')
pyglet.gl.glBlendFunc( pyglet.gl.GL_SRC_ALPHA, pyglet.gl.GL_ONE_MINUS_SRC_ALPHA)
pyglet.gl.glEnable(pyglet.gl.GL_BLEND)

pray = Survivor()
food = Food()

def draw(dt):
    pray.seek(food)
    pray.update()

@window.event
def on_mouse_motion(x, y, dx, dy):
    food.pos = np.array([x, y], dtype='float32')

@window.event
def on_draw():
    window.clear()
    pray.show()
    food.show()
pyglet.clock.schedule(draw)
pyglet.app.run()



