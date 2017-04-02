from graphic.shape import *
from logic_object import Thing


class GameLogic:
    def on_init(self):
        self.strawberry = Thing(ImageShape('graphic/pics/food.bmp', (230,170)))

    def on_loop(self):
        if pygame.K_SPACE in config.keys:
            self.strawberry.addVector(config.jump_vector)
        self.strawberry.addVector(config.gravity_vector)
        self.strawberry.on_loop()
