import config
from graphic.shape import RectShape, Shape

class Thing(object):
    def __init__(self, shape):
        self.shape = shape
        self.vector = [0.0,0.0]
        config.objects.append(self)

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
    def __init__(self, height, size = 100):
        self.height = height
        self.size = size
        self.up = RectShape(config.pipes_color, (650,0), (50,height))
        self.down = RectShape(config.pipes_color, (650,height+size), (50,config.screen_size[1]))
        super(Pipe, self).__init__(Shape(self.down, self.up))
        self.vector = [-config.speed, 0]
