from model.mobile import Mobile
from model.sprite import Sprite

class Missile(Mobile):
    def __init__(self, sprite: Sprite, x: int, y: int, angle: float, sizeX: int, sizeY: int, opposite: int = 1):
        super().__init__(sprite, x, y, angle, 20.0, sizeX, sizeY, opposite)
        self.getSprite().rotateSprite(self.getAngle())
