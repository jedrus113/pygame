import pygame

import config


class GraphicEngine:
    def __init__(self):
        self.clock = pygame.time.Clock()

    def on_init(self):
        self.surface = pygame.display.set_mode(config.Window.size, *config.Window.options)
        pygame.display.set_caption(config.Window.title)
        self._running = True
 
    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False
        elif event.type == pygame.KEYDOWN:
            config.logic.keyDown(event.key)
        elif event.type == pygame.VIDEORESIZE:
            config.Window.size = event.size
            self.surface = pygame.display.set_mode(config.Window.size, *config.Window.options)
            pygame.display.flip()

    def on_render(self):
        self.surface.fill(config.World.background)

        for thing in config.World.objects:
            thing.draw()

        self.clock.tick(config.Window.lock_fps)
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
