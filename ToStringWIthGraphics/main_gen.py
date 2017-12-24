import pyglet
from planet import Population

window = pyglet.window.Window()
class Message():
    def __init__(self, texto='None', font_size=36, xOff=0, yOff=0, anchor_x='center', anchor_y='center',color=(255,255,255,255)):
        self.label = pyglet.text.Label(text=texto,
                          font_name='Times New Roman',
                          font_size=font_size,
                          x=window.width//2 + xOff, y=window.height//2 + yOff,
                          anchor_x=anchor_x, anchor_y=anchor_y,
                          color=color)
    def update_msg(self, sms):
        self.label.text = sms
    def show(self):
        self.label.draw()
class God():
    def __init__(self, goal, size_pop, mutationRate):
        self.msg_member = Message(color=(255,20,147,255))
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
goal = 'Natalia Goska'
g = God(goal, size_pop=200, mutationRate=0.01)

msg_info1 = Message(texto='Best Fitness: ', font_size=20, xOff=-200, yOff=-150, color=(0,191,255,255))
msg_info2 = Message(texto='Number of Generations:', font_size=20, xOff=-145, yOff=-100, color=(0,191,255,255))
@window.event
def on_draw():
    window.clear()
    msg_info1.show()
    msg_info2.show()
    g.msg_member.show()
    g.msg_fitness.show()
    g.msg_gen.show()
pyglet.clock.schedule(g.update_world)
pyglet.app.run()
