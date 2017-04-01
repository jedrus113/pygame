
class GameLogic:
    def __init__(self, graphic):
        self.graphic = graphic

    def on_loop(self):
        self.graphic.size += self.graphic.inc
        if self.graphic.size >= self.graphic.max_size or self.graphic.size <= self.graphic.min_size:
            self.graphic.inc = -self.graphic.inc