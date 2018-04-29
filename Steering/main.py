import pyglet
from pyglet.window import mouse, key
from pyglet.gl import *
import numpy as np
import shapes
from survivor import Survivor
from food import Food
from population import Population

'''creates window and enable alpha'''
window = pyglet.window.Window(1000, 600, caption='Evolutionary Steering', resizable=True, vsync=0)
pyglet.gl.glBlendFunc(pyglet.gl.GL_SRC_ALPHA, pyglet.gl.GL_ONE_MINUS_SRC_ALPHA)
pyglet.gl.glEnable(pyglet.gl.GL_BLEND)
pyglet.gl.glClearColor(1.0, 1.0, 1.0, 1.0)
fps_display = pyglet.clock.ClockDisplay()

dinner = [Food(1) for _ in range(30)]
venom = [Food(-1) for _ in range(10)]
p = Population(10)
p.makePopulation()
def addPoision(dt):
    if len(venom) < 30:
        venom.append(Food(-1))
def addFood(dt):
    if len(dinner) < 60:
        dinner.append(Food(1))
def draw(dt):
    p.popSeek(dinner, venom, predator=None)

@window.event
def on_key_press(symbol, modifiers):
    if symbol is key.D:
        p.Debug()

@window.event
def on_mouse_press(x, y, button, modifiers):
    if button == mouse.RIGHT:
        p.addSurvivor()
    if button == mouse.LEFT:
        for _ in range(10):
            dinner.append(Food(1))
    if button == mouse.MIDDLE:
        for _ in range(5):
            venom.append(Food(-1))

@window.event
def on_draw():
    glPushMatrix()
    glViewport(0, 0, window.width, window.height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0, 1000, 0, 600, -1, 1)
    glMatrixMode(GL_MODELVIEW)
    #
    window.clear()
    p.show()
    for food in dinner:
        food.show()
    for poison in venom:
        poison.show()
    #
    # fps_display.draw()
    glPopMatrix()

pyglet.clock.schedule(draw)
pyglet.clock.schedule_interval(addFood, 0.002)
pyglet.clock.schedule_interval(addPoision, 0.02)
pyglet.app.run()



