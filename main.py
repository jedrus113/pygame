import config
from logic.logic import GameLogic
from graphic.graphic_engine import GraphicEngine

config.logic = GameLogic()
config.graphic_engine = GraphicEngine()
config.graphic_engine.run()