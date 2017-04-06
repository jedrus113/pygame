from pygame import Color

from graphic.graphic_engine import GraphicEngine
from logic.logic import GameLogic


class Window:
    title = "Flying strawberry"
    size = (800, 500)
    lock_fps = 60.0

class World:
    background = Color("black")
    gravity_vector = (0, 10.0/Window.lock_fps)  # how hast items (player) accelerating with direction
    jump_vector = (0, -8)   # its one time boost, no need for div by frames lock
    score = 0   # init score
    objects = []    # object in world to take care of each render cycle
    pause = True    # game start paused

class Pipes:
    color = Color("Orange") # init colour
    speed = 1   # init speed, pipes do not accelerate

class Player:
    init_pos = (70, 300)    # init player pos
    size = (25,25)   # player model size

class Font:
    color = Color("White")

logic = GameLogic()
graphic = GraphicEngine()
