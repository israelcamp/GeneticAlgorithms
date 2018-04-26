import pyglet
from collections import deque
from pacman import Pacman
from pipe import Pipe
from ga import make_new_gen
class FBGame():


    def __init__(self, first=True, **kwargs):
        """Class that controls the Flappy Bird Pacman."""
        self.game_dict = kwargs
        if first:
            self.highest_score = 0
            self._create_birds_population(**kwargs)
        self.pipes_pop = self._create_pipes_population(**kwargs)
        self.height, self.width, self.pipe_size = kwargs['window_height'], kwargs['window_width'], kwargs['pipe_size']

    def update(self, dt):
        """Updates the state of the game, updates bird and pipes."""
        inputs = self._make_inputs() #prepare inputs from the pipes
        self.all_dead = True #suppose that all birds are dead
        self._update_birds_pop(inputs) #updates every bird
        if self.all_dead:
            self.birds_pop = deque(make_new_gen(self.birds_pop)) #creates new population of birds
            self.reset()  #resets pipes position
        self._updates_pipes_pop() #updates pipes positions
        
    def show(self):
        """Shows the bird and the pipes."""
        for bird in self.birds_pop:
            if not bird.lost:
                bird.show()
        for pipe in self.pipes_pop:
            pipe.show()
        self._show_high_score()
    
    def reset(self, first=False):
        """Resets the game to initial state."""
        self.__init__(first=first, **self.game_dict)

    def _update_birds_pop(self, inputs):
        """Updates the birds y position"""
        for bird in self.birds_pop:
            #checks if the birds hit one of the pipes
            if bird.hits(self.pipes_pop[0]):
                bird.lost = True
            if not bird.lost:
                self.all_dead = False
                bird.increase_score()
                bird.decides_jump(inputs)
                bird.updates()

    def _updates_pipes_pop(self):
        """Updates pipes position."""
        for pipe in self.pipes_pop:
            pipe.updates()
        if self.pipes_pop[0].x + self.pipe_size < 0:
            self.pipes_pop.popleft()
            self._append_new_pipe()

    def _make_inputs(self):
        """Make part of the network inputs based only on the info about the closest pipe."""
        if self.pipes_pop[0]. x + self.pipes_pop[0].size < self.game_dict['bird_x']:
            inputs = self._make_pipes_input(self.pipes_pop[1])
        else:
            inputs = self._make_pipes_input(self.pipes_pop[0])
        return inputs

    def _make_pipes_input(self, pipe):
        """Create the list with pipe info normalized."""
        return [pipe.x / self.width, (pipe.height - pipe.spacing) / self.height, (pipe.height - 2*pipe.spacing) / self.height]

    def _high_score(self):
        """Calculates highest current score and updates the all time best."""
        high = 0
        for bird in self.birds_pop:
            if high < bird.fitness:
                high = bird.fitness
        if self.highest_score < high:
            self.highest_score = high
        return high

    def _show_high_score(self):
        """Show the highest scores."""
        pyglet.text.Label('Highest Score Now: {}'.format(self._high_score()),font_name='Times New Roman',font_size=20,x=0, y=0, color=(255,0,0,255),
                                  anchor_x='left', anchor_y='bottom').draw()
        pyglet.text.Label('Highest Score Ever: {}'.format(self.highest_score),font_name='Times New Roman',font_size=20,x=0, y=25, color=(0,255,0,255),
                                  anchor_x='left', anchor_y='bottom').draw()


    def _game_over(self):
        """Draws the Game Over message."""
        pyglet.text.Label('Game Over',font_name='Times New Roman',font_size=60,x=self.width/2, y=self.height/2, color=(255,0,0,255),
                                  anchor_x='right', anchor_y='center').draw()

    def _append_new_pipe(self):
        """Appends a new pipe to the game."""
        self.pipes_pop.append(Pipe(x=self.pipes_pop[-1].x + 5*self.pipe_size, size=self.pipe_size, height=self.height))

    def _create_pipes_population(self, **kwargs):
        """Creates the inital population of pipes."""
        return deque([Pipe(x=kwargs['pipe_x'] + dx, height=kwargs['window_height'], size=kwargs['pipe_size'])
                        for dx in range(kwargs['pipe_x'], kwargs['window_width'], 5*kwargs['pipe_size'])])

    def _create_birds_population(self, **kwargs):                                         
        self.birds_pop = deque([])
        for i in range(kwargs['birds_pop_size']):
            self.birds_pop.append(Pacman(x=kwargs['bird_x'], y=kwargs['bird_y'], 
                        radius=kwargs['bird_radius'], height=kwargs['window_height']))