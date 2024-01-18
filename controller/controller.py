import time

from shared.action import Action
from shared.icontroller import IController
from shared.imodel import IModel
from shared.iview import IView
from model.missile import Missile
from model.sprite import Sprite

class Controller(IController):
    __view: IView
    __model: IModel
    __running: bool
    __pause: bool

    def __init__(self, view: IView, model: IModel):
        self.__view = view
        self.__model = model
        self.__view.setModel(self.__model)
        self.__view.setController(self)

    def getView(self) -> IView:
        return self.__view

    def getModel(self) -> IModel:
        return self.__model

    def start(self):
        self.__running = True
        self.__pause = False
        self.__view.showGame(self.__model.getPopulation())
        self.__gameLoop()

    def __gameLoop(self):
        while self.__running:
            if not self.__pause:
                self.__model.moveMobiles()
            self.__view.showGame(self.__model.getPopulation())
            # time.sleep(0.0001)
            time.sleep(0.01)


    def performAction(self, action: Action):
        if action == Action.CLOSE:
            self.__running = False
        elif action == Action.PAUSE:
            self.__pause = not self.__pause
        elif action == Action.LEFT:
            self.__model.getPopulation().getPlane(0).rotateSprite(int(self.__model.getFromKey("rotateSpeed")))
        elif action == Action.RIGHT:
            self.__model.getPopulation().getPlane(0).rotateSprite(-int(self.__model.getFromKey("rotateSpeed")))
        elif action == Action.FIRE:
            missile = Missile(Sprite("model/image/missile1.png"), self.__model.getPopulation().getPlane(0).getX() + 120,
                        self.__model.getPopulation().getPlane(0).getY(),
                        self.__model.getPopulation().getPlane(0).getAngle(), self.__model.getFromKey("missileSizeX"), self.__model.getFromKey("missileSizeY"))
            self.__model.getPopulation().addMissile(missile)

            self.__model.getPopulation().getPlane(0).addMissile(missile)

        elif action == Action.FIRE2:
            missile = Missile(Sprite("model/image/missile2.png"), self.__model.getPopulation().getPlane(1).getX() - 120,
                              self.__model.getPopulation().getPlane(1).getY(),
                              self.__model.getPopulation().getPlane(1).getAngle(), self.__model.getFromKey("missileSizeX"), self.__model.getFromKey("missileSizeY"), -1)
            self.__model.getPopulation().addMissile(missile)

            self.__model.getPopulation().getPlane(1).addMissile(missile)
        elif action == Action.RESTART:
                    self.performAction(Action.CLOSE)
                    # controller = Controller(ViewTkinter(), Model())
                    # controller.start()

