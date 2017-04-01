import pygame

#http://pygametutorials.wikidot.com/tutorials-three
import config


class GraphicEngine:
    def __init__(self):
        self._running = True
        self.screen = None
        self._image_surf = None
        self.size = 10
        self.max_size = 100
        self.min_size = 1
        self.inc = 1
        self.speed = 0
        self.clock = pygame.time.Clock()
        self.display_options = (pygame.RESIZABLE,)
 
    def on_init(self):
        pygame.init()
        self.screen = pygame.display.set_mode(config.screen_size, *self.display_options)
        pygame.display.set_caption(config.game_title)
        self._running = True
        self._image_surf = pygame.image.load("graphic/pics/food.bmp").convert()
        transColor = self._image_surf.get_at((0,0))
        self._image_surf.set_colorkey(transColor)
 
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
                self.screen.fill([0, 0, 0])
                font=pygame.font.Font(None,30)
                scoretext=font.render("Fastforward", 1,(255,255,255))
                self.screen.blit(scoretext, (20, 20))
                pygame.display.flip()
        elif event.type == pygame.VIDEORESIZE:
            config.screen_size = event.size
            self.screen = pygame.display.set_mode(config.screen_size, *self.display_options)

    def on_loop(self):
        self.size += self.inc
        if self.size >= self.max_size or self.size <= self.min_size:
            self.inc = -self.inc

    def on_render(self):
        if self.speed <= 1:
            self.screen.fill([0, 0, 0])

            self.screen.blit(self._image_surf,(230,170))

            pygame.draw.circle(self.screen, (0, 255, 255), [200,200], self.size)

            self.screen.blit(self._image_surf,(200,170))

            self.clock.tick(60)
            pygame.display.flip()

    def on_cleanup(self):
        pygame.quit()
 
    def on_execute(self):
        if self.on_init() == False:
            self._running = False
 
        while( self._running ):
            for event in pygame.event.get():
                self.on_event(event)
            self.on_loop()
            self.on_render()
        self.on_cleanup()
