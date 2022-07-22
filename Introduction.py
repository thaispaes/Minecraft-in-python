from ursina import *

class Test_cube(Entity):
    def _init_(self):
        super()._init_(
            model = 'cube',
            color = color.white,
            texture = 'white_cube',
            rotation = Vec3(45,45,45)
            )

def update():
    if held_keys['a']:
        test_square.x -=4 * time.dt

app = Ursina()

test_square = Entity(model = 'quad', color = color.black, scale = (1,4), position = (5,4))

sans_texture = load_texture('assets/Sans.jpeg')
sans = Entity(model = 'quad', texture = sans_texture)

test_cube = Test_cube()

app.run()
