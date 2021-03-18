import pyglet
import time
from pyglet.window import key
from . import resources


class Player(pyglet.sprite.Sprite):

    def __init__(self, *args, **kwargs):
        super().__init__(img=resources.player_character[0], *args, **kwargs)
        self.jump_height = 500
        self.vspeed = 0.0
        self.max_speed = 1000
        self.speed= 0.0

        self.velocity_x, self.velocity_y = 0.0, 0.0

        self.flipped = False
        self.is_running = False
        self.is_jumping = False
        self.is_falling = False
        self.key_handler = key.KeyStateHandler()

    def on_key_press(self, symbol, modifiers):
        if symbol == key.D:
            self.flipped = False
            self.run(self.flipped)
        if symbol == key.A:
            self.flipped = True
            self.run(self.flipped)
        if symbol == key.SPACE:
            self.jump()

    def on_key_release(self, symbol, modifiers):
        if self.key_handler[key.D] == False and self.key_handler[key.A] == False:
            self.stand()
            
        if self.key_handler[key.D] == True and self.key_handler[key.A] == False:
            self.flipped = False
            self.run(self.flipped)

        if self.key_handler[key.D] == False and self.key_handler[key.A] == True:
            self.flipped = True
            self.run(self.flipped)

    def stand(self):
        self.speed = 0
        if self.flipped == False:
            self.image = resources.player_character[0]
            self.draw()
        if self.flipped == True:
            self.image = resources.player_character[1]
            self.draw()

    def run(self, flipped):
        self.is_running = True
        if flipped == False:
            self.speed = self.max_speed
            self.image = resources.player_character[2]
            self.draw()
        elif flipped == True:
            self.speed = -self.max_speed
            self.image = resources.player_character[3]
            self.draw()

    def jump(self):
        if self.is_jumping == False:
            self.is_jumping = True
            self.vspeed = self.jump_height
    
    def gravity(self):
        if self.is_falling:
            self.vspeed = -self.jump_height
            
    
    def update(self, dt):
        self.x += self.velocity_x * dt
        self.velocity_x += (self.speed - self.velocity_x) * .5
        self.y += self.velocity_y * dt
        self.velocity_y += (self.vspeed - self.velocity_y) * .3
        

        

    
