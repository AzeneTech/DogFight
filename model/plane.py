from model.mobile import Mobile
from model.sprite import Sprite

from model.missile import Missile

class Plane(Mobile):
    __missiles: [Missile]
    def __init__(self, sprite: Sprite, x: int, y: int, angle: float, sizeX: int, sizeY: int, opposite: int = 1):
        super().__init__(sprite, x, y, angle, 10, sizeX, sizeY, opposite)
        self.__missiles = []

    def addMissile(self, missile: Missile):
        self.__missiles.append(missile)

    def delMissile(self, missile: Missile):
        self.__missiles.remove(missile)

    def getMissile(self) -> [Missile]:
        return self.__missiles
