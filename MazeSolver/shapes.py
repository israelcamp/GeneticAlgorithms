import pyglet

def square_list(x, y, width, color=(51, 0, 102)):
    vertex_list = pyglet.graphics.vertex_list(4,
                    ('v2f',(x, y, x+width, y, x+width, y+width, x, y+width)),
                    ('c3B', color*4))
    return vertex_list