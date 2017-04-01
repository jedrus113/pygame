import pygame
import math

#config
game_title = "Snake"
screen_size = (500, 500)
lock_fps = 60
black = (0, 0, 0)

margin = 1
height = 20
width = 50

pygame.init()

screen = pygame.display.set_mode(screen_size, pygame.RESIZABLE)
pygame.display.set_caption(game_title)

clock = pygame.time.Clock()

# ---------------- Main Program Loop ---------------- #
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.VIDEORESIZE:
            screen_size = event.size
            screen = pygame.display.set_mode(screen_size, pygame.RESIZABLE)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            height += 10

    screen.fill(black)

    # Draw the grid
    for row in range(int(math.ceil(screen_size[1] / height)) + 1):
        for column in range(int(math.ceil(screen_size[0] / width)) + 1):
            color = (255,255,255)
            pygame.draw.rect(screen, color,
                             [(margin + width) * column + margin, (margin + height) * row + margin, width, height])

    # limit to `lock_fps` frames per second
    clock.tick(lock_fps)

    pygame.display.flip()

# IDE friendly line
pygame.quit()