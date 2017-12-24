import pyglet
from planet import Population

window = pyglet.window.Window()
class Message():
    def __init__(self):
        self.label = pyglet.text.Label('None',
                          font_name='Times New Roman',
                          font_size=36,
                          x=window.width//2, y=window.height//2,
                          anchor_x='center', anchor_y='center')
    def update_msg(self, sms):
        self.label.text = sms

class God():
    def __init__(self, goal, size_pop, mutationRate):
        self.msg = Message()
        self.planet = Population(goal, size_pop, mutationRate)
        self.pop = self.planet.make_population()
        self.best_member = self.pop[0]
    def update_world(self, dt):
        if self.best_member.fitness() < 1:
            self.pop, self.best_member = self.planet.one_step_evolve(self.pop)
        self.msg.update_msg(''.join(self.best_member.value))
goal = 'Natalia Goska'
g = God(goal, size_pop=200, mutationRate=0.01)

@window.event
def on_draw():
    window.clear()
    g.msg.label.draw()
pyglet.clock.schedule(g.update_world)
pyglet.app.run()
