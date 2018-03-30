import pyglet
from pyglet import gl
from pyglet.gl import *
import argparse
from planet import Population

parser = argparse.ArgumentParser()
parser.add_argument('-goal', help='Set in this the string that you want to evolve to')
parser.add_argument('-mutRate', type=int, help='Set in this the mutation rate for the population')
parser.add_argument('-pop', type=int, help='Set in this the number of members per population')
args = parser.parse_args()
goal = args.goal
size_pop = args.pop
mutationRate = args.mutRate
if goal is None:
	goal = 'Natalia Goska'
if size_pop is None:
    size_pop = 200
if mutationRate is None:
    mutationRate = 0.01

window = pyglet.window.Window(width=600, height=400, resizable=True, caption='Genetic Algorithm, Goal: '+goal)
class Message():
    def __init__(self, texto=' ', font_size=36, xOff=0, yOff=0, anchor_x='center', anchor_y='center',color=(255,255,255,255)):
        self.label = pyglet.text.Label(text=texto,
                          font_name='Times New Roman',
                          font_size=font_size,
                          x=window.width//2 + xOff, y=window.height//2 + yOff,
                          anchor_x=anchor_x, anchor_y=anchor_y,
                          color=color)
        self.xOff, self.yOff = xOff, yOff
    def update_msg(self, sms):
        self.label.text = sms
    def update_pos(self):
        self.label.x = window.width//2 + self.xOff
        self.label.y = window.height//2 + self.yOff
    def show(self):
        self.label.draw()
        
class God():
    def __init__(self, goal, size_pop, mutationRate):
        self.msg_member = Message(color=(255,255,147,255))
        self.msg_fitness = Message(font_size=20, xOff=-120, yOff=-150, anchor_x='left',anchor_y='center')
        self.msg_gen = Message(font_size=20, xOff=20, yOff=-100)
        self.planet = Population(goal, size_pop, mutationRate)
        self.pop = self.planet.make_population()
        self.best_member = self.pop[0]
        self.count_gen = 0
    def update_world(self, dt):
        if self.best_member.fitness() < 1:
            self.count_gen += 1
            self.pop, self.best_member = self.planet.one_step_evolve(self.pop)
            self.msg_member.update_msg(''.join(self.best_member.value))
            self.msg_fitness.update_msg(str(self.best_member.fitness()))
            self.msg_gen.update_msg(str(self.count_gen))
            
g = God(goal, size_pop=size_pop, mutationRate=mutationRate)

msg_info1 = Message(texto='Best Fitness:', font_size=20, xOff=-200, yOff=-150, color=(0,191,255,255))
msg_info2 = Message(texto='Number of Generations:', font_size=20, xOff=-145, yOff=-100, color=(0,191,255,255))

labels = [g.msg_member, g.msg_fitness, g.msg_gen, msg_info1, msg_info2]
def label_update(dt):
    for l in labels:
        l.update_pos()

@window.event
def on_draw():
    window.clear()
    msg_info1.show()
    msg_info2.show()
    g.msg_member.show()
    g.msg_fitness.show()
    g.msg_gen.show()
pyglet.clock.schedule(g.update_world)
pyglet.clock.schedule(label_update)
pyglet.app.run()
