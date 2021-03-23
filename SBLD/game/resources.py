import pyglet
pyglet.resource.path = ['../resources']
pyglet.resource.reindex()

def resize_image(image, scale):
    """Resizes Image"""
    image.width *= scale
    image.height *= scale

def resize_ani(grid, scale):
    """Resizes Image"""
    for item in grid:
        item.width *= scale
        item.height *= scale

def center_image(image):
    """Sets an image's anchor point to its center"""
    image.anchor_x = image.width // 2
    image.anchor_y = 32

def center_ani(grid):
    """Sets an animation's anchor point to its center"""
    for item in grid:
        item.anchor_x = item.width // 2
        item.anchor_y = 13

def sprite_image(image,scale):
    image = pyglet.resource.image(image)
    resize_image(image,scale)
    center_image(image)
    return image


def animate_sprite(image, rows, columns, scale, duration, loop):
    """Animates and processes sprite"""
    sprite_sheet = pyglet.resource.image(image)
    sprite_grid = pyglet.image.ImageGrid(sprite_sheet, rows=rows, columns=columns)
    resize_ani(sprite_grid, scale)
    center_ani(sprite_grid)
    ani = pyglet.image.Animation.from_image_sequence(sprite_grid, duration=duration, loop=loop)
    return ani

# Player Sprites

idle_ani = animate_sprite('idle.png', 1, 2, 5, 0.2, True)
fl_idle = animate_sprite('idle_flipped.png', 1, 2, 5, 0.2, True)

running_ani = animate_sprite('running.png', 1, 8, 5, 0.1, True)
fl_running = animate_sprite('running_flipped.png', 1, 8, 5, 0.1, True)

jumping_ani = animate_sprite('Jumping.png', 1, 10, 5, 0.1, False)
fl_jumping = animate_sprite('Jumping_flipped.png', 1, 10, 5, 0.1, False)

player_character = [idle_ani, fl_idle, running_ani, fl_running, jumping_ani]

# Platform Sprite
platform = sprite_image('platform.png',5)