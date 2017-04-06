from graphic.shape import *
from logic_object import Thing, Pipe, ScoreBoard


class GameLogic:
    def __init__(self):
        self.keys = []
        ScoreBoard()

    def on_init(self):
        config.World.objects = [config.World.objects[0]]
        self.strawberry = Thing(ImageShape('graphic/pics/food.bmp', config.Player.init_pos, config.Player.size))
        Pipe()

    def keyDown(self, key):
        self.keys.append(key)

    def on_loop(self):
        if config.World.pause and pygame.K_SPACE in self.keys:
            config.World.pause = False

        if not config.World.pause:
            if pygame.K_SPACE in self.keys:
                self.strawberry.addVector(config.World.jump_vector)
            self.strawberry.addVector(config.World.gravity_vector)

            for thing in config.World.objects:
                thing.on_loop()

            # end level condition
            pipe = config.World.objects[2]
            if self.strawberry.getPos()[1] + config.Player.size[1] > config.Window.size[1] or self.strawberry.getPos()[1] < 0 or ((self.strawberry.getPos()[0]+config.Player.size[0]-10 > pipe.getPos()[0] and self.strawberry.getPos()[0]-40 < pipe.getPos()[0]) and (self.strawberry.getPos()[1]+10 < pipe.height or self.strawberry.getPos()[1]+config.Player.size[1]-10 > pipe.height + pipe.size)):
                config.World.score = 0
                self.on_init()
            elif pipe.getPos()[0] < 0:
                config.World.score += 1
                del config.World.objects[2]
                Pipe()
        self.keys = []