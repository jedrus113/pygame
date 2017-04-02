import pygame

import config


class ShapeBase(object):
    def __init__(self, pos):
        self.pos = pos

    def getPos(self):
        return self.pos

    def setPos(self, pos=(0,0)):
        self.pos = pos

    def move(self, vect):
        self.pos = (self.pos[0] + vect[0], self.pos[1] + vect[1])

    def draw(self):
        raise NotImplementedError()


class CircleShape(ShapeBase):
    def __init__(self, color, radius, pos=(0,0), width=0):
        super(CircleShape, self).__init__(pos)
        self.color = color
        self.radius = radius
        self.width = width

    def draw(self):
        pygame.draw.circle(config.surface, self.color, self.pos, self.radius, self.width)


class ImageShape(ShapeBase):
    cashe = {}
    def __init__(self, path, pos=(0,0)):
        super(ImageShape, self).__init__(pos)
        self.path = path
        self.image_surface = False

    def draw(self):
        if not self.image_surface:
            if self.path in self.cashe:
                self.cashe[self.path][0] += 1
                self.image_surface = self.cashe[self.path][1]
            else:
                self.image_surface = pygame.image.load(self.path).convert()
                transColor = self.image_surface.get_at((0,0))
                self.image_surface.set_colorkey(transColor)
                self.cashe[self.path] = [1, self.image_surface]
        config.surface.blit(self.image_surface, self.pos)

    def reset(self):
        self.image_surface = False
        self.cashe[self.path][0] -= 1
        if self.cashe[self.path][0] == 0:
            del self.cashe[self.path]

    def __del__(self):
        self.reset()


class Shape(object):
    def __init__(self, *simple_shapes):
        self.simple_shapes = simple_shapes
        self.shape_pos_dep = []

        pos = self.simple_shapes[0].getPos()
        for shape in self.simple_shapes[1:]:
            self.shape_pos_dep.append((shape.pos[0] - pos[0], shape.pos[1] - pos[1]))

    def addShape(self, *simple_shapes):
        self.simple_shapes.extend(simple_shapes)

    def getPos(self):
        return self.simple_shapes[0].getPos()

    def setPos(self, pos):
        self.simple_shapes[0].setPos(pos)
        for i, shape in enumerate(self.simple_shapes[1:]):
            shape.setPos((pos[0] + self.shape_pos_dep[i][0], pos[1] + self.shape_pos_dep[i][1]))

    def move(self, vect):
        for shape in self.simple_shapes:
            shape.move(vect)

    def draw(self):
        for simple_shape in self.simple_shapes:
            simple_shape.draw()