from graphic.shape import *
from logic_object import Thing, Pipe
from random import randint


class GameLogic:
    def on_init(self):
        config.pause = True
        config.objects = []
        self.scoreShape = TextShape((50,50), "Wynik: " + str(config.score))
        Thing(self.scoreShape)
        self.strawberry = Thing(ImageShape('graphic/pics/food.bmp', config.init_pos, config.player_size))
        size = randint(50, 200)
        height = randint(0, config.screen_size[1] - 200)
        self.pipe = Pipe(height, size)

    def on_loop(self):
        if config.pause and pygame.K_SPACE in config.keys:
            config.pause = False

        if not config.pause:
            if pygame.K_SPACE in config.keys:
                self.strawberry.addVector(config.jump_vector)
            self.strawberry.addVector((config.gravity_vector[0], config.gravity_vector[1]))
            self.strawberry.on_loop()
            self.pipe.on_loop()


            if self.strawberry.getPos()[1] + config.player_size[1] > config.screen_size[1] or self.strawberry.getPos()[1] < 0 or ((self.strawberry.getPos()[0]+config.player_size[0]-10 > self.pipe.getPos()[0] and self.strawberry.getPos()[0]-40 < self.pipe.getPos()[0]) and (self.strawberry.getPos()[1]+10 < self.pipe.height or self.strawberry.getPos()[1]+config.player_size[1]-10 > self.pipe.height + self.pipe.size)):
                #config.score = 0
                self.on_init()
            elif self.strawberry.getPos()[0] > config.screen_size[0]:
                config.score += 1
                self.on_init()