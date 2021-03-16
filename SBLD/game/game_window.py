import pyglet
from pyglet.gl import glClearColor

class game_window(pyglet.window.Window):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.set_minimum_size(400, 300)
        glClearColor(0,0.5,1,0)
        

