from random import randint

import config
from graphic.shape import RectShape, Shape

class Thing(object):
    def __init__(self, shape):
        self.shape = shape
        self.vector = [0.0,0.0]
        config.World.objects.append(self)

    def addVector(self, vector):
        self.vector[0] += vector[0]
        self.vector[1] += vector[1]

    def setPos(self, pos):
        self.shape.setPos(pos)

    def getPos(self):
        return self.shape.getPos()

    def draw(self):
        self.shape.draw()

    def on_loop(self):
        self.shape.move(self.vector)

class Pipe(Thing):
    def __init__(self):
        self.size = randint(config.Pipes.minsize, config.Pipes.maxsize)
        x = config.Pipes.default_x if config.Pipes.default_x >= 0 else config.Window.size[0] + config.Pipes.default_x
        self.height = randint(config.Pipes.min_top_gap, config.Window.size[1] - config.Pipes.min_down_gap - self.size)
        self.height = self.height if self.height >= 0 else config.Window.size[1] + self.height

        self.up = RectShape(config.Pipes.color, (x,0), (config.Pipes.width, self.height))
        self.down = RectShape(config.Pipes.color, (x,self.height+self.size), (config.Pipes.width, config.Window.size[1]))
        super(Pipe, self).__init__(Shape(self.down, self.up))
        self.vector = [-config.Pipes.speed, 0]
