import pyglet
from pyglet.window import key
from pyglet.gl import glEnable, glTexParameteri, GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST
from game import resources
from game.game_window import game_window

glEnable(GL_TEXTURE_2D)
glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)

window = game_window(1280, 720, "SBLD", resizable=True)

main_batch = pyglet.graphics.Batch()

player_character = pyglet.sprite.Sprite(img=resources.idle_ani, x=200, y=200, batch=main_batch)

@window.event
def on_draw():
    window.clear()
    main_batch.draw()


if __name__ == '__main__':
    pyglet.app.run()

