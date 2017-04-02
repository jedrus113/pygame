import pygame
from pygame.locals import Color

import config


class GraphicEngine:
    def __init__(self):
        self.clock = pygame.time.Clock()
        self.display_options = (pygame.RESIZABLE,)

    def on_init(self):
        pygame.init()
        config.surface = pygame.display.set_mode(config.screen_size, *self.display_options)
        pygame.display.set_caption(config.game_title)
        self._running = True
 
    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False
        elif event.type == pygame.KEYDOWN:
            config.keys.append(event.key)
        elif event.type == pygame.VIDEORESIZE:
            config.screen_size = event.size
            config.surface = pygame.display.set_mode(config.screen_size, *self.display_options)
            pygame.display.flip()

    def on_render(self):
        config.surface.fill(config.background)

        for thing in config.objects:
            thing.draw()

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
            config.keys = []
            for event in pygame.event.get():
                self.on_event(event)
            config.logic.on_loop()
            self.on_render()
        self.on_cleanup()
