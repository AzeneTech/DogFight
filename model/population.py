from model.mobile import Mobile
from model.plane import Plane
from model.missile import Missile
from model.cloud import Cloud
class Population:
    __planes: [Plane]
    __missiles: [Missile]
    __mobiles: [Mobile]
    __clouds: [Cloud]
    def __init__(self):
        self.__planes = []
        self.__missiles = []
        self.__mobiles = []
        self.__clouds = []
    def addPlane(self, plane: Plane):
        self.__planes.append(plane)
        self.addMobiles(plane)

    def getPlane(self, index: int = None) -> [Plane]:
        if index is not None:
            return self.__planes[index]
        else:
            return self.__planes

    def addMissile(self, missile: Mobile) -> object:
        self.__missiles.append(missile)
        self.addMobiles(missile)

    def getMissile(self, index: int = None) -> [Mobile]:
        if index is not None:
            return self.__missiles[index]
        else:
            return self.__missiles

    def addCloud(self, cloud: Cloud):
        self.__clouds.append(cloud)
        self.addMobiles(cloud)

    def getCloud(self):
        return self.__clouds

    def addMobiles(self, mobile: Mobile) -> None:
        self.__mobiles.append(mobile)

    def getMobiles(self) -> [Mobile]:
        return self.__mobiles

    # def delMissile(self, missile: Missile):
    #     if self.__missiles != []:
    #         self.__missiles.remove(missile)
    #         self.__mobiles.remove(missile)
    #         missile.explode()

    # def explodePlane(self, mobile: Mobile):
    #     self.__planes.remove(mobile)
    #     self.__mobiles.remove(mobile)
    #     mobile.explode()

    def delMobile(self, mobile: Mobile):
        if isinstance(mobile, Cloud):
            if self.__clouds != []:
                self.__clouds.remove(mobile)
        elif isinstance(mobile, Plane):
            self.__planes.remove(mobile)
        elif isinstance(mobile, Missile):
            if self.__missiles != []:
                self.__missiles.remove(mobile)

        self.__mobiles.remove(mobile)
        mobile.explode()
