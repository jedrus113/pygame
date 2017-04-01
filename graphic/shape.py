import pygame


class ShapeBase:
    def __init__(self, surface, pos):
        self.surface = surface
        self.pos = pos

    def setPos(self, pos=(0,0)):
        self.pos = pos

    def move(self, vect):
        self.pos = (self.pos[0] + vect[0], self.pos[1] + vect[1])

    def draw(self):
        raise NotImplementedError()


class Circle(ShapeBase):
    def __init__(self, surface, color, radius, pos=(0,0), width=0):
        super(Circle, self).__init__(surface, pos)
        self.color = color
        self.radius = radius
        self.width = width

    def draw(self):
        pygame.draw.circle(self.surface, self.color, self.pos, self.radius, self.width)


class image(ShapeBase):
    def __init__(self, surface, path, transparency=(0,0), pos=(0,0)):
        super(image, self).__init__(surface, pos)
        self.path = path
        self.image_surface = False
        self.transparency = transparency

    def draw(self):
        if not self.surface:
            self.surface = pygame.image.load("graphic/pics/food.bmp").convert()
            if self.transparency:
                transColor = self.surface.get_at((self.transparency))
                self.surface.set_colorkey(transColor)
        self.surface.blit(self.image_surface, self.pos)


class Shape():
    def __init__(self, *simple_shapes):
        self.simple_shapes = simple_shapes
        self.shape_pos_dep = []
        self.pos = self.simple_shapes[0].pos
        for shape in self.simple_shapes[1:]:
            self.shape_pos_dep.append((shape.pos[0] - self.pos[0], shape.pos[1] - self.pos[1]))

    def addShape(self, *simple_shapes):
        self.simple_shapes.extend(simple_shapes)

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