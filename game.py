import pygame
from pygame.locals import *

#http://pygametutorials.wikidot.com/tutorials-three

class App:
    def __init__(self):
        self._running = True
        self._display_surf = None
        self._image_surf = None
        self.size = 10
        self.max_size = 100
        self.min_size = 1
        self.inc = 1
        self.fps = 0
        self._start_fps = 0
        self.last_tick = 0
        self.ms_beetween_frames = 32
        self.speed = 0
 
    def on_init(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode((350,350), pygame.HWSURFACE)
        self._running = True
        self._image_surf = pygame.image.load("food.bmp").convert()
        transColor = self._image_surf.get_at((0,0))
        self._image_surf.set_colorkey(transColor)
 
    def on_event(self, event):
        if event.type == QUIT:
            self._running = False
        elif event.type == KEYUP:
            if event.key == K_1:
                self.speed = 0
            elif event.key == K_2:
                self.speed = 1
            elif event.key == K_0:
                self.speed = 999
                self._display_surf.fill([0, 0, 0])
                font=pygame.font.Font(None,30)
                scoretext=font.render("Fastforward", 1,(255,255,255))
                self._display_surf.blit(scoretext, (20, 20))
                pygame.display.flip()

    def on_loop(self):
        pass

    def one_step(self):
        self.size += self.inc
        if self.size >= self.max_size or self.size <= self.min_size:
            self.inc = -self.inc


    def on_render(self):
        self.one_step()
        if self.speed <= 1:
            self._display_surf.fill([0, 0, 0])

            #self._display_surf.blit(self._image_surf,(x,y))

            pygame.draw.circle(self._display_surf, (0, 255, 255), [200,200], self.size)
            pygame.display.flip()

            act_tick = pygame.time.get_ticks()
            self.fps += 1
            if self._start_fps < act_tick - 1000:
                self._start_fps = act_tick
                print self.fps
                self.fps = 0
     
            if self.speed <= 0:
                time_passed = act_tick - self.last_tick
                ms_to_wait = self.ms_beetween_frames
                if time_passed < self.ms_beetween_frames:
                    ms_to_wait = self.ms_beetween_frames - time_passed
                pygame.time.wait(ms_to_wait)
                self.last_tick = pygame.time.get_ticks()

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
 
if __name__ == "__main__" :
    theApp = App()
    theApp.on_execute()
