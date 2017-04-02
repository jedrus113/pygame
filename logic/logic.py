from graphic.shape import *
from logic_object import Thing


class GameLogic:
    def on_init(self):
        config.pause = True
        config.graphic_engine.cleanShapes()
        self.strawberry = Thing(ImageShape('graphic/pics/food.bmp', config.init_pos, config.player_size))

    def on_loop(self):
        if config.pause and pygame.K_SPACE in config.keys:
            config.pause = False
        if not config.pause:
            if pygame.K_SPACE in config.keys:
                self.strawberry.addVector(config.jump_vector)
            self.strawberry.addVector(config.gravity_vector)
            self.strawberry.on_loop()

            if self.strawberry.getPos()[1] + config.player_size[1] > config.screen_size[1] or self.strawberry.getPos()[1] < 0:
                self.on_init()