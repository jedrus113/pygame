import config
from graphic.shape import *


class GameLogic:
    def on_init(self):
        self.size = 10
        self.inc = 1
        shapes = []
        shapes.append(ImageShape('graphic/pics/food.bmp', (230,170)))
        self.circle = CircleShape((0,255,255), self.size, (200,200))
        shapes.append(self.circle)
        shapes.append(ImageShape('graphic/pics/food.bmp', (200,170)))
        config.graphic_engine.addShape(*shapes)


    def on_loop(self):
        self.size += self.inc
        self.circle.radius = self.size
        if self.size >= 100 or self.size <= 10:
            self.inc = -self.inc