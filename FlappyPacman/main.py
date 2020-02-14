from pyglet.window import Window
import pyglet
from game import FBGame

window = Window(600, 800, caption='Flappy Bird', vsync=0.0)

fps_display = pyglet.clock.Clock()

game_dict = {
    'bird_x': 80.,
    'bird_y': window.height/2.,
    'bird_radius': 30.,
    'pipe_x': 160,
    'pipe_size': 80,
    'window_width': window.width + 60,
    'window_height': window.height,
    'birds_pop_size': 100
}
game = FBGame(first=True, **game_dict)


@window.event
def on_key_press(symbol, modifiers):
    if symbol is pyglet.window.key.W:
        # game.jump_bird()
        pass
    if symbol is pyglet.window.key.R:
        game.reset(first=True)


@window.event
def on_draw():
    window.clear()
    game.show()
    # fps_display.draw()


pyglet.clock.schedule_interval(game.update, 1./120.)
pyglet.app.run()
