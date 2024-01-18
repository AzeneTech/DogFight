from abc import ABC, abstractmethod

from shared.imodel import IModel
from model.population import Population


class IView(ABC):
    @abstractmethod
    def display(self, message) -> None:
        ...

    @abstractmethod
    def setModel(self, model: IModel):
        ...

    @abstractmethod
    def askYesNo(self, message: str) -> bool:
        ...

    @abstractmethod
    def showGame(self, population: Population = None):
        ...

    @abstractmethod
    def setController(self, controller) -> None:
        ...
