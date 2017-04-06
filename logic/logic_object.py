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
    def __init__(self, pos, size):
        try:
            x = pos[0]
            self.height = pos[1]
        except TypeError:
            x = config.Pipes.default_x
            self.height = pos
        x = x if x >= 0 else config.Window.size[0] + x
        self.height = self.height if self.height >= 0 else config.Window.size[1] + self.height
        self.size = size

        self.up = RectShape(config.Pipes.color, (x,0), (50,self.height))
        self.down = RectShape(config.Pipes.color, (x,self.height+size), (50,config.Window.size[1]))
        super(Pipe, self).__init__(Shape(self.down, self.up))
        self.vector = [-config.Pipes.speed, 0]
