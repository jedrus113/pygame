import config


class Thing(object):
    def __init__(self, shape):
        self.shape = shape
        self.vector = [0.0,0.0]

        config.graphic_engine.addShape(self.shape)

        self.inc_timer = 0
        self.inc = 1

    def addVector(self, vector):
        self.vector[0] += vector[0]
        self.vector[1] += vector[1]

    def setPos(self, pos):
        self.shape.setPos(pos)

    def getPos(self):
        return self.shape.getPos()

    def on_loop(self):
        self.shape.move((int(self.vector[0]), int(self.vector[1])))
        if self.getPos()[1] > config.screen_size[1] or self.getPos()[1] < 0:
            self.vector = [0,0]
            self.setPos([250,250])