from graphic.shape import *
from logic_object import Thing, Pipe
from random import randint


class GameLogic:
    def __init__(self):
        self.keys = []

    def on_init(self):
        config.World.objects = []
        self.scoreShape = TextShape((50,50), "Wynik: " + str(config.World.score))
        Thing(self.scoreShape)
        self.strawberry = Thing(ImageShape('graphic/pics/food.bmp', config.Player.init_pos, config.Player.size))

        # test pipes setup
        size = randint(90, 200)
        height = randint(0, config.Window.size[1] - 200)
        self.pipe = Pipe(height, size)

    def keyDown(self, key):
        self.keys.append(key)

    def on_loop(self):
        if config.World.pause and pygame.K_SPACE in self.keys:
            config.World.pause = False

        if not config.World.pause:
            if pygame.K_SPACE in self.keys:
                self.strawberry.addVector(config.World.jump_vector)
            self.strawberry.addVector(config.World.gravity_vector)
            self.strawberry.on_loop()
            self.pipe.on_loop()

            # end level condition
            if self.strawberry.getPos()[1] + config.Player.size[1] > config.Window.size[1] or self.strawberry.getPos()[1] < 0 or ((self.strawberry.getPos()[0]+config.Player.size[0]-10 > self.pipe.getPos()[0] and self.strawberry.getPos()[0]-40 < self.pipe.getPos()[0]) and (self.strawberry.getPos()[1]+10 < self.pipe.height or self.strawberry.getPos()[1]+config.Player.size[1]-10 > self.pipe.height + self.pipe.size)):
                config.World.score = 0
                self.on_init()
            elif self.pipe.getPos()[0] < 0:
                config.World.score += 1
                self.on_init()
        self.keys = []