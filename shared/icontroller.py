from abc import ABC, abstractmethod

from shared.imodel import IModel
from shared.iview import IView


class IController(ABC):
    @abstractmethod
    def getView(self) -> IView:
        ...

    @abstractmethod
    def getModel(self) -> IModel:
        ...

    @abstractmethod
    def start(self):
        ...

    def performAction(self, action) -> None:
        ...
