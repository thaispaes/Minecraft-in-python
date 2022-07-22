
from ursina import *

def update():
    if held_keys['a']:
        test_square.x -=4 * time.dt

app = Ursina()

test_square = Entity(model = 'quad', color = color.black, scale = (1,4), position = (5,4))

sans_texture = load_texture('assets/Sans.jpeg')
sans = Entity(model = 'quad', texture = sans_texture, scale = (4,4))

app.run()
