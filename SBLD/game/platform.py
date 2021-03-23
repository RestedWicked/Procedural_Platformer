import pyglet
from . import resources

class Platform(pyglet.sprite.Sprite):

    def __init__(self, *args, **kwargs):
        super().__init__(img=resources.platform, *args, **kwargs)