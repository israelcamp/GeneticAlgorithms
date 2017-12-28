import pyglet
from pyglet.gl import *
from numpy import pi, sin, cos

def square_list(x, y, width, color=(51, 0, 102)):
    vertex_list = pyglet.graphics.vertex_list(4,
                    ('v2f',(x, y, x+width, y, x+width, y+width, x, y+width)),
                    ('c3B', color*4))
    return vertex_list

def circle(x, y, radius, color=(255, 255, 255)):
    iterations = int(2*radius*pi)
    s = sin(2*pi / iterations)
    c = cos(2*pi / iterations)

    dx, dy = radius, 0
    glColor3f(color[0]/255, color[1]/255, color[2]/255)
    glBegin(GL_TRIANGLE_FAN)
    glVertex2f(x, y)
    for i in range(iterations+1):
        glVertex2f(x+dx, y+dy)
        dx, dy = (dx*c - dy*s), (dy*c + dx*s)
    glEnd()

def text(txt, x, y, size):
    label = pyglet.text.Label(text=txt, font_name='Times New Roman',
                          font_size=size,
                          x=x, y=y,
                          anchor_x='center', anchor_y='center',
                          color=(0, 0, 0, 255))
    label.draw()