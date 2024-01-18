from abc import ABC, abstractmethod

from model.population import Population


class IModel(ABC):
    @abstractmethod
    def getFromKey(self, key: str) -> str:
        ...

    @abstractmethod
    def moveMobiles(self):
        ...

    @abstractmethod
    def getPopulation(self) -> Population:
        ...
