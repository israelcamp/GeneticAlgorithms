import pyglet
from pyglet.window import mouse
import numpy as np
import shapes
from survivor import Survivor
from food import Food
from population import Population
from predator import Predator
'''creates window and enable alpha'''
window = pyglet.window.Window(1000, 600, caption='Evolutionary Steering')
pyglet.gl.glBlendFunc( pyglet.gl.GL_SRC_ALPHA, pyglet.gl.GL_ONE_MINUS_SRC_ALPHA)
pyglet.gl.glEnable(pyglet.gl.GL_BLEND)
pyglet.gl.glClearColor(1.0, 1.0, 1.0, 1.0)


predator = Predator()
dinner = [Food(1) for _ in range(30)]
venom = [Food(-1) for _ in range(10)]
p = Population(10)
p.makePopulation()
def addPoision(dt):
    if len(venom) < 10:
        venom.append(Food(-1))
def addFood(dt):
    if len(dinner) < 30:
        dinner.append(Food(1))
def draw(dt):
    predator.hunting(p.pop)
    predator.update()
    p.popSeek(dinner, venom, predator)
    p.popUpdate()

@window.event
def on_mouse_press(x, y, button, modifiers):
    if button == mouse.RIGHT:
        p.addSurvivor()
    if button == mouse.LEFT:
        dinner.append(Food(1))
    if button == mouse.MIDDLE:
        venom.append(Food(-1))
@window.event
def on_draw():
    window.clear()
    predator.show()
    p.show()
    for food in dinner:
        food.show()
    for poison in venom:
        poison.show()
pyglet.clock.schedule(draw)
pyglet.clock.schedule_interval(addFood, 0.2)
pyglet.app.run()



