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
    glColor4f(color[0]/255, color[1]/255, color[2]/255, 1.0)
    glBegin(GL_TRIANGLE_FAN)
    glVertex2f(x, y)
    for i in range(iterations+1):
        glVertex2f(x+dx, y+dy)
        dx, dy = (dx*c - dy*s), (dy*c + dx*s)
    glEnd()

def cartesian(wband, wheight, delta):
    sz = 2*delta
    glPushMatrix()
    glColor4f(0., 0., 0., 1.)
    #changes line width
    glLineWidth(3)
    #adds the middle vertical line
    glBegin(GL_LINES)
    glVertex2f(wband/2, 0.)
    glVertex2f(wband/2, wheight)
    glEnd()
    #adds the middle vertical line
    glBegin(GL_LINES)
    glVertex2f(0., wheight/2)
    glVertex2f(wband, wheight/2)
    glEnd()
    #add the upper triangle
    triangle(wband/2 - sz/2, wheight - sz - 5, size=sz, color=(0, 0, 0, 255))
    #add the right triangle
    glPushMatrix()
    glTranslatef(wband - sz, wheight/2, 0)
    glRotatef(-90, 0, 0, 1)
    triangle(-sz/2, 0, size=sz, color=(0, 0, 0, 255))
    glPopMatrix()
    glPopMatrix()

def grid(wband, wheight, delta):
    delta *= 5
    vertical_lines = int(wheight/delta)
    horizontal_lines = int(wband/delta)
    glPushMatrix()
    glLineWidth(1)
    #add the vertical lines
    for i in range(vertical_lines-1):
        glBegin(GL_LINES)
        glVertex2f((i+1)*delta, 0.)
        glVertex2f((i+1)*delta, wheight)
        glEnd()
    #add the horizontal lines
    for i in range(horizontal_lines-1):
        glBegin(GL_LINES)
        glVertex2f(0, (i+1)*delta)
        glVertex2f(wband, (i+1)*delta)
        glEnd()    
    glPopMatrix()

def line(x0, y0, x1, y1, color):
    glColor4f(color[0]/255, color[1]/255, color[2]/255, color[3]/255)
    glLineWidth(5)
    glBegin(GL_LINES)
    glVertex2f(x0, y0)
    glVertex2f(x1, y1)
    glEnd()
