import pyglet
from pyglet import gl as GL
import argparse
from planet import Population

parser = argparse.ArgumentParser()
parser.add_argument('-goal', default="Curso de Matematica", help='Set in this the string that you want to evolve to')
parser.add_argument('-mutRate', default=0.01, type=int, help='Set in this the mutation rate for the population')
parser.add_argument('-pop', default=200, type=int, help='Set in this the number of members per population')
args = parser.parse_args()
goal = args.goal
size_pop = args.pop
mutationRate = args.mutRate

window = pyglet.window.Window(width=600, height=400, resizable=True, caption='Genetic Algorithm, Goal: '+goal)
class Message(pyglet.text.Label):
    def __init__(self, xOff, yOff, color, text='', font_size=20):
        super().__init__(text=text, font_name='Times New Roman', font_size=font_size, x=window.width//2 + xOff, y=window.height//2 + yOff,\
                          anchor_x='center', anchor_y='center', color=color)
        self.xOff, self.yOff = xOff, yOff

    def update_msg(self, sms):
        self.text = sms
        
class God():
    def __init__(self, goal, size_pop, mutationRate):
        self.msg_member = Message(0, 0, color=(255,255,147,255), font_size=36)
        self.msg_fitness = Message(xOff=-90, yOff=-150, color=(255,255,255,255))
        self.msg_gen = Message(xOff=20, yOff=-100, color=(255,255,255,255))
        self.planet = Population(goal, size_pop, mutationRate)
        self.pop = self.planet.make_population()
        self.best_member = self.pop[0]
        self.count_gen = 0
        
    def update_world(self, dt):
        if self.best_member.fitness() < 1:
            self.count_gen += 1
            self.pop, self.best_member = self.planet.one_step_evolve(self.pop)
            self.msg_member.update_msg(''.join(self.best_member.value))
            self.msg_fitness.update_msg('{:.3f}'.format(self.best_member.fitness()))
            self.msg_gen.update_msg(str(self.count_gen))
            
g = God(goal, size_pop=size_pop, mutationRate=mutationRate)

msg_info1 = Message(text='Best Fitness:', xOff=-200, yOff=-150, color=(0,191,255,255))
msg_info2 = Message(text='Number of Generations:', xOff=-145, yOff=-100, color=(0,191,255,255))

labels = [g.msg_member, g.msg_fitness, g.msg_gen, msg_info1, msg_info2]

@window.event
def on_draw():
    GL.glPushMatrix()
    GL.glViewport(0, 0, window.width, window.height)
    GL.glMatrixMode(GL.GL_PROJECTION)
    GL.glLoadIdentity()
    GL.glOrtho(0, 600, 0, 400, -1, 1)
    GL.glMatrixMode(GL.GL_MODELVIEW)
    window.clear()
    for label in labels:
        label.draw()
    GL.glPopMatrix()

pyglet.clock.schedule(g.update_world)
pyglet.app.run()
