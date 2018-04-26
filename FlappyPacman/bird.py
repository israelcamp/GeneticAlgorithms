import pyglet.gl as GL
from numpy.linalg import norm
from numpy import pi, sin, cos, linspace

class Bird():


    def __init__(self, x, y, radius, height=800):
        """Class for Bird, or Pacman :), for the game Flappy Bird."""
        self.x, self.y, self.radius = x, y, radius
        self.velocity, self.gravity = 0, -0.3        
        self.height = height

    def show(self):
        """Shows the Bird = Pacman."""
        self.pacman(self.x, self.y, self.radius)
        
    def updates(self):
        """Updates the y position of the bird."""
        self.apply_gravity()
        self.y += self.velocity
        # self._keep_inside()

    def apply_gravity(self):
        """Applies the force of gravity to the bird."""
        self.velocity += self.gravity

    def apply_force(self, accelaration):
        """Applies user input force to the bird."""
        self.velocity += 1.3*accelaration

    def hits(self, pipe):
        """Given the pipe, checks if the bird hits the pipe."""
        #checks the x postion
        if self.x > pipe.x and self.x < pipe.x + pipe.size:
            if self.y + self.radius > pipe.height - pipe.spacing or\
                self.y - self.radius < pipe.height - 2 * pipe.spacing or\
                self.y > self.height:
                return True
        if self.y < 0 :
                return True
        return False

    def _keep_inside(self):
        """Checks if the bird is trying to get out of the screen, adjust if so."""
        if self.y > self.height:
            self.y = self.height
            self.velocity = 0
        elif self.y < 0:
            self.y = 0
            self.velocity = 0

    @staticmethod
    def pacman(x, y, radius, color=(255, 255, 0, 255)):
        """Draws the bird."""
        GL.glColor4f(color[0]/255, color[1]/255, color[2]/255, color[3]/255)
        GL.glBegin(GL.GL_POLYGON)
        GL.glVertex2f(x, y)
        for i in linspace(0.15, 1.85, num=30):
            dx = x + radius*cos(i*pi)
            dy = y + radius*sin(i*pi)
            GL.glVertex2f(dx, dy)
        GL.glEnd()