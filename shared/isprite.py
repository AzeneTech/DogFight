from abc import ABC, abstractmethod


class ISprite(ABC):
    @abstractmethod
    def getImage(self) -> str:
        ...

    def rotateSprite(self, angle: float):
        ...
