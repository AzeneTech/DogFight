import random
from abc import ABC, abstractmethod
from math import cos as cos
from math import sin as sin
from math import radians

from model.sprite import Sprite


class Mobile(ABC):
    __sprite: Sprite
    __x: int
    __y: int
    __angle: float
    __speed: float
    __opposite: int
    __distanceFlew: int
    __sizeX: int
    __sizeY: int

    def __init__(self, sprite: Sprite, x: int, y: int, angle: float, speed: float,  sizeX: int, sizeY: int, opposite: int):
        self.__sprite = sprite
        self.__x = x
        self.__y = y
        self.__angle = angle
        self.__speed = speed
        self.__opposite = opposite
        self.__distanceFlew = 0
        self.__sizeX = sizeX
        self.__sizeY = sizeY

    def getX(self):
        return self.__x

    def getY(self):
        return self.__y

    def setX(self, x: int):
        self.__x = x

    def moveX(self, max: int):
        self.__x = (self.__x + (cos(radians(self.__angle)) * self.__speed) * self.__opposite) % max
        self.__distanceFlew += self.__speed

    # def moveX(self, x: int, max: int):
    #     self.__x(cos(self.__angle) * self.__speed) * self.__opposite % max
    #     #self.__x = (self.__x + x) % max


    def setY(self, y: int):
        self.__y = y

    def moveY(self, max: int):
        self.__y = (self.__y + (sin(radians(self.__angle)) * self.__speed) * self.__opposite) % max

    # def moveY(self, y: int, max: int):
    #     self.__y = (self.__y + y) % max

    def rotate(self, rotationValue: float):
        newAngle = round(self.__angle + rotationValue, 2)
        if newAngle > 90:
            self.__angle = 90
        elif newAngle < -90:
            self.__angle = -90
        else:
            self.__angle = newAngle
        self.__sprite.rotateSprite(self.__angle)


    def getAngle(self) -> float:
        return self.__angle

    def getSpeed(self) -> float:
        return self.__speed

    def isOpposite(self) -> int:
        return self.__opposite

    def getSprite(self) -> Sprite:
        return self.__sprite

    def getDistanceFlew(self):
        return self.__distanceFlew

    def getHitbox(self):
        return ((self.__x - self.__sizeX, self.__x + self.__sizeX), (self.__y - self.__sizeY, self.__y + self.__sizeY), self.__angle)

    def explode(self):
        self.__sprite = Sprite("model\image\plane3")

    def randomizeY(self):
        self.__y = random.randint(0, 500)