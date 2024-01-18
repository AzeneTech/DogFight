import json
import random

from model.plane import Plane
from model.population import Population
from shared.imodel import IModel
from model.sprite import Sprite
from model.cloud import Cloud

class Model(IModel):
    __data: dict
    # __step: int
    __population: Population
    __oppositeList = [-1, 1]

    def __init__(self):
        # self.__step = 0
        self.__population = Population()
        with open("data/data.json") as jsonfile:
            self.__data = json.load(jsonfile)
        self.__population.addPlane(
            Plane(Sprite(self.getFromKey("plane1")), self.getFromKey("plane1StartX"), self.getFromKey("plane1StartY"), 0.0, self.getFromKey("planeSizeX"), self.getFromKey("planeSizeY")))

        self.__population.addPlane(
            Plane(Sprite(self.getFromKey("plane2")), self.getFromKey("plane2StartX"), self.getFromKey("plane2StartY"), 0.0, self.getFromKey("planeSizeX"), self.getFromKey("planeSizeY"), -1))
        self.__population.addCloud(
                 Cloud(Sprite(self.getFromKey("cloud")), self.getFromKey("width"),
                       random.randint(0, self.getFromKey("height")), 0.0, random.randint(10, 20), self.getFromKey("planeSizeX"), self.getFromKey("planeSizeY"), self.__oppositeList[random.randint(0, 1)]))

        self.__population.addCloud(
                 Cloud(Sprite(self.getFromKey("cloud")), self.getFromKey("width"),
                       random.randint(0, self.getFromKey("height")), 0.0, random.randint(10, 20), self.getFromKey("planeSizeX"), self.getFromKey("planeSizeY"), self.__oppositeList[random.randint(0, 1)]))

        self.__population.addCloud(
                 Cloud(Sprite(self.getFromKey("cloud")), self.getFromKey("width"),
                       random.randint(0, self.getFromKey("height") - 100), 0.0, random.randint(10, 20), self.getFromKey("planeSizeX"), self.getFromKey("planeSizeY"), self.__oppositeList[random.randint(0, 1)]))

        for mobile in self.__population.getMobiles():
            if isinstance(mobile, Cloud):
                pass
            else:
                mobile.getSprite().rotateSprite(0)


    def getFromKey(self, key: str):
        try:
            return self.__data[key]
        except KeyError:
            return "Key " + key + " unknown"

    def moveMobiles(self):

        for mobile in self.__population.getMobiles():

            mobile.moveX(int(self.__data["width"]))
            #mobile.moveX((cos(mobile.getAngle()) * mobile.getSpeed()) * mobile.isOpposite(), int(self.__data["width"]))
            mobile.moveY(int(self.__data["height"]))
            #mobile.moveY((sin(mobile.getAngle()) * mobile.getSpeed()) * mobile.isOpposite(), int(self.__data["height"]))


    def getPopulation(self) -> Population:
        return self.__population

    # def getPlaneX(self):
    #     return (int(self.__data["planeStartX"]) + self.__step) % int(self.__data["width"])

    # def getPlaneY(self):
    #     return int(self.__data["planeStartY"])
