from pyglet.gl import *
from numpy import pi, sin, cos, linspace

def triangle(x, y, size, angle = 0, color=(255, 255, 255, 150)):
    glColor4f(color[0]/255, color[1]/255, color[2]/255, color[3]/255)
    glBegin(GL_TRIANGLES)
    glVertex2f(x, y)
    glVertex2f(x + size, y)
    glVertex2f(x + size/2, y + size*1.4)
    glEnd()


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

def line(x, y, length, color=(0, 0, 0)):
    glColor4f(color[0]/255, color[1]/255, color[2]/255, 1.0)
    glBegin(GL_LINE_STRIP)
    glVertex2f(x, y)
    glVertex2f(x, y+length*20)
    glEnd()

def pacman(x, y, radius, color=(255, 255, 0, 255)):
    glColor4f(color[0]/255, color[1]/255, color[2]/255, color[3]/255)
    glBegin(GL_POLYGON)
    glVertex2f(x, y)
    for i in linspace(0.15, 1.85, num=30):
        dx = x + radius*cos(i*pi)
        dy = y + radius*sin(i*pi)
        glVertex2f(dx, dy)
    glEnd()