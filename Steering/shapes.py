import pyglet
from pyglet.gl import *
from numpy import pi, sin, cos, linspace

def triangle(x, y, size, angle = 0, color=(255, 255, 255, 150)):
    glPushMatrix()
    glTranslatef(x + size/2, y + size/3, 0.0)
    glRotatef(angle, 0, 0, 1)
    glTranslatef(-x - size/2, -y - size/3, 0.)
    pyglet.graphics.draw(3, pyglet.gl.GL_TRIANGLES,
            ('v2f', (x, y, x+size, y, x+size/2, y+size*1.4)),
            ('c4B', color*3))

    glPopMatrix()

def circle(x, y, radius, color=(255, 0, 0)):
    iterations = int(2*radius*pi)
    s = sin(2*pi / iterations)
    c = cos(2*pi / iterations)
    dx, dy = radius, 0
    glColor4f(color[0]/255, color[1]/255, color[2]/255, 0.7)
    glBegin(GL_TRIANGLE_FAN)
    glVertex2f(x, y)
    for i in range(iterations+1):
        glVertex2f(x+dx, y+dy)
        dx, dy = (dx*c - dy*s), (dy*c + dx*s)
    glEnd()

def ring(x, y, radius, color=(255,0,0)):
    glColor4f(color[0]/255, color[1]/255, color[2]/255, 1.0)
    glBegin(GL_LINE_STRIP)
    for i in linspace(0.0, 2.0, num=50):
        dx = x + radius*cos(i*pi)
        dy = y + radius*sin(i*pi)
        glVertex2f(dx, dy)
    glEnd()

