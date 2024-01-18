
from model.mobile import Mobile
from model.sprite import Sprite

class Cloud(Mobile):
    def __init__(self, sprite: Sprite, x: int, y: int, angle: float, speed: float, sizeX: int, sizeY: int,opposite: int = 1):
        super().__init__(sprite, x, y, angle, speed, sizeX, sizeY, opposite)

