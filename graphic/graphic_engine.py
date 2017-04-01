import pygame
from pygame.locals import Color

import config


class GraphicEngine:
    def __init__(self):
        self.speed = 0
        self.clock = pygame.time.Clock()
        self.display_options = (pygame.RESIZABLE,)
        self.background = Color("black")
        self.shapes = []

    def addShape(self, *shapes):
        self.shapes.extend(shapes)

    def on_init(self):
        pygame.init()
        config.surface = pygame.display.set_mode(config.screen_size, *self.display_options)
        pygame.display.set_caption(config.game_title)
        self._running = True
 
    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_1:
                self.speed = 0
            elif event.key == pygame.K_2:
                self.speed = 1
            elif event.key == pygame.K_0:
                self.speed = 999
                config.surface.fill([0, 0, 0])
                font=pygame.font.Font(None,30)
                scoretext=font.render("Fastforward", 1,(255,255,255))
                config.surface.blit(scoretext, (20, 20))
                pygame.display.flip()
        elif event.type == pygame.VIDEORESIZE:
            config.screen_size = event.size
            pygame.display.update()

    def on_render(self):
        if self.speed <= 1:
            config.surface.fill(self.background)

            for shape in self.shapes:
                shape.draw()

            self.clock.tick(config.lock_fps)
            pygame.display.flip()

    def on_cleanup(self):
        pygame.quit()
 
    def run(self):
        self._running = True
        if self.on_init() == False:
            self._running = False
        config.logic.on_init()
 
        while( self._running ):
            for event in pygame.event.get():
                self.on_event(event)
            config.logic.on_loop()
            self.on_render()
        self.on_cleanup()
