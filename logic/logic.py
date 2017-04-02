import config
from graphic.shape import *


class GameLogic:
    def on_init(self):
        self.inc = 1
        self.inc_timer = 0
        shapes = []
        self.strawberry = ImageShape('graphic/pics/food.bmp', (230,170))
        shapes.append(self.strawberry)
        config.graphic_engine.addShape(*shapes)

        self.strawberry.fetch()
        self.max_size = self.strawberry.size[0]+10
        self.min_size = self.strawberry.size[0]

    def on_loop(self):
        if self.inc_timer < 1:
            self.inc_timer = 2
            self.strawberry.size = (self.strawberry.size[0]+self.inc, self.strawberry.size[1]+self.inc)
            if self.strawberry.size[0] >= self.max_size  or self.strawberry.size[0] <= self.min_size:
                self.inc = -self.inc
        else:
            self.inc_timer -= 1

