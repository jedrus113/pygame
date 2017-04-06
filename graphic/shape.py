import pygame

import config


class ShapeBase(object):
    def __init__(self, pos):
        self.pos = pos

    def getPos(self):
        return self.pos

    def getPosInt(self):
        return (int(self.pos[0]), int(self.pos[1]))

    def setPos(self, pos=(0,0)):
        self.pos = pos

    def move(self, vect):
        self.pos = (self.pos[0] + vect[0], self.pos[1] + vect[1])

    def draw(self):
        raise NotImplementedError()


class RectShape(ShapeBase):
    def __init__(self, color, pos, size, width=0):
        super(RectShape, self).__init__(pos)
        self.color = color
        self.size = size
        self.width = width

    def draw(self):
        pygame.draw.rect(config.graphic.surface, self.color, (self.getPosInt()[0], self.getPosInt()[1], self.size[0], self.size[1]), self.width)

class CircleShape(ShapeBase):
    # size / radius = int
    def __init__(self, color, radius, pos=(0,0), width=0):
        super(CircleShape, self).__init__(pos)
        self.color = color
        self.size = radius
        self.width = width

    def draw(self):
        pygame.draw.circle(config.graphic.surface, self.color, self.getPosInt(), self.size, self.width)

class TextShape(ShapeBase):
    def __init__(self, pos, text):
        super(TextShape, self).__init__(pos)
        self.myfont = pygame.font.SysFont("monospace", 16)
        self.myfont.set_bold(True)
        self.text = text

    def draw(self):
        scoretext = self.myfont.render(self.text, 1, config.Font.color)
        config.graphic.surface.blit(scoretext, self.getPos())

class ImageShape(ShapeBase):
    cashe = {}
    # path = str path to file with picture, left top corner show transparency
    # size = tuple (withd, heitht) in px
    def __init__(self, path, pos=(0,0), size=None):
        super(ImageShape, self).__init__(pos)
        self.path = path
        self.size = size

        if self.path in self.cashe:
            self.cashe[self.path][0] += 1
            self.image_surface = self.cashe[self.path][1]
        else:
            self.image_surface = pygame.image.load(self.path).convert()
            transColor = self.image_surface.get_at((0, 0))
            self.image_surface.set_colorkey(transColor)
            self.cashe[self.path] = [1, self.image_surface]
        if not self.size:
            self.size = self.image_surface.get_size()


    def draw(self):
        config.graphic.surface.blit(pygame.transform.scale(self.image_surface, self.size), self.getPosInt())

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