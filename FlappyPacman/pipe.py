import pyglet.gl as GL
from numpy.random import randint
class Pipe():


    def __init__(self, x, size, height):
        """Class that defines a pair of pipes, top and bottom."""
        self.x, self.height, self.size = x, height, size
        self.spacing = randint(low=2*self.size, high=4*self.size)
        self.velocity = 4

    def show(self):
        """Shows the pipe."""
        self._draw_pipes(self.x, self.spacing, self.height, delta=self.size)

    def updates(self):
        """Updates the x position of the pipe."""
        self.x -= self.velocity

    @staticmethod
    def _draw_pipes(x, spacing, height, delta=80):
        """Draw the pair of pipes."""
        GL.glPushMatrix()
        GL.glColor4f(1., 1., 1., 1.)
        
        GL.glBegin(GL.GL_QUADS)
        GL.glVertex2f(x, 0)
        GL.glVertex2f(x + delta, 0)
        GL.glVertex2f(x + delta, height - 2 * spacing)
        GL.glVertex2f(x, height - 2 * spacing)
        GL.glEnd()

        GL.glBegin(GL.GL_QUADS)
        GL.glVertex2f(x, height)
        GL.glVertex2f(x, height - spacing)
        GL.glVertex2f(x + delta, height - spacing)
        GL.glVertex2f(x + delta, height)
        GL.glEnd()

        GL.glPopMatrix()