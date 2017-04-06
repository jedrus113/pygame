import pygame

from graphic.graphic_engine import GraphicEngine
from logic.logic import GameLogic


pygame.init()

class Window:
    title = "Flying strawberry"
    size = (800, 500)
    options = (pygame.RESIZABLE,)
    lock_fps = 60.0
    font = pygame.font.SysFont("monospace", 16)
    font.set_bold(True)

class World:
    background = pygame.Color("black")
    gravity_vector = (0, 10.0/Window.lock_fps)  # how hast items (player) accelerating with direction
    jump_vector = (0, -8)   # its one time boost, no need for div by frames lock
    score = 0   # init score
    objects = []    # object in world to take care of each render cycle
    pause = True    # game start paused
    score_board_pos = (50,50)

class Pipes:
    min_gap_beetween_pipes = 200
    minsize = 90
    maxsize = 300
    min_down_gap = 20
    min_top_gap = 20
    width = 50
    color = pygame.Color("Orange") # init colour
    speed = 1   # init speed, pipes do not accelerate

class Player:
    init_pos = (70, 300)    # init player pos
    size = (25,25)   # player model size

class Font:
    color = pygame.Color("White")

logic = GameLogic()
graphic = GraphicEngine()
