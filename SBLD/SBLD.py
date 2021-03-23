import pyglet
from pyglet.gl import glEnable, glTexParameteri, GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST
from game import player
from game.window import Game_Window

glEnable(GL_TEXTURE_2D)
glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)

window = Game_Window(1280, 720, "SBLD", resizable=True)

main_batch = pyglet.graphics.Batch()


player_character = player.Player(x=400, y=200, batch=main_batch)

window.push_handlers(player_character)
window.push_handlers(player_character.key_handler)

game_objects = [player_character]

@window.event
def on_draw():
    window.clear()
    main_batch.draw()
def update(dt):
    for obj in game_objects:
        obj.update(dt)


if __name__ == '__main__':
    pyglet.clock.schedule_interval(update, 1/60.0)
    pyglet.app.run()

